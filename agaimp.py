#!/usr/bin/env python

import os
import sys
import wx

from apscheduler.scheduler import Scheduler

from apps.importer.controllers import Importer
from apps.localparam.controllers import params
from apps.systrayapp.views import SystrayApp

from settings import TRAY_ICON, TRAY_TOOLTIP


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))

    app = wx.App()

    # App su systray
    systray = SystrayApp(TRAY_ICON, TRAY_TOOLTIP)
    systray.add_menu_item('Exit', systray.OnExit)
    systray.add_menu_item('Parametri', params.OnEdit)

    # Importer
    importer = Importer()
    importer.execute()

    # Schedulazione
    sched = Scheduler()
    sched.start()
    sched.add_interval_job(importer.execute, seconds=3)

    app.MainLoop()
    sched.shutdown()
    params.save()
