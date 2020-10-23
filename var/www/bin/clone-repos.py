#!/usr/bin/python
from github import Github
import json
import subprocess
import urllib2

username = "feurig"
repodir = "/var/www/git"
#g = Github()
#user = g.get_user(username)
#for repo in user.get_repos():
#    url="git@github.com:"+username+"/"+repo.name+".git"
#    print "Cloning :",url
#    subprocess.call(["/usr/bin/git", "clone", "--mirror", url], cwd=repodir)

#response = urllib2.urlopen("https://api.bitbucket.org/2.0/repositories/"+username+"?pagelen=100")
#data=json.loads(response.read())['values']
#for record in data:
#    url="git@bitbucket.org:"+username+"/"+record['slug']+".git"
#    print "Cloning :",url
#    subprocess.call(["/usr/bin/git", "clone", "--mirror", url], cwd=repodir)
#git clone git@bitbucket.org:feurig/missinglink-hardware.git
repos=['feurig/ems-light','feurig/musicbox','feurig/straight-from-hell.com',
       'feurig/trashterm','feurig/missinglink-hardware','feurig/bnc-proprietary',
       'feurig/ems-firmware','feurig/ems-golang','feurig/ems-framework','joedumoulin/sesh']
for repo in repos:
    url="git@bitbucket.org:"+repo+".git"
    print "Cloning :",url
    subprocess.call(["/usr/bin/git", "clone", "--mirror", url], cwd=repodir)



