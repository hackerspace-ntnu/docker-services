from fabric.api import env,run,cd
from fabric.context_managers import prefix
from fabric.operations import sudo

env.hosts = ['localhost']
root_folder = '/devops/'
project_folder = '/website'

def createserver(project='prod', branch='master',name='test'):
    with cd(root_folder):
        sudo('mkdir '+name)
        with cd(root_folder+name):
            sudo('git clone https://github.com/hackerspace-ntnu/docker-services.git')
            sudo('git clone https://github.com/hackerspace-ntnu/website.git')
            sudo('cp '+root_folder+'.env docker-services')
            update_nginx(name)
            create_cert(name)
            updateserver(name)
            with cd(root_folder+name+'/docker-services'):
                run('docker-compose docker-compose.yml up -d')

def update_nginx(name='test'):
    pass
def create_cert(name='test'):
    pass
def updateserver(name='name'):
    pass

def deleteserver(project='prod',branch='master', name='test'):
    with cd(root_folder):
        sudo('rm -rf '+name)
