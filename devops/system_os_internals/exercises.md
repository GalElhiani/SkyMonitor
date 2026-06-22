/******************************************************/

ex1:

galelhiani@galelhiani:~/Desktop/git/devops/system_os_internals$ ps
    PID TTY          TIME CMD
  15302 pts/0    00:00:00 bash
  23507 pts/0    00:00:00 git
  23574 pts/0    00:00:00 ps
galelhiani@galelhiani:~/Desktop/git/devops/system_os_internals$ lsof -p 15302
lsof: WARNING: can't stat() tracefs file system /sys/kernel/debug/tracing
      Output information may be incomplete.
COMMAND   PID       USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
bash    15302 galelhiani  cwd    DIR  253,0     4096  527444 /home/galelhiani/Desktop/git/devops/system_os_internals
bash    15302 galelhiani  rtd    DIR  253,0     4096       2 /
bash    15302 galelhiani  txt    REG  253,0  1399416 3408449 /usr/bin/bash
bash    15302 galelhiani  mem    REG  253,0  3048928 3408867 /usr/lib/locale/locale-archive
bash    15302 galelhiani  mem    REG  253,0  1661968 3428406 /usr/lib/aarch64-linux-gnu/libc.so.6
bash    15302 galelhiani  mem    REG  253,0   195784 3409574 /usr/lib/aarch64-linux-gnu/libtinfo.so.6.3
bash    15302 galelhiani  mem    REG  253,0   187776 3408324 /usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1
bash    15302 galelhiani  mem    REG  253,0    27004 3436891 /usr/lib/aarch64-linux-gnu/gconv/gconv-modules.cache
bash    15302 galelhiani    0u   CHR  136,0      0t0       3 /dev/pts/0
bash    15302 galelhiani    1u   CHR  136,0      0t0       3 /dev/pts/0
bash    15302 galelhiani    2u   CHR  136,0      0t0       3 /dev/pts/0
bash    15302 galelhiani  255u   CHR  136,0      0t0       3 /dev/pts/0
galelhiani@galelhiani:~/Desktop/git/devops/system_os_internals$ 

/******************************************************/

ex2:

free -h

               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.0Gi       1.0Gi       383Mi       3.8Gi       4.5Gi
Swap:          4.0Gi          0B       4.0Gi

/******************************************************/

ex3:

strace uname -a

write(1, "Linux galelhiani 5.15.0-181-gene"..., 115Linux galelhiani 5.15.0-181-generic #191-Ubuntu SMP Fri May 22 19:27:05 UTC 2026 aarch64 aarch64 aarch64 GNU/Linux

/******************************************************/

ex4:

ps
    PID TTY          TIME CMD
  37863 pts/0    00:00:00 bash
  39187 pts/0    00:00:00 ps

pstree 37863
bash───pstree



