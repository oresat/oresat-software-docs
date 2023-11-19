.. _glossary:

=========
 Glossary
=========

.. glossary::
    :sorted:

    CubeSat
        A small satellite is made up of multiples of 10cm × 10cm × 10cm cubic
        units.

    OreSat
        PSAS's open source CubeSat. See https://www.oresat.org/

    PSAS
        Portland State Aerosapce Society. A student aerospace group at Portland
        State University. See https://www.pdxaerospace.org/

    CFC
        Cirrus Flux Camera. One of OreSat payloads and a Linux card.

    SDR
        Software Define Radio. Radio communications that are traditionally
        implemented in hardware are instead implemented in software.

    C3
        Command, communication, and control card. It is the flight computer for
        OreSat. See https://github.com/oresat/oresat-c3

    CAN
        Control Area Network. A message bus for embedded systems common is the
        automotive industry.

    CANopen
        A communication protocol and device profile specification for a CAN 
        bus defined by CAN in Automation. More info at https://can-cia.org/

    OLAF
        OreSat Linux Application Framework. The pythonic CANopen application
        framework for all OreSat Linux cards. See
        https://github.com/oresat/oresat-olaf

    OD
        Object Dictionary. The main data structure of a CANopen node.

    OPD
        OreSat Power Domain. Allows the C3 to turn other cards on or off.

    UniClOGS
        University Class Open Ground Station. The ground station for OreSat.
        See https://www.uniclogs.org/

    HGS
        Handheld Ground Station. Apart of the OreSat Live Mission.

    EDL
        Engineering Data Link. The main communication data link between OreSat
        and UniClOGS used for commanding OreSat and uploading/downloading
        files to/from OreSat.

    SatNOGS
        A open source global network of satellite ground stations. See
        https://satnogs.org/

    FlatSat
        The develment enviroment for OreSat. The dev OreSat is layout flat on
        a table, hence the name FlatSat.

    FlatClOGS
        A develment enviroment for UniClOGS software connected to FlatSat.

    OreFlat
        FlatSat and FlatClOGS together. A full hardware-in-loop satellite 
        and ground station for integration and testing.

    Telecommand
        A command message sent to a satellite.

    Telemetry
        Health and status information from a satellite.

    OTA
        Over the Air. Is any type of wireless transmission.

    SDO
        Service Data Object. A sequence of CANopen messages for a node to
        read or write a value to another node OD.

    PDO
        Product Data Object. A broadcast type CANopen message for a
        node that none, one, or many other nodes can consume.

    EMCY
        Emergency. A broadcast CANopen message to mark an error on a node used
        for diagnostics.
