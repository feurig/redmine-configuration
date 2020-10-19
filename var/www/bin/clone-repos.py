#!/usr/bin/python
from github import Github
import subprocess
username = "feurig"
repodir = "/var/www/git"
g = Github()
user = g.get_user(username)
for repo in user.get_repos():
    url="git@github.com:"+username+"/"+repo.name+".git"
    print "Cloning :",url
    subprocess.call(["/usr/bin/git", "clone", "--mirror", url], cwd=repodir)
