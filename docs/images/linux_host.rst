Connecting from a Linux host
============================

SSH (with shared internet)
--------------------------

.. note:: This guide only goes over Linux systems using `NetworkManager`_ or
   `systemd-networkd`_

1. Connect the OreSat Linux card to the host machine using a USB cable.

2. In a terminal, run the following command and wait for an interface starting with ``enp`` or ``enx`` to appear.

The number following the ``enx`` or ``enp`` is the MAC address of the target's interface. Note that it can change if the target is rebooted.

  .. code-block:: text

    $ watch -n1 ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
      ...
    2: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
      ...
    3: enp0s20f0u3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UNKNOWN group default qlen 1000
        link/ether 60:64:05:f9:0d:06 brd ff:ff:ff:ff:ff:ff
    4: enp0s20f0u3i2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
        link/ether 60:64:05:f9:0d:08 brd ff:ff:ff:ff:ff:ff

If there are multiple interfaces whose name start with ``enp``
the target is usually connected to the ``enp*i2`` interface (as shown above). If the interface name starts with ``enx``
interface, the target is usually connected to the interface with a higher number following the ``enx``.

**Only if the Linux host uses** `NetworkManager`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Install ``dnsmasq`` on your system.

2. In another terminal, setup a DHCP server. **Replace** ``enp0s20f0u3i2`` in the following command with the name found in previous step on your host.

.. note:: This guide use the `nmcli` command as the NetworkManager GUI is limited.

.. code-block:: text

    nmcli connection add type ethernet ifname enp0s20f0u3i2 ipv4.method shared con-name oresat-card

.. note:: This interface name can change if the target reboots. To change the intrerface name use the following.

      ``nmcli connection modify oresat-card connection.interface_name [interface name]``
  
    You can rely on tab completion to discover the interface name.

**Only if the Linux host uses** `systemd-networkd`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Setup the DHCP server, with your favorite IDE or text editor create a file with the name ``20-oresat-card.network``  in the ``/etc/systemd/network`` directory. Add the following text to the file. **Replace** enp*i2 as needed.
   
.. code-block:: text
  [Match]
  Name=enp*i2

  [Network]
  Address=10.42.1.1/24
  DHCPServer=true
  IPMasquerade=ipv4
  MulticastDNS=yes

  [DHCPServer]
  EmitDNS=yes
  DNS=9.9.9.9

2. Restart systemd-networkd

.. code-block:: text

  sudo systemctl restart systemd-networkd

SSH using an IP address
^^^^^^^^^^^^^^^^^^^^^^^

1. Go back to the terminal with ``watch ip a`` command running at wait for the address to be set. Make a note of the address and IPv4 address space; it should be something like ``10.42.1.1/24``. 

.. code-block:: text

  $ watch -n1 ip a
  1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    ...
  2: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    ...
  3: enp0s20f0u3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UNKNOWN group default qlen 1000
    link/ether 60:64:05:f9:0d:06 brd ff:ff:ff:ff:ff:ff
  4: enp0s20f0u3i2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 60:64:05:f9:0d:08 brd ff:ff:ff:ff:ff:ff
    inet 10.42.1.1/24 scope host lo
      valid_lft forever preferred_lft forever
    net6 fe80::cbcb:674d:2adf/64 scope link noprefixroute
      valid_lft forever preferred_lft forever

2. Install ``nmap``_ on the Linux host.

3. Run nmap to discover the card's IP address. **Replace** ``10.42.1.1/24`` in the following command **with** the IPv4 address space found in the previous step. Alternatively, ``[linux_host_hostname].local/24`` (e.g. ``thnkpd.local/24``) will work as well on most distros.

.. code-block:: text

  $ nmap -sn 10.42.1.1/24
  Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-13 22:07 UTC
  Nmap scan report for 10.42.1.1
  Host is up (0.00079s latency).
  Nmap scan report for 10.42.1.120
  Host is up (0.0035s latency).
  Nmap done: 256 IP addresses (2 hosts up) scanned in 2.63 seconds

That should print out two IP addresses (one is the Linux host and one is the OreSat card) 

The terminal with ``watch ip a`` running is no longer needed.

4. SSH onto the card. Password is ``temppwd``. **Replace** ``10.42.1.120`` in the following command with other address that nmap found

.. code-block:: text

  ssh debian@10.42.1.120

SSH using multicast DNS (mDNS) domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: mDNS is not configured by default on the target. To configure it add ``MulticastDNS=yes`` to ``\etc\systemd\network\10-usb0.network`` and restart ``systemd-networkd``.

1. SSH onto the card. Password is ``temppwd``. **Replace** ``oresat-dev`` in the following command with other hostname
    
.. code-block:: text

  ssh debian@oresat-dev.local

For convenience, we can add ``oresat-dev.local`` to ``$HOME/.ssh/config``.

.. code-block:: text

  Host oresat-dev.local
    HostName oresat-dev.local
    User debian

This gives the slight benefit of using tab completion when using ``ssh``.

Mounting a remote directory with SSHFS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
Mounting the target to the host filesystem makes it easy to transfer files, search the target's file tree (try fzf_, ripgrep_, and zoxide_), and remotely develop and deploy code to the target. To mount the target's filesystem first install `sshfs`_ to your Linux host machine, then run the following command.

.. codeblock:: text

  sshfs -o allow_other,default_permissions debian@oresat-dev.local:/ /mnt

        

Verify the target has an internet connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

  $ ping www.google.com
  PING www.google.com (172.217.14.228) 56(84) bytes of data.
  64 bytes from sea30s02-in-f4.1e100.net (172.217.14.228): icmp_seq=1 ttl=117 time=41.6 ms
  64 bytes from sea30s02-in-f4.1e100.net (172.217.14.228): icmp_seq=2 ttl=117 time=29.1 ms

.. _systemd-networkd: https://wiki.archlinux.org/index.php/Systemd-networkd
.. _NetworkManager: https://networkmanager.dev/
.. _nmap: https://wiki.archlinux.org/title/Nmap
.. _fzf: https://www.mankier.com/1/fzf
.. _ripgrep: https://manpages.debian.org/testing/ripgrep/rg.1.en.html
.. _zoxide: https://packages.debian.org/stable/admin/zoxide


Serial
------

1. Install ``picocom`` to the Linux host.

2. Connect a USB to FTDI chip on the card debug board and to you system

.. code-block:: text

  picocom -b 115200 /dev/serial/by-id/usb-BeagleBoard*

.. Note:: To exit picocom enter control-A-X
