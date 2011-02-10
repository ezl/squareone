import os
from settings import PROJECT_DIR


# paths to files that to be catted to debconf-set-selections
DEBCONF_SEEDS = (
    os.path.join(PROJECT_DIR, 'deploy/debconf_seeds/exim4.seed'),
)

# the packages will be installed in order, so order matters
BASIC_PACKAGES = (
    'exim4',
    'apticron',
    'aptitude',
    'apt-listchanges',
    'emacs22-nox',
    'emacs-goodies-el',
    'exuberant-ctags',
    'gcc',
    'git-core',
    'ipython',
    'language-pack-en',   # so perl will STFU
    'man',
    'manpages',
    'mercurial',
    'python-dev',
    'python-imaging', # because it is hard to install onto virtualenvs
    'python-mode',
    'python-pip',
    'python-psycopg2',
    'python-pysqlite2',
    'python-setuptools',
    'python-virtualenv',
    'screen',
    'sqlite3',
    'subversion',
    'vim-nox',
    'zsh',
)


SSH_KEYS_DIR = os.path.join(PROJECT_DIR, 'deploy', 'ssh-keys')
SYSADMINS = {
# example: 'username': {'shell': 'bash' , 'email': 'username@example.com', 'ssh_key':/home/username/.ssh/id_rsa.pub }
# make sure the keys are absolute paths to local files
    'ezl': {
            'shell':        'bash',
            'email':        'ericzliu@gmail.com',
            'ssh_key_path': os.path.join(SSH_KEYS_DIR, 'ezl-id_rsa.pub')
        },
}

HOSTS = (
#   ('ip address', 'hostname'),
    ('173.255.225.206', 'poop'),
)


PROJECT_NAME = "squareone"
GIT_URL = "https://github.com/ezl/squareone.git"

PROJECT_USERNAME = None
GIT_BRANCH = "master"
DJANGO_SETTINGS_MODULE = "production-settings"

# ==================
POSTGRES_USERNAME = "squareone"
POSTGRES_PASSWORD = "squareone"
POSTGRES_DBNAME = "squareone"

APACHE_SERVER_NAME = "leasely.com"
APACHE_SERVER_ALIAS = "*.leasely.com"
APACHE_SERVER_ADMIN = "null@example.com"
