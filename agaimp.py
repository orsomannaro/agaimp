#!/usr/bin/env python

import sys

from apscheduler.scheduler import Scheduler

from settings import *

from apps import importers
from apps import uploader
from apps.agaimp import aGaiMp
from apps.userauth import get_importers


def start_importer():
    for importer in get_importers():
        importers.start(importer)


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))

    # App
    agaimp = aGaiMp()
    importers.publisher.subscribe(agaimp)

    start_importer()
    uploader.start()

    # Scheduler
    sched = Scheduler()
    sched.start()
    sched.add_interval_job(start_importer, seconds=3)  # solo per test
    #sched.add_cron_job(importers.execute,
    #                   day_of_week=RUN_AT['d'],
    #                   hour=RUN_AT['h'],
    #                   minute=RUN_AT['m'])

    agaimp.MainLoop()

    # Quit
    sched.shutdown()
