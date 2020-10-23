#!/usr/bin/python
from github import Github
import subprocess
username = "feurig"
repodir = "/var/www/git/"

githubrepos=['feurig/arduino-core-105','feurig/Arduino_STM32_MIDI_project',
    'feurig/Cohen','feurig/ems-light','feurig/ems2','feurig/failandflail',
    'feurig/libmaple','feurig/libmaplemidi-cma','feurig/maple','feurig/maplebacon',
    'feurig/midimonster2012','feurig/pubcrawler','feurig/python-dialog',
    'feurig/redmine-configuration','feurig/rtmidi','feurig/Suspect-Devices-Open-Hardware',
    'feurig/wsgi-bitbucket-mirror',
]

bitbucketrepos=['feurig/ems-light','feurig/musicbox','feurig/straight-from-hell.com',
       'feurig/trashterm','feurig/missinglink-hardware','feurig/bnc-proprietary',
       'feurig/ems-firmware','feurig/ems-golang','feurig/ems-framework','joedumoulin/sesh']

repos=githubrepos+bitbucketrepos

for repo in repos:
    d=repodir+repo.split('/')[1]+".git"
    print "updating :",d
    subprocess.call(["/usr/bin/git", "fetch", "-q", "--all", "-p"], cwd=d)


