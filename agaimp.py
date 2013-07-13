#!/usr/bin/env python

import os
import sys
import wx

from apps.taskbarapp import TaskBarIcon


def again_import(event):
    print 'Import!'


def again_parameters(event):
    print 'Parametri!'


def main():
    app = wx.App()
    tb = TaskBarIcon()
    tb.add_menu_item('Parametri', again_parameters)
    tb.add_menu_item('Import', again_import)
    app.MainLoop()


if __name__ == '__main__':
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))
    # Run
    main()
