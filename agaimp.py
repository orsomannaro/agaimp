#!/usr/bin/env python

import os
import sys
import wx

from settings import TRAY_ICON, TRAY_TOOLTIP

from apps.importer.controllers import importer
from apps.localparam.controllers import params
from apps.systrayapp.views import SystrayApp


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))

    # App su systray
    app = wx.App()
    systray = SystrayApp(TRAY_ICON, TRAY_TOOLTIP)
    systray.add_menu_item('Exit', systray.OnExit)
    systray.add_menu_item('Parametri', params.OnEdit)

    # Importer
    importer.execute()
    importer.schedule()

    app.MainLoop()
    importer.shutdown()
    params.save()
