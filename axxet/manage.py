#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    env = os.getenv('AXXET_ENVIRONMENT') or 'dev'
    if env not in ('dev', 'prod'):
        env = 'dev'
    os.environ.setdefault("AXXET_ENVIRONMENT", env)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "axxet.settings.%s" % env)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)