#!c:\projects\personaldevelopment\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PersonalDevelopment','console_scripts','initialize_PersonalDevelopment_db'
__requires__ = 'PersonalDevelopment'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('PersonalDevelopment', 'console_scripts', 'initialize_PersonalDevelopment_db')()
    )
