import os
import sys

path = 'D:\\python-codes\\'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'cyan.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

