# Setup the Development Environment

## Getting Started
1. Run the `clone_repos.sh` script. Execute the script by providing either "ssh" or "https" as an argument. 
This will determine which protocol to use when cloning the repositories:

For SSH:
```
./clone_repos.sh ssh
```
For HTTPS:
```
./clone_repos.sh https
```

## A Closer look at the Dev environment Vagrantfile

1. **Vagrant configuration version**: The line `Vagrant.configure("2")` sets the configuration version. 
You should not change this value unless you know what you're doing, as it ensures compatibility with Vagrant.
2. **Box configuration**: The line `config.vm.box = "ubuntu/focal64"` sets the base box for the virtual machine. 
In this case, it is using Ubuntu 20.04 (Focal Fossa) 64-bit. You can find more boxes at https://vagrantcloud.com/search.
3. **Synced folders**: The following lines configure shared folders between the host and guest machines
```
config.vm.synced_folder "oresat-olaf/", "/vagrant"
config.vm.synced_folder "oresat-c3/", "/vagrant"
config.vm.synced_folder "yamcs/", "/vagrant"
```
These lines map the "oresat-olaf", "oresat-c3", and "yamcs" folders on the host machine to the "/vagrant" folder on the guest machine.
4. Provisioning: The Vagrantfile includes a shell provisioner that runs a series of commands on the guest machine
after it starts. In this case, the script updates the package lists, installs Python 3 Pip, and installs the extra
Linux modules for the current kernel version
```
config.vm.provision "shell", inline: <<-SHELL
  sudo apt update
  sudo apt install python3-pip
  sudo apt-get install -y linux-modules-extra-$(uname -r)
SHELL
```