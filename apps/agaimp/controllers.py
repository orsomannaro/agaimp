import wx

from apps.localparam.controllers import localparam
from apps.systrayapp.controllers import aGaiMpSysApp


class aGaiMp(wx.App):
    """
    Main app
    """

    def __init__(self):
        wx.App.__init__(self, redirect=0)

        # Systray app
        menu = [
            ('Exit', self.on_close),
            ('Messaggi', self.on_show_messages),
            ('Parametri', self.on_edit_params),
        ]
        self.systrayapp = aGaiMpSysApp(None, menu)

    def on_close(self, event):
        self.systrayapp.exit()
        self.Exit()

    def on_edit_params(self, event):
        localparam.edit()

    def on_show_messages(self, event):
        self.systrayapp.show_messages()

    def publish(self, message):
        """ Messaggi in arrivo dai server
        """
        msg = u'[%s] %s (%s): %s' % (message.time, message.server, message.level, message.text)
        self.systrayapp.message(msg)
