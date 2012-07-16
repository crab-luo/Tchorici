from fabric.api import env, run, local

env.hosts = ['glor.cz']
env.cwd = '/home/yetty/projects/Tchorici/'


def push():
    local('./manage.py test')
    local('git add -p')
    local('git commit')
    local('git push')
