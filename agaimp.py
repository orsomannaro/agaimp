#!/usr/bin/env python

import os
import sys
import wx


from apps.Importer import importer
from apps.taskbarapp import TaskBarIcon
from apps.parameters import Paramenters


def parameters(event):
    """
    :param event:
    """
    param = Paramenters(None)
    param.Show()


def main():
    """
    main
    """
    app = wx.App()
    tb = TaskBarIcon()
    tb.add_menu_item('Parametri', parameters)
    importer.start()
    app.MainLoop()


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))
    # Run
    main()
