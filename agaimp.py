#!/usr/bin/env python

import os
import sys

from settings import *

from apps.agaimp import aGaiMp
from apps.importer import importer

import logging
logging.basicConfig()

if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))

    # App
    agaimp = aGaiMp()

    # Importer
    try:
        importer.execute()
    except:
        raise
    else:
        importer.schedule()

    agaimp.MainLoop()
    importer.shutdown()
