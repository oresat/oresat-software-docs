Git Repositories
================

Common
------

Common repos for all OreSat Linux Cards.

- `oresat-linux`_ OreSat Linux image builder and general image utilities.
- `oresat-configs`_ Configs for all CANopen-based OreSat projects. Defines all ODs for all OreSat
  cards.
- `oresat-olaf`_ The OreSat Linux App Framework. Framework for all OreSat Linux applications.
  Built ontop of Python's CANopen library.
- `oresat-kicad`_ Common KiCAD library for all OreSat cards.

C3 Card
-------

Command, Control, Commication card. The main flight card.

- `oresat-c3`_ Hardware design for the C3 card.
- `oresat-c3-software`_ The main C3 OLAF-based application.
- `oresat-ax5043-driver`_ The AX5043 radio driver.
- `oresat-c3-watchdog`_ The watchdog app for the C3 software.

DxWiFi Card
------------

A card with a camera and antenna for sending live video of Earth over long
distance WiFi. This is a part of the OreSat Live payload mission.

- `oresat-dxwifi-hardware`_ Hardware design for the OreSat Live card.
- `oresat-dxwifi-software`_  The main DxWiFi OLAF-based application.
- `oresat-live-software`_  HGS software.
- `oresat-libdxwifi`_  Library for OreSat's 2.4GHz WiFi transmission system.

CFC (Cirrus Flux Camera) Card
------------------------------

Short wave infrared camera to map cirrus clouds. Another payload for OreSat.

- `oresat-cfc-hardware`_ Hardware design for the CFC cards.
- `oresat-cfc-software`_ The CFC OLAF-based application.
- `oresat-prucam-pirt1280`_ A kernel module for interfacing to PIRT1280 camera with PRUs.

GPS Card
---------

SDR / Hardware GPS receiver to calculate the location of satellite.

- `oresat-gps-hardware`_ Hardware design for the GPS card.
- `oresat-gps-software`_ The GPS OLAF-based application.

Star Tracker Card
------------------

Camera system that takes images of stars and uses the pattern of the stars let
to figure out which way the satellite is pointing.

- `oresat-star-tracker`_ Hardware design for the Star Tracker card.
- `oresat-star-tracker-software`_ The Star Tracker OLAF-based application.
- `oresat-prucam-ar013x`_ A kernel module for interfacing to AR013x camera with PRUs.

.. _oresat-ax5043-driver: https://github.com/oresat/oresat-ax5043-driver
.. _oresat-c3: https://github.com/oresat/oresat
.. _oresat-c3-software: https://github.com/oresat/oresat-c3-software
.. _oresat-c3-watchdog: https://github.com/oresat/oresat-c3-watchdog
.. _oresat-cfc-hardware: https://github.com/oresat/oresat-cfc-hardware
.. _oresat-cfc-software: https://github.com/oresat/oresat-cfc-software
.. _oresat-dxwifi-hardware: https://github.com/oresat/oresat-dxwifi-hardware
.. _oresat-dxwifi-software: https://github.com/oresat/oresat-dxwifi-software
.. _oresat-configs: https://github.com/oresat/oresat-configs
.. _oresat-gps-hardware: https://github.com/oresat/oresat-gps-hardware
.. _oresat-gps-software: https://github.com/oresat/oresat-gps-software
.. _oresat-kicad: https://github.com/oresat/oresat-kicad
.. _oresat-libdxwifi: https://github.com/oresat/oresat-libdxwifi
.. _oresat-linux: https://github.com/oresat/oresat-linux
.. _oresat-live-software: https://github.com/oresat/oresat-live-software
.. _oresat-olaf: https://github.com/oresat/oresat-olaf
.. _oresat-prucam-ar013x: https://github.com/oresat/oresat-prucam-ar013x
.. _oresat-prucam-pirt1280: https://github.com/oresat/oresat-prucam-pirt1280
.. _oresat-star-tracker: https://github.com/oresat/oresat-star-tracker
.. _oresat-star-tracker-software: https://github.com/oresat/oresat-star-tracker-software
