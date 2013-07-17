#!/usr/bin/env python

import os
import sys
import wx


from apps.importer import importer
from apps.taskbarapp import TaskBarIcon
from apps.parameters import Paramenters
from apps.userauth import authenticate


def parameters(event):
    """
    :param event:
    """
    param = Paramenters(None)
    param.Show()


@authenticate
def import_data():
    importer.start()


def main():
    """
    main
    """
    app = wx.App()
    # creazione del menu
    tb = TaskBarIcon()
    tb.add_menu_item('Parametri', parameters)
    # importazione dati
    import_data()
    app.MainLoop()


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))
    # Run
    main()
