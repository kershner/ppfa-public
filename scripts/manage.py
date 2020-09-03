#!/usr/bin/env python
import os
import sys
import importlib

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pp.settings.local")
    settings = os.environ['DJANGO_SETTINGS_MODULE']
    try:
        importlib.import_module(settings)
    except ImportError as e:
        sys.stderr.write('''
Error: {e}
       Can't import `{settings}` module.

The settings file is missing or the file has syntax errors. Check the file
or create a `local.py` file in `pp/settings/` using the example file aside.
        '''.format(e=str(e), settings=settings))
        sys.exit()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
