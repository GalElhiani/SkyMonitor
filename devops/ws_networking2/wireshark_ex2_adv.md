/*****************************************************/

WIRESHARK ADVANCED:

/*****************************************************/

ex1:

filter: tcp.flags.syn == 1 and tcp.flags.ack == 0
statistic -> conversation -> tcp:38
there were 38 tcp connections initiated

/*****************************************************/

ex2:

filter: tcp.flags.fin == 1
statistic -> conversation -> tcp:11
there were 11 connection terminations

/*****************************************************/

ex3:


filter: arp.isgratuitous == 1

there were 6 instances of Gratuitous arp messages sent.

/*****************************************************/

ex4:

10.2.0.76 was trying to find out the address of google play
and it took him 256.097 micro seconds to get a response.

/*****************************************************/

ex5:

fiter: tcp.len > 10000 (i tried 1000 and saw there were too many)

and then check the tcp segment len which is 10136

/*****************************************************/

ex6:

filter: udp
look at the bottom where it says Displayed: 8482

there were 8482 udp packets sent

