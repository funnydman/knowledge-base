
### create new user with sudo privileges 

```bash 
sudo adduser username
```
Grant privilages.
```bash
sudo usermod -aG sudo username
```
Use the su command to switch to the new user account.

```bash
su - username
```

https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04
https://www.digitalocean.com/community/tutorials/automating-initial-server-setup-with-ubuntu-18-04
