#!/usr/bin/env python

import os
import sys
import wx

from apps.TaskBarIcon import TaskBarIcon


def say_ciao(event):
    print 'Ciao!'


def main():
    app = wx.App()
    tb = TaskBarIcon()
    tb.add_menu_item("ciao", say_ciao)
    app.MainLoop()


if __name__ == "__main__":
    # Add directory in PYTHONPATH
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))
    # Run
    main()
