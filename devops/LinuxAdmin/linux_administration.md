/*******************************************************/

ex1:
sudo adduser labuser1

for one liner:

sudo useradd labuser2 && echo "labuser2:0545424712$" | sudo chpasswd

sudo mkdir -p /home/labusers_home

sudo usermod -m -d /home/labusers_home/labuser1 labuser1
sudo usermod -m -d /home/labusers_home/labuser2 labuser2

/*******************************************************/

ex2:

a)
touch newfile.txt
ls -l
-rw-rw-r-- 1 galelhiani galelhiani     0 Jun 20 16:31 newfile.txt

chmod 551 newfile.txt
chmod u=rx,g=x,o=x newfile.txt

b)
umask 077

/*******************************************************/

ex3:

simply insert the command to a bash script

sudo ss -luntp

/*******************************************************/

ex4:

sudo mv activesockets.sh /usr/local/bin/
sudo chmod 755 /usr/local/bin/activesockets.sh

/*******************************************************/

ex5:

awk -F: '{print $1}' /etc/passwd | sort

/*******************************************************/

ex6:

sudo find / -name "uptime" 2>/dev/null

/*******************************************************/

ex7:

sudo find / 2>/dev/null | grep '\.c$'

/*******************************************************/

ex8:

sudo find / -type f -size +50M 2>/dev/null | xargs du -h --apparent-size | sort -h

/*******************************************************/

ex9:

ln text.txt hardlink.txt
changes in one of them will apply to the other

/*******************************************************/

ex10:
ln -s ..... <new directory>
changes will apply in both of the source directory
and the soft linked one

/*******************************************************/

ex12:

scp file.txt <target ip: target path> <local path>

/*******************************************************/

ex13:





