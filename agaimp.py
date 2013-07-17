#!/usr/bin/env python

import os
import sys
import wx


from apps.importer import importer
from apps.taskbarapp import taskbarapp
from apps.parameters import paramenters_menu



def main():
    """
    main
    """
    app = wx.App()
    taskbarapp.add_menu_item('Parametri', paramenters_menu)
    importer.start()
    app.MainLoop()


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))
    # Run
    main()
