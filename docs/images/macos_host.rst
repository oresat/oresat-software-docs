Connecting from a MacOS host
============================

SSH (with shared internet)
--------------------------

- Connect the OreSat Linux card to host using a USB cable

- Go to ``System Settings => Network`` and wait for the BeagleBone connection to come up
- Go to ``System Settings => General => Sharing``, click on the ``i`` next to ``Internet
  Sharing``, check the checkbox next to ``BeagleBone``, and then check the checkbox for
  ``Internet Sharing``

- Open a terminal and watch ifconfig
  
  .. code-block::
    
    $ watch -n 1 ifconfig
    lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
      ...
    en0: flags=8822<BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
      ...
    en7: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1486
      ether 60:64:05:f9:0d:06 
      nd6 options=201<PERFORMNUD,DAD>
      media: autoselect
      status: active
    bridge100: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1486
      options=3<RXCSUM,TXCSUM>
      ether ca:2a:14:44:1d:64 
      inet 192.168.2.1 netmask 0xffffff00 broadcast 192.168.2.255
      inet6 fe80::c82a:14ff:fe44:1d64%bridge100 prefixlen 64 scopeid 0xe 
      Configuration:
        id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
        maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
        root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
        ipfilter disabled flags 0x2
      member: en7 flags=3<LEARNING,DISCOVER>
              ifmaxaddr 0 port 13 priority 0 path cost 0
      nd6 options=201<PERFORMNUD,DAD>
      media: autoselect
      status: active

- Once the bridge show up note the IP address and stop the watch (control-C).
  In the example ``ifconfig`` above, the address for the bridge would be
  ``192.168.2.1``.

- Go back to ``System Settings => Network`` and edit ``BeagleBone`` and
  change it to ``Using DHCP with manual address`` and set the address to the
  address found from ifconfig. 

- SSH onto the card. Password is ``temppwd``. Replace ``oresat-dev`` in the
  following command with the image hostname as needed.

  .. code-block:: text

    $ ssh debian@oresat-dev.local

- Make sure shared internet is working

  .. code-block:: text

    $ ping www.google.com
    PING www.google.com (172.217.14.228) 56(84) bytes of data.
    64 bytes from sea30s02-in-f4.1e100.net (172.217.14.228): icmp_seq=1 ttl=117 time=41.6 ms
    64 bytes from sea30s02-in-f4.1e100.net (172.217.14.228): icmp_seq=2 ttl=117 time=29.1 ms

Serial
------

 - Install ``picocom``::

   $ brew install picocom

 - Connect a USB to FTDI chip on the card debug board and to you system::

   $ picocom -b 115200 /dev/serial/tty.usb*

- **Note:** To exit control-A-X
