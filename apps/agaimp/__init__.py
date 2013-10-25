import wx

from apps.localparam.controllers import localparam
from apps.messagelogger.controllers import MessageLogger

from .controllers import aGaiMpSysApp


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

        # Gestore messaggi server
        self.messages = MessageLogger(None)

    def on_close(self, event):
        self.messages.close()
        self.systrayapp.close()
        self.Exit()

    def on_edit_params(self, event):
        localparam.edit()

    def on_show_messages(self, event):
        self.messages.show()
        self.systrayapp.set_status(self.systrayapp.APP_WORKING)

    def publish(self, message):
        """ Messaggi in arrivo dai server
        """
        msg = u'[%s %s] %s (%s)' % (message.server, message.time, message.text, message.level)
        self.messages.log(msg)
        self.systrayapp.set_status(self.systrayapp.APP_ERROR)
