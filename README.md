# Redmine Server.
[https://github.com/feurig/redmine-configuration/blob/main/README.md](https://github.com/feurig/redmine-configuration/blob/main/README.md)

![](https://github.com/feurig/redmine-configuration/blob/main/usr/share/redmine/public/themes/susdev/images/sd_logo_sm.png?raw=true)

Suspect Devices maintains a git backup server for repositories hosted by github and bitbucket. This site uses Redmine to track issues and work. 

### Tasks
* Backup repositories hosted elsewhere.
* Consolidate work into active/inactive projects
* Track issues (ticketing)
* Document server setup.

# Server configuration
This server is running on a Ubuntu 18.04 container because redmine requires a version of Ruby that is behind the new LTS (20.04). We will revisit this next spring.

```
apt-get install postgresql
apt-get install apache2 libapache2-mod-passenger
apt-get install redmine-pgsql
apt-get install redmine
cp /usr/share/doc/redmine/examples/apache2-passenger-host.conf /etc/apache2/sites-available/redmine.conf
nano /etc/apache2/sites-available/redmine.conf
a2enmod passenger
a2ensite redmine.conf
a2dissite 000-default
service apache2 reload
update.sh
```
Adding git functionality...

```
apt-get install git
```
Add git command to configuration

```
cp /usr/share/redmine/config/configuration.yml.example /etc/redmine/default/configuration.yml
nano /etc/redmine/default/configuration.yml
... add git command here ...
  scm_git_command: git
...
service redmine restart
```
Create some space for mirrors.

```
mkdir /var/git
chown -R www-data:www-data /var/git/
```
The www-data user should have its keys added to bitbucket and github. (This user does not need write permission)

```
vipw
su - www-data
mkdir /var/www/.ssh
chown www-data:www-data /var/www
su - www-data
ssh-genkey

```
Rather than configuring a git hook for both github and bitbucket we will create scripts to populate and update the mirrors. 

```
vi /etc/cron.d/sync_git_repos
*/2 * * * * www-data /var/www/bin/update-repos.py
```
### Making redmine less ugly.
Redmine makes it fairly easy to theme using css to override its defaults.

```
cd /usr/share/redmine/public/themes/
ls
mkdir susdev
chown www-data susdev
mkdir susdev/stylesheets/
mkdir susdev/images
ls
cd susdev/images/
wget https://serverdocs.suspectdevices.com/serverdocs/chrome/site/sd_logo_sm.png
wget https://serverdocs.suspectdevices.com/serverdocs/chrome/site/sd_logo_sm.png --no-check-certificate
nano ../stylesheets/application.css 
ls
nano ../stylesheets/application.css 
chown -R www-data:www-data ../../susdev
```
[usr/share/redmine/public/themes/susdev/stylesheets/application.css](https://github.com/feurig/redmine-configuration/blob/main/usr/share/redmine/public/themes/susdev/stylesheets/application.css)
### Adding SSL to the site 

```
sudo bash
make-ssl-cert generate-default-snakeoil --force-overwrite 
cd /etc/apache2/
ls
a2enmod ssl
nano sites-enabled/redmine.conf 
apache2ctl configtest
apache2ctl restart
```
#### Getting a certificate from letsencrypt
the EFF provides a certificate and a program to set it up from letsencrypt

```
apt-get install certbot
```
Certbot expects to be able to verify that your server exists and can serve one of its files. The file needs to be accessable at http://\<servers.fqdn>/.well-known/acme-challenge/ the example below assumes the document root for redmine.

```
cd /usr/share/redmine/public
mkdir -p .well-known/acme-challenge/
echo hello> .well-known/acme-challenge/test
root@emile:/usr/share/redmine/public# chown -R www-data:www-data .well-known/
```
Once this is done you can run certbot manually. 

```
certbot certonly --manual
```
They are going to ask a bunch of questions and then ask you to create file on the server.
The script pauses and you will have to create the file in a different shell. 

```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Create a file containing just this data:

KncX49YdVo125HQZiI1qYbSZxIPIUPMmcJUg2thHHCs.yoObxAOItnb_LvbpT7eCOZwNmD_ROuCOAkQqFAoKSTc

And make it available on your web server at this URL:

http://git.suspectdevices.com/.well-known/acme-challenge/KncX49YdVo125HQZiI1qYbSZxIPIUPMmcJUg2thHHCs

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Press Enter to Continue
```
Create the file as instructed in a different terminal and make sure its accessable by apache.

```
echo KncX49YdVo125HQZiI1qYbSZxIPIUPMmcJUg2thHHCs.yoObxAOItnb_LvbpT7eCOZwNmD_ROuCOAkQqFAoKSTc>/usr/share/redmine/public/.well-known/acme-challenge/KncX49YdVo125HQZiI1qYbSZxIPIUPMmcJUg2thHHCs
chown www-data:www-data /usr/share/redmine/public/.well-known/acme-challenge/KncX49YdVo125HQZiI1qYbSZxIPIUPMmcJUg2thHHCs
```
If it's successful it will install the certificate and private key under /etc/letsencrypt/live/. Adjust your apache configuration. 

```
nano /etc/apache2/sites-enabled/redmine.conf
... replace the top portion of the original virtualhost config with the following ....
<VirtualHost *:80>
Redirect permanent "/" "https://git.suspectdevices.com/"
</VirtualHost> 

<VirtualHost *:443>

    ServerName git.suspectdevices.com
    SSLEngine on
    #SSLCertificateFile      /etc/ssl/certs/ssl-cert-snakeoil.pem
    #SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key
    SSLCertificateFile   /etc/letsencrypt/live/git.suspectdevices.com/fullchain.pem
    SSLCertificateKeyFile   /etc/letsencrypt/live/git.suspectdevices.com/privkey.pem

    # this is the passenger config
    
... and save it ....
apache2ctl configtest
apache2ctl restart
```
* [etc/apache2/sites-enabled/redmine.conf](https://github.com/feurig/redmine-configuration/blob/main/etc/apache2/sites-enabled/redmine.conf)


### Creating scripts clone and update the repositories
both bitbucket and git have apis that allow you to list the repositories for each user without needing to authenticate (and expose your credentials). There are limitations but they are worth exploring. 

```
apt-get install python-github
apt-get install python-bitbucket

su -l www-data
python
```
The scripts I arrived at work but could certainly be refined. 
I should probably just use a list for each repo regardless of the site and maintain that as part of this repo. Bitbucket does not allow you to list all of the private repos so I just went with a simple list.

* [clone-repos.py](https://github.com/feurig/redmine-configuration/blob/main/var/www/bin/clone-repos.py)
* [update-repos.py](https://github.com/feurig/redmine-configuration/blob/main/var/www/bin/update-repos.py)

### Set up email 
Debians postfix installer makes it very easy to install postfix configured as a null client. When installing select Satelite and provide your domain name and relay host.

```
apt-get install postfix
```
## Things that are done in redmine.
* Set passwords and add admin users.
* Add projects and add repositories to them. 
* Remove repo browsing from anonymous / non project users
* Activate themes
* USE IT.

