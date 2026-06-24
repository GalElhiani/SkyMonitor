/**********************************************/
ex1:

install samba:

sudo apt install samba

then enamble the service:

systemctl enable --now smbd

change configuration of samba to enable service:

sudo nano /etc/samba/smb.conf 

[sambashare]
   path = /home/galelhiani/Desktop/shared_folder
   read only = No

create a for a user:

sudo smbpasswd -a galelhiani

restart the service:

sudo systemctl restart smbd


/**********************************************/
