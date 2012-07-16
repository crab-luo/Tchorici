from fabric.api import env, run, local, settings, abort, prefix
from fabric.contrib.console import confirm

env.hosts = ['glor.cz']
env.cwd = '/home/yetty/projects/Tchorici/tchorici'


def deploy():
    with prefix('workon tchorici'):
        run('git pull')

        with settings(warn_only=True):
            result = run('./manage.py test')
        if result.failed and not confirm('Tests failed. Continue?'):
            if confirm('Return to previous version?'):
                run('git reset --hard @{1}')
            abort('Aborting...')

        run('./manage.py compress')
        run('sudo service tchorici restart')


def push():
    local('./manage.py test')
    local('git add -p')
    local('git commit')
    local('git push')
