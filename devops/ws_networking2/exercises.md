EXERCISES:

ex1:

dig google.com - 127.0.0.53

nslookup google.com

host google.com
/***********************************************************************/

ex2:

connect to lab partner using ssh command
then:
cat /etc/hosts

and after recieving a list of hosts we can use the identifying
name to ping someone instead of ip


/***********************************************************************/

ex3:
sudo nano /etc/hosts
change entry name
ping new host
it works because its vs the local DNS

/***********************************************************************/

ex4:

sudo nano /etc/hosts
remove the friend's entry

/***********************************************************************/

ex5:

a)
galelhiani@galelhiani:~/Desktop/git/devops/ws_networking2$ nslookup youtube.com
Server:		127.0.0.53
Address:	127.0.0.5
Non-authoritative answer:
Name:	youtube.com
Address: 142.250.75.206
Name:	youtube.com
Address: 2a00:1450:4028:806::200e



b)
galelhiani@galelhiani:~/Desktop/git/devops/ws_networking2$ dig youtube.com NS


; <<>> DiG 9.18.39-0ubuntu0.22.04.4-Ubuntu <<>> youtube.com NS
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 50350
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;youtube.com.			IN	NS

;; ANSWER SECTION:
youtube.com.		4502	IN	NS	ns1.google.com.
youtube.com.		4502	IN	NS	ns3.google.com.
youtube.com.		4502	IN	NS	ns2.google.com.
youtube.com.		4502	IN	NS	ns4.google.com.

;; Query time: 67 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Thu Jun 18 15:09:24 UTC 2026
;; MSG SIZE  rcvd: 119

/***********************************************************************/

ex6:

ill use dig youtube.com +trace for iterative requests using dig.






