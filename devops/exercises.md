ex1:
use ip link to show mac address, it will be link\ether ...
use ip address to show ip addresses
use ip route to show subnet for each networking interface.

/*******************************************************************************/

ex2:
i'll use traceroute google.com
it took 8 hops
the ip address belongs to the default local gateway

/*******************************************************************************/

ex3:
sudo ss -tulpn for all open ports
sudo netstat -tulpn
sudo nmap -sTU -O localhost
Netid    State     Recv-Q    Send-Q                            Local Address:Port        Peer Address:Port    Process                                         
udp      UNCONN    0         0                                       0.0.0.0:5353             0.0.0.0:*        users:(("avahi-daemon",pid=26717,fd=12))       
udp      UNCONN    0         0                                 127.0.0.53%lo:53               0.0.0.0:*        users:(("systemd-resolve",pid=54969,fd=13))    
udp      UNCONN    0         0                           192.168.64.2%enp0s1:68               0.0.0.0:*        users:(("systemd-network",pid=54967,fd=18))    
udp      UNCONN    0         0                                       0.0.0.0:37487            0.0.0.0:*        users:(("avahi-daemon",pid=26717,fd=14))       
udp      UNCONN    0         0                                          [::]:5353                [::]:*        users:(("avahi-daemon",pid=26717,fd=13))       
udp      UNCONN    0         0                                          [::]:39002               [::]:*        users:(("avahi-daemon",pid=26717,fd=15))       
udp      UNCONN    0         0            [fe80::78e6:46ff:fe77:bc66]%enp0s1:546                 [::]:*        users:(("systemd-network",pid=54967,fd=21))    
tcp      LISTEN    0         128                                     0.0.0.0:22               0.0.0.0:*        users:(("sshd",pid=54930,fd=3))                
tcp      LISTEN    0         128                                   127.0.0.1:631              0.0.0.0:*        users:(("cupsd",pid=75235,fd=7))               
tcp      LISTEN    0         4096                              127.0.0.53%lo:53               0.0.0.0:*        users:(("systemd-resolve",pid=54969,fd=14))    
tcp      LISTEN    0         128                                        [::]:22                  [::]:*        users:(("sshd",pid=54930,fd=4))                
tcp      LISTEN    0         128                                       [::1]:631                 [::]:*        users:(("cupsd",pid=75235,fd=6))  

/*******************************************************************************/

ex4:
tcp      LISTEN    0         128                                     0.0.0.0:22               0.0.0.0:*        users:(("sshd",pid=54930,fd=3)) 
tcp      LISTEN    0         128                                        [::]:22                  [::]:*        users:(("sshd",pid=54930,fd=4))                

/*******************************************************************************/
ex5:
1)
in order to check arp cache ill use ip neigh command
REACHABLE = destination is valid and recently confirmed
STALE = connection is old but valid, will re-verify in the next transmission
FAILURE = the hardware address couldnt be resolved

2)
to clear ARP cache ill use sudo ip -s -s neigh flush all

3) ip neigh

4) within its life time the entry refreshes with every use

/*******************************************************************************/

CISCO EXERCISES:

ex4:
after using ping 192.168.1.255 to broadcast PC2 got the transmission but PC3 which is
connected to vlan didnt get it.

/*******************************************************************************/

ex5:
the packet didnt arrive because PC3 is connected to VLAN2

/*******************************************************************************/

ex6:
in order to reconfigure the network to get transfer the ICMP we need to switch the
switch which is a Layer 2 device (its forbidden from moving traffic across a vlan boundary)
we'll use a router instead and configure the switch to be a trunk. and then configure the default gateway
of both pc2 and pc3

/*******************************************************************************/
 
 WIRESHARK EXERCISES:
 
 ex1:
 the mac address is: 7a:e6:46:77:bc:66

/*******************************************************************************/

ex2:

the ttl value of the packets:
request = 64
reply = 116

/*******************************************************************************/
ex3:
the steps involved are:

src[192.168.64.2] -> dst[34.107.221.82] [SYN] ports: 43590 -> 80

src[34.107.221.82] -> dst[192.168.64.2] [SYN, ACK] ports: 80 -> 43590

src[192.168.64.2] -> dst[34.107.221.82] [ACK] ports: 43590 -> 80

seq=0



/*******************************************************************************/

ex4:
start download and capture
stop when download is finished
filter tcp
find tcp packet with relative big length
click follow tcp stream
size is calculateable by counting length of packets
statistics -> conversations -> TCP-5 search for the size of the file
size of the downloaded file is 60kb

