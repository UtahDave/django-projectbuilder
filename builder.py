#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.28

#
# Requires fabric, virtualenv, and virtualenvwrapper
#

# FIXME This shouldn't be hard-coded
GENERIC_SCRIPTS_PATH = 'generic_scripts/'

#import pbs
import commands, pbs, os, random, string, sys

USAGE = '%s /path/to/new/project_name' % (sys.argv[0])
FUTURE_USAGE = USAGE + ' [--cms] [--zinnia]'

if len(sys.argv) < 2:
    print USAGE
    sys.exit(0)

# FIXME Every file in generic_scripts and *-generic should be listed
# here... or we can copy entire directories
pathify = {
    # 'urls_dev.py':       '',
    'cms_settings.py':   'extra_settings/',
    'django.wsgi':       'apache/',
    '__init__.py':       '',
    '__init__.py':       'extra_settings/',
    'manage.py':         '',
    'model_forms.py':    '%(PROJECT_NAME)s/',
    'models.py':         '%(PROJECT_NAME)s/',
    'requirements.txt':  '',
    'settings.py':       '',
    'settings_local.py': '',
    'tests.py':          '%(PROJECT_NAME)s/',
    'urls.py':           '',
    'views.py':          '%(PROJECT_NAME)s/',
    'zinnia_settings.py':'extra_settings/',
}
weird_files = ['manage.py']

HOME_DIR = os.path.expandvars('$HOME').rstrip('/') + '/'

# Trailing / may be included or excluded
PROJECT_PATH = sys.argv[1].rstrip('/') + '/'
PROJECT_NAME = PROJECT_PATH.split('/')[-2]
BASE_PATH    = '/'.join(PROJECT_PATH.split('/')[:-2]) + '/'

# Make virtualenv
# FIXME Shouldn't assume the location of virtualenvwrapper.sh
cmd  = 'bash -c "source /usr/local/bin/virtualenvwrapper.sh'
cmd += ' && mkvirtualenv %s --no-site-packages"' % (PROJECT_NAME)
commands.getstatusoutput(cmd)

#(pbs.which('virtualenvwrapper.sh'), ))
##VIRTUALENV_PATH = HOME_DIR + '.virtualenvs/' + PROJECT_NAME

SECRET_KEY = ''.join([ random.choice(string.printable[:94].replace("'", ""))
                       for _ in range(50) ])
PROJECT_PASSWORD = ''.join([ random.choice(string.printable[:67].replace("'", ""))
                             for _ in range(30) ])

replacement_values = {
    'PROJECT_NAME':     PROJECT_NAME,
    'PROJECT_PASSWORD': PROJECT_PASSWORD,
    'BASE_PATH':        BASE_PATH,
    'SECRET_KEY':       SECRET_KEY,
}

# Make directories
# FIXME Add more dirs to this list
for dir_name in ['', 'media', 'static', 'templates', 'apache', 'extra_settings',
                 '%(PROJECT_NAME)s']:
    os.mkdir(PROJECT_PATH + dir_name % replacement_values)


generic_files = [x for x in os.listdir(GENERIC_SCRIPTS_PATH)
                 if x.endswith('-generic')]

for filename in generic_files:
    # Grab *-generic filenames
    f_read = open(GENERIC_SCRIPTS_PATH + filename, 'r')
    contents = f_read.read()
    f_read.close()

    # Replace %(SECRET_KEY)s, etc with new value for new project
    new_filename = filename.replace('-generic', '')
    # Path names include '%(PROJECT_NAME)s', etc
    file_path = pathify[new_filename] % replacement_values
    f_write = open(PROJECT_PATH + file_path + new_filename, 'a')
    #print "File:", new_filename
    if new_filename not in weird_files:
        new_contents = contents % replacement_values
    else:
        new_contents = contents
    f_write.write(new_contents)
    f_write.close()