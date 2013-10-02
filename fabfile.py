__author__ = 'vijay'
from fabric.api import env, local, run
import LaunchEC2
import TerminateEC2

#env.hosts = ['host.name.com']
#env.user = 'user'
#env.key_filename = '/path/to/keyfile.pem'

def local_uname():
    local('uname -a')

def remote_uname():
    run('uname -a')

def deploy():
    LaunchEC2.launch_instance(cmd_shell=False)
    TerminateEC2.terminateAll()