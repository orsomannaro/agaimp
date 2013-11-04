#!/usr/bin/env python

import sys

from apscheduler.scheduler import Scheduler

from settings import *

from apps import server  # prima di import e uploader
from apps import importer
from apps import uploader
from apps.agaimp.controllers import aGaiMp


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))

    # App
    agaimp = aGaiMp()
    server.servers_publisher.subscribe(agaimp)

    importer.start()
    uploader.start()

    # Scheduler
    sched = Scheduler()
    sched.start()
    sched.add_interval_job(importer.start, seconds=3)  # solo per test
    #sched.add_cron_job(importer.execute,
    #                   day_of_week=RUN_AT['d'],
    #                   hour=RUN_AT['h'],
    #                   minute=RUN_AT['m'])

    agaimp.MainLoop()

    # Quit
    sched.shutdown()
