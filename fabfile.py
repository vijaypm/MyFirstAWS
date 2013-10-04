__author__ = 'vijay'
from fabric.api import env, local, run, execute, cd
import LaunchEC2
import TerminateEC2
import defaults
import time

#env.hosts = []
env.user = defaults.EC2_USER_BITNAMI
env.key_filename = defaults.KEY_PATH
env.connection_attempts = 3

def local_uname():
    local('uname -a')

def remote_uname():
    run('uname -a')

def deploy_photosite():
    run('sudo pip install pil')
    run('sudo pip install boto')
    run('sudo pip install django-registration')
    run('sudo pip install django-registration-defaults')
    run('sudo pip install django-ses')
    run('sudo pip install django-storages')
    run('sudo pip install wsgiref')
    run("echo 'Y' | sudo apt-get install git")
    run('git clone https://github.com/vijaypm/MyPhotoSite.git')
    with cd('MyPhotoSite'):
        run('python manage.py syncdb')
        run('python manage.py runserver 0.0.0.0:%s' % defaults.DJANGO_PORT)

def deploy():
    instance = LaunchEC2.launch_instance(cmd_shell=False)[0]
    sleeptime = 30
    print('sleeping for %d seconds' % sleeptime)
    time.sleep(sleeptime)

    print('attempting to connect to %s' % instance.public_dns_name)
    execute(deploy_photosite, hosts=[instance.public_dns_name])

def undeploy():
    TerminateEC2.terminateAll()