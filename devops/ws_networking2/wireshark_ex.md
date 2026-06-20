/************************************************************/
WIRESHARK EXERCISES:
/************************************************************/
ex1:
go to wireshark
filter dns
find query response of visited sites
we can use dns.qry.name contains "example" to easily filter
go to packet information and scroll to "Answers"
find the address:

bing: 199.203.60.211

linkedin: 172.64.146.215

twitter: 172.66.0.227

DNS: 10.100.102.1

/************************************************************/

ex2:

reply code: No such name (3)

yes the DNS replies.

/************************************************************/

ex3:
filter for tls
go for packet info and expand TLSv1.3 Record Layer: Handshake Protocol: Client Hello

Version: TLS 1.0 (0x0301)

Cipher Suite: TLS_AES_256_GCM_SHA384 (0x1302)

for using paypal.com there wasnt a certificate exchange visible.
