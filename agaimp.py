#!/usr/bin/env python

import os
import sys
import wx


from apps import importer
from apps.parameters import Paramenters
from apps.systrayapp import TaskBarIcon


def menu_paramenters(event):
    """
    Visualizza la finestra dei parametri.

    :param event:
     parametro tornato quando viene cliccato il tasto sinistro
     su una voce di un menu wx.TaskBarIcon.
    """
    agaimp_param = Paramenters(None)
    agaimp_param.Show()


def menu_start(event):
    importer.start()


def menu_stop(event):
    importer.stop()


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))
    app = wx.App()
    # Iniziallizza e avvia app su systray
    agaimp_app = TaskBarIcon()
    agaimp_app.add_menu_item('Parametri', menu_paramenters)
    agaimp_app.add_menu_item('Start', menu_start)
    agaimp_app.add_menu_item('Stop', menu_stop)
    importer.start()
    app.MainLoop()
