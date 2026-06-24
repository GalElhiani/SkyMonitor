/*******************************************************************/
ex1:

use the command
journalctl --list--boots

instance of one boot:
-18 b9d71da59b134b9695295f2cc180a379 Thu 2026-05-28 14:43:27 UTC—Thu 2026-05-28 14:56:27 UTC



/*******************************************************************/

ex2:

use the command journalctl -S today

-S flag stands for since

i saved the logs in a file called ex2_logs.md

/*******************************************************************/

ex3:

use the command:
journalctl _PID={pid}

and use top to find a process

journalctl _PID=1566

i saved the logs in a file called ex3_logs.md

/*******************************************************************/

ex4:

answer is in ex4.sh

/*******************************************************************/

ex5:

ex5.sh purposely broken file (syntax error)

i ran strace -t ./ex5.sh and found the exact time of the error:

15:35:48 rt_sigprocmask(SIG_SETMASK, [], ./ex5.sh: line 5: 7: command not found
NULL, 8) = 0

/*******************************************************************/

ex6:
run nmon command in bash and then press c for cpu


/*******************************************************************/

ex7:

we see that the code creates an infinite loop running on the background.

in order to fix it we can need to first terminate the background looping process using kill $(jobs -p) 

/*******************************************************************/

ex8:

running gnome-system-monitor
then run the code that was provided in the exercise in a different terminal
we can see the PID's of the processes of the infinite loop and simply right clicking on them and choose "kill"


