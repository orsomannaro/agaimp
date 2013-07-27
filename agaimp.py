#!/usr/bin/env python

import os
import sys
import wx


from apps import importer
from apps.localparam.views import edit_param
from apps.systrayapp import TaskBarIcon


def menu_paramenters(event):
    """ Visualizza la finestra dei parametri.
    """
    edit_param()


def menu_force(event):
    """ Forza l'esecuzione degli importer.
    """
    importer.execute()


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))
    app = wx.App()
    # Iniziallizzazione e avvio app su systray
    agaimp_app = TaskBarIcon()
    agaimp_app.add_menu_item('Parametri', menu_paramenters)
    agaimp_app.add_menu_item('Force', menu_force)
    # Esecuzione e schedulazione importer
    try:
        importer.execute()
    except:
        print 'errore eseguendo importer'
        raise
    else:
        importer.schedule()
    app.MainLoop()
    importer.shutdown()
