#!/usr/bin/python
"""-------------------------------------------------------------------------clone-repos.py
Make mirror copies of repos from github and bitbucket.
Author: D. Delmar Davis <don@suspectdevices.com>
Copyleft: (c) 2020 D. Delmar Davis <don@suspectdevices.com>
Liscense: mit
"""
#from github import Github
#import json
import subprocess
#import urllib2

username = "feurig"
repodir = "/var/www/git"

githubrepos=['feurig/arduino-core-105','feurig/Arduino_STM32_MIDI_project',
    'feurig/Cohen','feurig/ems-light','feurig/ems2','feurig/failandflail',
    'feurig/libmaple','feurig/libmaplemidi-cma','feurig/maple','feurig/maplebacon',
    'feurig/midimonster2012','feurig/pubcrawler','feurig/python-dialog',
    'feurig/redmine-configuration','feurig/rtmidi','feurig/Suspect-Devices-Open-Hardware',
    'feurig/wsgi-bitbucket-mirror',
]

bitbucketrepos=['feurig/ems-light','feurig/musicbox','feurig/straight-from-hell.com',
       'feurig/trashterm','feurig/missinglink-hardware','feurig/bnc-proprietary',
       'feurig/ems-firmware','feurig/ems-golang','feurig/ems-framework',
       'joedumoulin/sesh','suspectdevicesadmin/ansible']


for repo in githubrepos:
    url="git@github.com:"+repo+".git"
    print "Cloning :",url
    subprocess.call(["/usr/bin/git", "clone", "--mirror", url], cwd=repodir)

for repo in bitbucketrepos:
    url="git@bitbucket.org:"+repo+".git"
    print "Cloning :",url
    subprocess.call(["/usr/bin/git", "clone", "--mirror", url], cwd=repodir)

# used to create lists of repos
#response = urllib2.urlopen("https://api.bitbucket.org/2.0/repositories/"+username+"?pagelen=100")
#data=json.loads(response.read())['values']
#for record in data:
#    url="git@bitbucket.org:"+username+"/"+record['slug']+".git"
#    print "Cloning :",url
#    subprocess.call(["/usr/bin/git", "clone", "--mirror", url], cwd=repodir)
#git clone git@bitbucket.org:feurig/missinglink-hardware.git


#g = Github()
#user = g.get_user(username)
#for repo in user.get_repos():
#    print"'"+username+"/"+repo.name+"',"


