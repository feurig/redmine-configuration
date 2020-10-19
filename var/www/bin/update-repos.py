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
    subprocess.call(["/usr/bin/git", "fetch", "-q", "--all", "-p"], cwd=d)
