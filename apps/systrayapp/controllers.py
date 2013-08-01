import wx

from .views import SystrayApp


class aGaiMp(wx.App):
    def __init__(self, icon, tooltip, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.systray = SystrayApp(icon, tooltip)
