#!/usr/bin/env python

import os
import sys

from apscheduler.scheduler import Scheduler

from settings import *

from apps.agaimp.controllers import aGaiMp
from apps.server import importer, servers_publisher


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))

    # App
    agaimp = aGaiMp()
    servers_publisher.subscribe(agaimp)

    # Importer
    try:
        importer.execute()
    except:
        raise

    # Scheduler
    sched = Scheduler()
    sched.start()
    sched.add_interval_job(importer.execute, seconds=3)  # solo per test
    #sched.add_cron_job(importer.execute,
    #                   day_of_week=RUN_AT['d'],
    #                   hour=RUN_AT['h'],
    #                   minute=RUN_AT['m'])

    agaimp.MainLoop()

    # Quit
    sched.shutdown()
