# Redmine Server.
![](usr/share/redmine/public/themes/susdev/images/sd_logo_sm.png)

Suspect Devices maintains a git backup server for repositories hosted by github and bitbucket. 
This server was running trac to track issues and work. 
This site replaces trac with Redmine to evaluate its usefullness.

* Backup repositories hosted elsewhere.
* Consolidate work into active/inactive projects
* Track issues (ticketing)
* Document server setup.

# Server configuration
This server is running on a Ubuntu 18.04 container. 

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
Add git command do configuration

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
### Adding SSL to the configuration 
Debugging css is easier with firefox and its handy tools however to authenticate using your credentials requires ssl which is high on the list of things to do early so here it is.

*[etc/apache2/sites-enabled/redmine.conf](etc/apache2/sites-enabled/redmine.conf)

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
### Creating scripts to do the updates 
both bitbucket and git have apis that allow you to list the repositories for each user without needing to authenticat (and expose your credentials). 

```
apt-get install python-github
apt-get install python-bitbucket

su -l www-data
python
```
The scripts I arrived at work but could certainly be refined. 
I should probably just use a list for each repo regardless of the site and maintain that as part of this repo. Bitbucket does not allow you to list all of the private repos so I just went with a simple list.

* [clone-repos.py](var/www/bin/clone-repos.py)
* [update-repos.py](var/www/bin/update-repos.py)

## Things that are done in redmine.
* Set passwords and add admin users.
* Add projects and add repositories to them. 
* Remove repo browsing from anonymous / non project users
* Activate themes
