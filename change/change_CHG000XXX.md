# Change CHG000XXX - Internet upgrade at Isabey
### 1 - verification before change
impact: none  

__spab-doris-mdf-wd01__  
```

!verification of the ipsec tunnel and default route  
show security ipsec security-associations  
show route 0.0.0.0/0  

! ping ipsec peer private ip  
ping 192.168.161.64  
ping 192.168.161.42  

! Check Zscaler status  
show services rpm history-results | match zscaler  
ping 10.126.0.10 source 10.126.0.9  
ping 10.126.0.14 source 10.126.0.13  
```

### 2 - Add new ip address as a secondary IP for internet interface.
impact: none  

__spab-doris-mdf-wd01__  
```
set interface ge-0/0/4.0 familiy inet *new-ip*  
```
__doris-mdf-es01__  
```
config terminal  
 interface Gi1/0/44  
  description New internet access  
  switchport access vlan 998  
  speed 100  
  duplex full  
  no ip access-group user-port-block in  
```
__spab-doris-mdf-wd01__  
```

! ping public IP address of IPSec Peer from the new IP  
ping {'pub': None, 'st0.52': '192.168.161.64'}  
```

### 3 - New task
impact: I don't know  


