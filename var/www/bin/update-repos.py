#!/usr/bin/python
from github import Github
import subprocess
username = "feurig"
repodir = "/var/www/git/"
g = Github()
user = g.get_user(username)
for repo in user.get_repos():
    d=repodir+repo.name+".git"
    print "updating :",d

repos=['feurig/ems-light','feurig/musicbox','feurig/straight-from-hell.com',
       'feurig/trashterm','feurig/missinglink-hardware','feurig/bnc-proprietary',
       'feurig/ems-firmware','feurig/ems-golang','feurig/ems-framework','joedumoulin/sesh']
for repo in repos:
    d=repodir+repo.split('/')[1]+".git"
    print "updating :",d
    subprocess.call(["/usr/bin/git", "fetch", "-q", "--all", "-p"], cwd=d)



