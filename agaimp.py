#!/usr/bin/env python

import os
import sys

from settings import *

from apps.agaimp import aGaiMp


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))

    # Carica server
    for server in INSTALLED_SERVERS:
        __import__(server)

    # App
    agaimp = aGaiMp()
    agaimp.MainLoop()
