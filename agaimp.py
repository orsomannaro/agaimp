#!/usr/bin/env python

import os
import sys

import wx

from apps.importer.controllers import get_importer
from apps.localparam import params
from apps.localparam.controllers import EditParams
from apps.systrayapp.views import SystrayApp
from apps.userauth import user_auth

from settings import TRAY_ICON, TRAY_TOOLTIP


def menu_paramenters(event):
    """ Visualizza la finestra dei parametri.
    """
    EditParams(None, params)


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))
    app = wx.App()
    # App su systray
    frame = wx.Frame(None)
    agaimp_app = SystrayApp(TRAY_ICON, TRAY_TOOLTIP)
    agaimp_app.add_menu_item('Exit', agaimp_app.OnExit)
    agaimp_app.add_menu_item('Parametri', menu_paramenters)
    # Esecuzione e schedulazione importer
    importer = get_importer(user_auth['servers'])
    importer.start()
    app.MainLoop()
    params.save()
    importer.shutdown()
