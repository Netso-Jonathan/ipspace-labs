# ipSpace Exercices 1 - Build your own network automation lab
## Lab description
### Network device virtualisation
I'm using GNS3 2.1.12 to virtualize all my network devices.
GS3 server is running on two physical servers but for this first lab, one is enough :-).
The main host server is running Centos7 and I install GNS3 with pip (yes I like trouble :-), I though it was a good opportunity to learn centos at the same time :-). 

### Ansible control station
I've a Ubuntu 16.04 VM on my PC using Hyper-V(yes I like trouble :-)). The VM is in a private hyper-v network with a static IP address and it's nated with my Laptop IP address when it's need to reach the Device is my LAB. The setup allow me to reach my lab from the VM from everywhere (When I'm connecter remote to my network via openvpn)

I've also installed netbox on this VM for future use (I hope to get some time to play with Netbox)

I've also share a directory with SMB that allow my to map the working directory on ubuntu with my windows laptop so I can edit all my files on my windows using VSC. 

### Network Topology
I've started with a Basic 3-tier architecture  with one core-switch (C1-CAMAS01-CSW01), 2 Distribution switch (C1-CAMAS01-DSW01&2) with 6 access switches (C1-CAMAS01-ASW01-6). Each distribution has 3 access switch connected and only one uplink two the core. 
Each switch has two physical uplink to one Distribution switch using LACP

Network os for the Distribution and Core will are vEOS and Access switches are vIOS-L2

All switch use the Vlan 6 as management vlan. The core switch is use to route the Vlan 6 to my Homelab network. 

### Goals
One of the main goal for this cours will be to create a ZTP environment to migrate Cisco access switch to Juniper EX switches (yes i changed my mind after the ZTP presention from Patrick Ogenstad :-) ).

### Playbook and scripts in this directory
I've created a python script (gns3_inv.py) that fetch the consol port information from GNS3 server via API call and build an Ansible host inventory file using a jinja2 template with the consol port informationj and assign an ansible_host ip. 

After I have the ansible-playbook play_basic_mgm_config.yml that use telnet and configure the basic management configuration that will allow ansible to connect via SSH.  
