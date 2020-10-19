exit
apt-get install postgresql
apt-get install redmine-pgsql
apt-get install redmine
apt-get install apache2 libapache2-mod-passenger
apt-get install redmine
apt-get install apache2 libapache2-mod-passenger
cp /usr/share/doc/redmine/examples/apache2-passenger-host.conf /etc/apache2/sites-available/redmine.conf
nano /etc/apache2/sites-available/redmine.conf
a2enmod passenger
a2ensite redmine.conf
a2dissite 000-default
service apache2 reload
update.sh
apt-get install git
mkdir /var/lib/redmine/repos/
chown -R www-data:www-data /var/lib/redmine/repos/
cd /var/lib/redmine/repos/
git clone https://github.com/feurig/ems2.git
ls -lsa
chown -R www-data:www-data /var/lib/redmine/repos/
cp /usr/share/redmine/config/configuration.yml.example /etc/redmine/default/configuration.yml
nano /etc/redmine/default/configuration.yml
service redmine restart
cd
cat .bash_history 
cat /root/.bash_history 
exit
sudo bash
cat .bash_history 
mkdir /var/git
sudo bash
mkdir /var/git
chown -R www-data:www-data /var/git/
su - www-data
vipw
su - www-data
mkdir /var/www/.ssh
chown www-data:www-data /var/www/.ssh
su - www-data
chown www-data:www-data /var/www
su - www-data
vi /etc/cron.d/sync_git_repos
crontab -l
reboot
sudo bash
crontab -l
crontab -l www-data
crontab -l -u www-data
cron
cron --help
cron -?D
cron -?
cron -h
cron help
ps -ef
tail /var/log/syslog
tail -f /var/log/syslog
su - www-data
sudo bash
find / -name plugins -print
find / -name Gemfile.local -print 2>/dev/null
gem "redmine_github_hook"
find / -name redmine -print 2>/dev/null
nano /etc/redmine/
nano /etc/redmine/default/configuration.yml 
nano /etc/redmine/d
sudo bash
find / -name *.css -print 2>/dev/null
/usr/share/redmine/public/stylesheets/application.css
nano /usr/share/redmine/public/stylesheets/application.css
service redmine restart
reboot
find / -name *.css -print 2>/dev/null
nano /usr/share/redmine/public/themes/README 
cd /usr/share/redmine/public/themes/
ls
mkdir susdev
chown www-data susdev
mkdir susdev/stylesheets/
mkdir susdev/images
ls
nano susdev/stylesheets/application.css
cd susdev/images/
ls
wget https://serverdocs.suspectdevices.com/serverdocs/chrome/site/sd_logo_sm.png
wget https://serverdocs.suspectdevices.com/serverdocs/chrome/site/sd_logo_sm.png --no-check-certificate
nano ../stylesheets/application.css 
ls
nano ../stylesheets/application.css 
chown -R www-data:www-data ../../susdev
ls
nano ../stylesheets/application.css 
tail /var/log/apache2/access.log 
tail -f /var/log/apache2/access.log 
tail -f /var/log/apache2/error.log
tail -f /var/log/redmine/default/production.log
nano ../stylesheets/application.css 
cd ..
mkdir favico
cd favico/
ls
wget https://blog.suspectdevices.com/blahg/wp-content/themes/sdtheme/favicon.ico --no-certificate-check
wget https://blog.suspectdevices.com/blahg/wp-content/themes/sdtheme/favicon.ico
wget https://blog.suspectdevices.com/blahg/wp-content/themes/sdtheme/favicon.ico --no-check-certificate
ls
mv ~feurig/favicon.ico .
ls
chown -R www-data:www-data ../../susdev
cd ../images/
mv ~feurig/susdev-site3-tiny.png .
nano ../stylesheets/application.css 
mv ~feurig/susdev-redmine.png .
nano ../stylesheets/application.css 
mv ~feurig/susdev-redmine.png .
nano ../stylesheets/application.css 
mv ~feurig/susdev-redmine.png .
nano ../stylesheets/application.css 
sudo bash
make-ssl-cert generate-default-snakeoil --force-overwrite 
cd /etc/apache2/
ls
a2enmod ssl
gzcat /usr/share/doc/apache2/README.Debian.gz 
gunzip -dc /usr/share/doc/apache2/README.Debian.gz 
nano apache2.conf 
nano sites-enabled/redmine.conf 
nano sites-available/default-ssl.conf 
nano sites-enabled/redmine.conf 
apache2ctl configtest
apache2ctl restart
cd /usr/share/redmine/public/themes/
cd susdev/
ls
nano stylesheets/application.css 
su - www-data
find / -name favicon.ico -print 2>/dev/null
cp /usr/share/redmine/public/themes/susdev/favico/favicon.ico /usr/share/redmine/public/favicon.ico
nano /etc/apache2/sites-enabled/redmine.conf 
cat /etc/apache2/sites-enabled/redmine.conf 
find / -name favicon.ico -print 2>/dev/null
sudo bash
apt-get update
apt-cache search PyGitHub
apt-get install python-github
su -l www-data
