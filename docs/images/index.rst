Linux Images
============

All OreSat Linux images are hosted at https://images.oresat.org/

Images
------

**oresat-dev-*.img**

The dev image is the recommended development image. It has a bunch of dev tools
and general libraries installed. This image should work fine on all OreSat
Boards, a `BeagleBone Black`_, or a `PocketBeagle`_.

**oresat-<card>-*.img**

.. warning:: Flight images expect the hardware for their specific card, so the
   software on these images may not work on other hardware.

These are the flight images. They have all software and system configurations
required for that specific card.

Notes about all images
----------------------

- All img are compress with ``zstd``. To decompress them::

    $ zstd -d oresat-*.img.zst

- All images use Debian 11 (Bullseye) with the TI 5.10 kernel.

- All images have the user `debian` with password `temppwd`.

- On the **first** boot, the image will expand to fill the eMMC or SD card.

- Root login over ssh is disabled.

- All use `systemd-networkd`_ for networking.

- Has two USB IP Links just like BeagleBoard's images, but they use both us
  DHCP, the first one is for Windows and the second is for a \*nix based OS.
- eth0 is also set up for DHCP for `BeagleBone Black`_ ethernet jack.

- The hostname is set to the name of card it's for; e.g. ``oresat-dev``,
  ``oresat-star-tracker``, etc.

- mDNS (MulticatDNS) is setup with `systemd-networkd`_, so if the host has mDNS
  enable, cards with OreSat images can be resolved to ``hostname.local``; e.g.:
  ``oresat-gps.local``

- On the dev image only

  - Both the eMMC0 and the CAN1 device tree overlays are enabled.

- On flight images

  - The PocketBeagle device is overwritten with custom OreSat card device tree from 
    https://github.com/oresat/oresat-linux/tree/master/image_builder/device_trees

  - All OreSat software for the card is installed via Debian and/or Python packages

Connecting to card using a OreSat Image
---------------------------------------

.. toctree::
    :maxdepth: 2
    
    linux_host
    macos_host

Building Images
---------------

See https://github.com/oresat/oresat-linux/tree/master/image_builder

.. _BeagleBone Black: https://beagleboard.org/black/
.. _PocketBeagle: https://beagleboard.org/pocket
.. _systemd-networkd: https://wiki.archlinux.org/index.php/Systemd-networkd
