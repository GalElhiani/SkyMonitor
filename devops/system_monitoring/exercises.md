/*******************************************************************/

ex1: Use journalctl to show every boot your system has ever made.
Show the full information from one of the boots.

use the command
journalctl --list--boots

instance of one boot:
-18 b9d71da59b134b9695295f2cc180a379 Thu 2026-05-28 14:43:27 UTC—Thu 2026-05-28 14:56:27 UTC



/*******************************************************************/

ex2: Show all logs written from the beginning of the day until now.

use the command journalctl -S today

-S flag stands for since

i saved the logs in a file called ex2_logs.md

/*******************************************************************/

ex3: Pick a process and show all logs written by it.

use the command:
journalctl _PID={pid}

and use top to find a process

journalctl _PID=1566

i saved the logs in a file called ex3_logs.md

/*******************************************************************/

ex4: Write a Bash script that logs every successful run to the /var/log/syslog file.

answer is in ex4.sh

/*******************************************************************/

ex5: Edit your Bash script from the previous exercise to have bad syntax. Use strace to find the exact time of the error.

ex5.sh purposely broken file (syntax error)

i ran strace -t ./ex5.sh and found the exact time of the error:

15:35:48 rt_sigprocmask(SIG_SETMASK, [], ./ex5.sh: line 5: 7: command not found
NULL, 8) = 0

/*******************************************************************/

ex6: Use nmon to observe the top processes and CPU usage.
run nmon command in bash and then press c for cpu


/*******************************************************************/

ex7: Open a different terminal and run the following command: for i in 1 2 3 4; do while :
do :; done & done.
Explain what you see in the nmon terminal.
Fix it.

we see that the code creates an infinite loop running on the background.

in order to fix it we can need to first terminate the background looping process using kill $(jobs -p) 

/*******************************************************************/

ex8: Do the last exercise again using gnome-system-monitor.

running gnome-system-monitor
then run the code that was provided in the exercise in a different terminal
we can see the PID's of the processes of the infinite loop and simply right clicking on them and choose "kill"


