CAN Primer
==========

On OreSat, two CAN 2.0A (aka classic CAN with 11-bit identifier) buses are used
for the main communication bus beteen OreSat cards.

See the Wikipedia page for CAN at https://en.wikipedia.org/wiki/CAN_bus for
the basics, it is fairly complete. No reason to repeat it here.

Virtual CAN Bus
---------------

Linux support make a vcan (Virtual CAN) bus. A vcan bus can be super usefuly
for developement.

To make a vcan bus on Linux:

.. code:: bash
  
   $ sudo ip link add dev vcan0 type vcan
   $ sudo ip link set vcan0 up

Software Utilities
------------------

candump
*******

The ``candump`` utility from the `can-utils`_ package can be used to monitor
the raw CAN message over a CAN bus. The first column is the CAN bus being
monitored, the second column is the ``COB-ID`` in hex, and the third column
is the size of CAN message (0 to 8), and the rest is the CAN message as an
octet string (hex values seperated by spaces).


.. code:: bash

  $ candump vcan0
    vcan0  710   [1]  05
    vcan0  080   [0]
    vcan0  710   [1]  05
    vcan0  610   [8]  40 18 10 00 00 00 00 00

For more info, see https://manpages.debian.org/testing/can-utils/candump.1.en.html

cansend
*******

The ``cansend`` utility from the `can-utils`_ package can be used to send
message over the CAN bus.

.. code:: bash

   $ cansend vcan0 190#05.10

.. code:: bash

  $ candump vcan0
    vcan0  190   [2]  05 10

For more info, see https://manpages.debian.org/testing/can-utils/cansend.1.en.html

Hardware
--------

A `CANable`_ can be used to connect to a CAN bus with a laptop. These are not
needed if using a vcan (virtual CAN) bus for developement.

Bash command to connect to a `CANable`_ using the slcand firmware.

.. code:: bash

  $ slcand -o -c -s8 /dev/ttyACM1 can0

The systemd-networkd config file to use a `CANable`_ using the candlelight firmware.

.. code::

   # /etc/systemd/network/50-can.network

  [Match]
  Name=can0

  [Link]
  RequiredForOnline=no

  [CAN]
  BitRate=1M

.. _CANable: https://canable.io/
.. _can-utils: https://github.com/linux-can/can-utils
