import os
import wx

from settings import IMAGES_DIR

from apps import localparam

from .views.messagelogger import MessageLogger
from .views.systrayapp import SystrayApp


ICON = os.path.join(IMAGES_DIR, 'icon.ico')
ICON_MSG = os.path.join(IMAGES_DIR, 'icon_msg.ico')
TOOLTIP = 'aGaiMp: working'
TOOLTIP_MSG = 'aGaiMp: fare click su Messaggi'


class aGaiMpSysApp(SystrayApp):

    APP_WORKING = 0
    APP_WARNING = 1

    APP_STATUS = {
        APP_WORKING: (ICON, TOOLTIP),
        APP_WARNING: (ICON_MSG, TOOLTIP_MSG),
    }

    def __init__(self, frame, menu, icon=ICON, tooltip=TOOLTIP):
        super(aGaiMpSysApp, self).__init__(icon, tooltip, menu, frame)
        self._messages = MessageLogger(None)

    def exit(self):
        self._messages.close()
        self.close()

    def message(self, text):
        self._messages.log(text)
        self.status(self.APP_WARNING)

    def status(self, status):
        """ Imposta icona e tooltip """
        try:
            tray = self.APP_STATUS[status]
        except KeyError:
            pass  # case statement default action
        else:
            self.icon(*tray)

    def show_messages(self):
        self._messages.show()
        self.status(self.APP_WORKING)


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
        """ Messaggi in arrivo dai importers """
        msg = u'[%s] %s (%s): %s' % (message.time, message.sender, message.level, message.text)
        self.systrayapp.message(msg)
