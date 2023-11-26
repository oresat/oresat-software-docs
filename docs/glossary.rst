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
        Cirrus Flux Camera. The science payload for OreSat.

    SDR
        Software-Defined Radio. Radio communications that are traditionally
        implemented in hardware are instead implemented in software.

    C3
        Command, communication, and control card. It is the flight computer for
        OreSat.

    CAN
        Control Area Network. A message bus for embedded systems common in the
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
        Handheld Ground Station. Ground part of the OreSat Live system.

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
        FlatSat and FlatClOGS together. A full HIL satellite and ground
        station for integration and testing.

    Telecommand
        A command message sent to a satellite.

    Telemetry
        Health and status information from a satellite.

    OTA
        Over the Air. Any type of wireless transmission.

    SDO
        Service Data Object. A sequence of CANopen messages for a node to
        read or write a value to another node OD.

    PDO
        Process Data Object. A broadcast type CANopen message for a
        node that none, one, or many other nodes can consume.

    EMCY
        Emergency Object. A broadcast CANopen message to mark an error on a node used
        for diagnostics.

    OreSat Live
        The outreach payload for OreSat that stream live video of earth to an HGS.

    HIL
        Hardware-in-the-loop. A test bench setup for testing and validating
        software with the real hardware.

    Octet
        A unit of 8-bits. In communications, it is common to the unit octet, as
        the unit byte has historically been platform-dependent, while an octet
        has always been 8-bits.

    CCSDS
        Consultative Committee for Space Data System. A committee of governmental
        space-agencies to discuss and develop standards for space data and information
        systems. See https://public.ccsds.org/default.aspx

    USLP
        Unified Space Data Link Protocol. A CCSDS communications protocol to be used
        by space missions for space-to-ground or space-to-space communications links.

    CFDP
        CCSDS File Delivery Protocol. A CCSDS file transfer protocol to be used
        by space missions.

    XTCE
        XML Telemetric and Command Exchange. An XML-based file for defining
        a spacecraft's telemetry and telecommand data format.

    ECSS
        European Cooperation for Space Standardization. Collibration of the 
        ESA (European Space Agency), the European space industries, and several space 
        agencies, to develop and maintain space mission standards for European space
        missions.

    SCET
        Spacecraft Elapsed Time.

    TPDO
        Transmit PDO
    
    RPDO
        Recieve PDO

    COB-ID
        Communication Object Identifier. Used to identify a CANopen messages.
