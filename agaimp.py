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
    # Main
    app = wx.App()

    # App su systray
    frame = wx.Frame(None)
    agaimp_app = SystrayApp(TRAY_ICON, TRAY_TOOLTIP)
    agaimp_app.add_menu_item('Exit', agaimp_app.OnExit)
    agaimp_app.add_menu_item('Parametri', params.OnEdit)

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
