CANopen Primer
==============

.. note:: 

  This only goes over the basics of CANopen for what is need to work on a
  OreSat device. For the full standards, see the `CAN in Automation (CiA)`_
  website.

`CANopen`_ is a message protocol for `CAN`_ messages on a `CAN`_ bus by 
`CAN in Automation (CiA)`_.

CANopen only uses little endian in its messages.

Nodes
-----

A node is a CANopen device.

All nodes will have an unique ``NODE-ID``, between ``0x01`` and ``0x7F``.

.. note::
   On OreSat, the C3 will always have the ``NODE-ID`` of ``0x01``.
   All nodes other than the C3 have ``NODE-IDs`` are multiples of ``0x04``; 
   e.g: ``0x04``, ``0x08``, ``0x12``, etc. See the notes in the PDO section
   for the reasoning.

OD (Object Dictionary)
----------------------

The data structure that hold all data for CANopen node.

Objects can have indexes and subindex.
Valid indexes range from ``0x1000`` to ``0x8000`` and valid subindexes range from
``0x00`` to ``0xFF``.

Objects at an index can be Variables, Arrays, or Records.  

Variable
********

- Can be at a index or at a subindex of a Record/Array.
- Has a access type of readonly, writeonly, readwrite, or constant.
- Has a default value (if not set it will be 0 or something similar for the data type).
- Optional, callbacks can be setup by software on read and/or writes.

Data Types
^^^^^^^^^^
.. csv-table::
   :header: "Name", "C Data Type", "Description"

   "BOOLEAN", "bool", "A true / false value"
   "INTEGER8", "int8_t", "8-bit signed integer"
   "INTEGER16", "int16_t", "16-bit signed integer"
   "INTEGER32", "int32_t", "32-bit signed integer"
   "INTEGER64", "int64_t", "64-bit signed integer"
   "UNSIGNED8", "uint8_t", "8-bit unsigned integer"
   "UNSIGNED16", "uint16_t", "16-bit unsigned integer"
   "UNSIGNED32", "uint32_t", "32-bit unsigned integer"
   "UNSIGNED64", "uint64_t", "64-bit unsigned integer"
   "REAL32", "float", "32-bit floating point number"
   "REAL64", "double", "64-bit (double-precision) floating point number"
   "VISABLE_STRING", "char []", "An ASCII string"
   "OCTET_STRING", "uint8_t []", "An octet string"
   "DOMAIN", "void \*", "A null value that must be have callback function(s)"

.. note:: There are other standard CANopen data types, but they are omitted as
   they are unused by OreSat.

Array
*****

- Can only be at an index.
- All subindexes other than subindex ``0x00``, must be the same data type.
- Subindex ``0x00`` is a Variable with value of the highest subindex.
- Variables in a Array do not have have sequential subindex; e.g.: a 
  Array can have object at subindexes ``0x00``, ``0x01``, ``0x04`` (no objects 
  at ``0x02`` or ``0x03`` in this example).

Record
******

- Can only be at an index.
- Subindex ``0x00`` is a Variable with value of the highest subindex.
- Variables in a Record do not have have sequential subindex; e.g.: a 
  Record can have object at subindexes ``0x00``, ``0x01``, ``0x04`` (no objects 
  at ``0x02`` or ``0x03`` in this example).

Object Groups
*************

Indexes can be divide into 3 groups: Mandatory, Manufacture, and Optional.

- Mandatory Objects (``0x1000``, ``0x1001``, ``0x1018``) are required indexes
  for all nodes.
- Manufacture Objects (``0x2000`` to ``0x5FFF``) are objects added by
  manufacturer.
- Optional Objects (``0x1000`` to ``0x1FFF`` and ``0x6000`` to ``0x8000``) are
  objects added by user.

.. note::
   On OreSat:

   - Indexes ``0x1000`` to ``0x2FFF`` are reserved for CANopen standard objects
   - Indexes ``0x3000`` to ``0x3FFF`` are reserved for common OreSat objects between all cards
   - Indexes ``0x4000`` to ``0x4FFF`` are reserved for unique OreSat objects for a card
   - Indexes ``0x5000`` to ``0x5FFF`` are reserved for mapped RPDO objects
   - Indexes above ``0x6000`` are not used.

Files
-----

Both EDS and DCF files are used to document and configure a CANopen device as
well as generate code for the OD for software / firmware.

EDS (Electronic Data Sheet)
***************************

An EDS file a ``.conf`` or ``.ini`` like configuration file for describing the
OD. It is used as the documentation and configuration file of a device.

DCF (Device Configure File)
***************************

A DCF file is mostly a EDS file with a extra section for device configuration
like ``NODE-ID``, node name, and other node unique things.

A EDS is general file for a device and is used to generate the DCF. The DCF is
used when the device is on an actual production CAN bus. 

The main benefit of a DCF is if there are multiple of the exact same device on
the CAN bus, they all will have an unique DCF that was made from the same EDS 
file. 

.. note::
   For OreSat, EDS / DCF files are not used anymore. They were to hard to keep in sync,
   a one change to a card EDS could effect all other cards. Now a centralized database
   of OD definitions as YAML files can be found in the `oresat-configs`_ git repo. 
   Each YAML config acts like EDS, but as all configs are loaded in by script the 
   resulting data gets turned  into a DCF equivalent. Also, all YAML config file are
   much smaller and easier to quickly understand than an EDS/DCF file.

Messages
--------

``COB-ID`` term is used as the name of the 11-bit identifier field of a CAN
message for a CANopen message.

``COB-ID`` is made up of 4-bits for the CANopen message id and 7-bits for the
``NODE-ID``.

CANopen nodes use the ``COB-ID`` to id all messages.

Heartbeat
*********

All node send out a 1-byte heartbeat message with a ``COB-ID`` of
``0x700 + NODE-ID``.

Heartbeat consumer node(s) can use the heartbeat message to confirm what boards are
on and in a good state.

.. csv-table::
   :header: "Value", "Description"

   "0x00", "Boot up"
   "0x04", "Stopped"
   "0x05", "Operational"
   "0x7F", "Pre-operational"

Example heartbeat messages from node ``0x10``

.. code:: bash

  $ candump vcan0
    vcan0  710   [1]  05
    vcan0  710   [1]  05
    vcan0  710   [1]  05


.. note::
   On OreSat, all nodes (including the C3) broadcast a heartbeat every second. The C3
   monitors all heartbeats.

SDO (Service Data Object)
*************************

SDOs allow a node to upload or download an object value to or from another node's OD.
The initiating node acts as the client and the node it is communicating with acts as the
server in `client-server model`_. A upload can also be thought of as a write; where 
the client upload/writes a value to the server. A download can also be thought of as 
a read; where the client download/reads a value from the server.

SDOs are the only messages that span over multiple CAN message, as the value
that is being read or written can be any length as defined by OD.

A SDO client will use a ``COB-ID`` of ``0x580 + NODE-ID`` of the node that being is reading
from or writing to (``NODE-ID`` is the id of SDO server). A SDO server will respond using
a ``COB-ID`` of ``0x600 + NODE-ID`` (its own ``NODE-ID``).

There are 3 types of SDOs; expedited, segmented, and block. CANopen libraries can determine the best
SDO type based off of the value's data type.

- **Expedited** is for message with data type of equal to or less than 4-bytes. Only one request
  message is sent, and one ACK/NACK like message is returned. On a write, the last 4-bytes of
  the request are the value being written. On a read, the last 4-bytes of the response are the
  value (if no error).
- **Segmented** is for message with data type of greater than 4-bytes. More than one request message
  is sent. On every request message, an response message is sent back. This is useful for larger
  data types like int64, uint64, float64, etc. Is consider the default SDO transaction type.
- **Block** is for large block data (typically for a DOMAIN data type). Data is sent in block of
  127 message and then a CRC is applied to the block, if the block is valid the next block is sent.
  For bulk data transfers, block type transfers are way more efficient than a Segmented type transfer;
  One ACK every 127 message vs on every message.

Example expedited SDO download from node ``0x10`` from index ``0x1018`` subindex ``0x00``.

.. code:: bash

  $ candump vcan0
    vcan0  610   [8]  40 18 10 00 00 00 00 00
    vcan0  590   [8]  4F 18 10 00 04 00 00 00

.. note::
   On OreSat, only the C3 will act as the SDO client and all other nodes are SDO servers.
   Expedited SDOs are used by the C3 to command and control all other nodes. Block SDOs are
   used for file transfers.

PDO (Process Data Object)
*************************

PDOs are producer / consumer type message. Any node can produce or consume PDO,
if configured.

There are two type of PDOs: TPDO (Transmit PDO) and RPDO (Receive PDO).
A node can produce data using TPDO and consume data using RPDO.

All PDOs are 1 to 8-byte message of mapped data from/to the OD.

Both RPDO and TPDO can be set up to be sent out every X SYNC message or on a
timer.

All nodes get 4 TPDOs and RPDOs by default, TPDO ``COB-ID`` are 
``0x180 + NODE-ID``, ``0x280 + NODE-ID``, ``0x380 + NODE-ID``, 
``0x480 + NODE-ID``. RPDO ``COB-ID`` are ``0x200 + NODE-ID``, 
``0x300 + NODE-ID``, ``0x400 + NODE-ID``, ``0x500 + NODE-ID``.

So a board with ``NODE-ID`` ``0x04`` can use the following 4 ``COB-ID`` for it's TPDOs:
``0x184``, ``0x284``, ``0x384``, ``0x484`` and 4 ``COB-ID`` for it's RPDOs:
``0x204``, ``0x304``, ``0x404``, ``0x504``.

Example TPDOs from node ``0x10``

.. code:: bash

  $ candump vcan0
    vcan0  190   [6]  2D 17 1B 00 00 00
    vcan0  290   [2]  00 00

.. note::
   On OreSat, the C3 will consume all TPDOs, all other nodes will produce and/or
   consume TPDOs as needed. All beacon data will be sent to the C3 via TPDOs.

.. note::
   As mention in the Node section above. All nodes on OreSat use a ``NODE-ID`` with a
   multiple of ``0x04``.

   This is done as 4 TPDOs (a total of 64 bytes of data) is not enough for OreSat
   Nodes. So PSAS decided to give all nodes 4 times the normal PDOs. So a OreSat
   CANopen node now has 256 bytes for telemetry.

   All nodes they use the PDOs of +1, +2, +3 to their ``NODE-IDs`` with a exception
   of the C3, which only has PDOs of +1, +2 of it's ``NODE-ID``.

   An example of board with ``NODE-ID`` of ``0x04``:

   - No nodes with ``NODE-ID`` of ``0x05``, ``0x06``, ``0x07`` will exist on
     OreSat.
   - Can use the following 16 TPDOs: ``0x184``, ``0x284``, ``0x384``, ``0x484``, 
     ``0x185``, ``0x285``, ``0x385``, ``0x485``, ``0x186``, ``0x286``, ``0x386``,
     ``0x486``, ``0x187``, ``0x287``, ``0x387``, and ``0x487``.
   - Can use the following 16 RPDOs: ``0x204``, ``0x304``, ``0x404``, ``0x504``, 
     ``0x205``, ``0x305``, ``0x405``, ``0x505``, ``0x206``, ``0x306``, ``0x406``, 
     ``0x506``, ``0x207``, ``0x307``, ``0x407``, and ``0x507``.

SYNC
****

A message that TPDO can be configure to response to after every X occurrences.
A SYNC message always has ``COB-ID`` of ``0x80`` with no payload.

Example SYNC message

.. code:: bash

  $ candump vcan0
    vcan0  080   [0]

.. note::
   On OreSat, the C3 is the SYNC producer, all other nodes are consumers.

EMCY (Emergency)
****************

An error message from the node. Useful for diagnostic.
A EMCY message has a ``COB-ID`` of ``0x80 + NODE-ID``.

.. csv-table::
   :header: "Name", "Bytes", "Description"

   "EEC", "2", "Emergency error code, a classification of the error"
   "ER", "1", "Error register, value from index ``0x1001``; a ongoing bit field of the active errors"
   "MSEF", "5", "Manufacturer-specific error code, defined by PSAS"

Example EMCYs from node ``0x10``

.. code:: bash

  $ candump vcan0
    vcan0  090   [8]  00 01 01 01 02 03 04 05
    vcan0  090   [8]  00 22 05 12 34 56 78 90

.. note::
   On OreSat, the C3 is the EMCY consumer, all nodes (including the C3) are EMCY producers. 

Time Sync
---------

.. warning:: This is not CANopen standard, but is used on OreSat.

The time sync message on OreSat uses the SCET format with the Unix
time stamp as the epoch. SCET is from the ECSS CAN bus extension
protocol standard.

ECSS SCET Definition
********************

.. code-block::

    struct {
        unsigned 32 Coarse Time
        unsigned 24 Fine Time (sub seconds)
    } scet

On OreSat the SCET value is a uint64 with Coarse Time first 4 bytes,
followed by the Fine Time 3 bytes, and the final byte is padding.

Time Syncing
************

Time syncing is handle by the C3 and the GPS board. The TPDO with ``COB-ID`` of
``0x181`` is reserved to be the Time Sync TPDO. Both the C3 and GPS board can
send it. All nodes that care about time, except the node that sent the Time
Sync TPDO, will sync their clocks to the time in the Time Sync TPDO when it is
received. 

The C3 has an RTC (Real Time Clock) and the GPS board has a GPS receiver and
will set it's system time to the GPS time in GPS messages.

The GPS board will only send the Time Sync TPDO, if has sync it's system time
to GPS time and it receives a SYNC message from the C3. So, either way the C3
has full control when all clocks are synchronized. The C3 can just send out the Time
Sync TPDO (it will use the time from it's RTC) or request it from the GPS
board, if the GPS board is on.

Software Utilities
------------------

The `CANopen Monitor`_ project can be used to monitor the decoded CANopen
messages over a CAN bus. It is a TUI that displays the decode values, so you do
not have to convert the raw hex values from ``candump`` to their "real" values.
Also, ``candump`` is great at quickly testing a node or two, but can easily
become impossible to read once several node start sending data across the CAN
bus or when a large block data transfer is in progress, so `CANopen Monitor`_
becomes more reasonable for viewing CANopen messages on the CAN bus.

.. _CANopen: https://en.wikipedia.org/wiki/CANopen
.. _CAN: https://en.wikipedia.org/wiki/CAN
.. _CAN in Automation (CiA): https://can-cia.org/
.. _CANopen Monitor: https://github.com/oresat/CANopen-monitor
.. _can-utils: https://github.com/linux-can/can-utils
.. _CANable: https://canable.io/
.. _client-server model: https://en.wikipedia.org/wiki/Client-server_model
.. _oresat-configs: https://github.com/oresat/oresat-configs
