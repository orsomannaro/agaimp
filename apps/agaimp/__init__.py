import wx

from apps.localparam.controllers import localparam
from apps.server.publisher import SRV_NAME, SRV_MSG_LVL, SRV_MSG_HMS, SRV_MSG_TXT, ERR_SRV_MSG_LVL

from .controllers import aGaiMpSysApp, aGaiMpMessages


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
        self._systrayapp = aGaiMpSysApp(None, menu)

        # Gestore messaggi server
        self._messages = aGaiMpMessages(None)

    def on_close(self, event):
        # TODO: bisognerebbe gestire arresto dei server
        self._messages.close()
        self._systrayapp.close()
        self.Exit()

    def on_edit_params(self, event):
        localparam.edit()

    def on_show_messages(self, event):
        self._systrayapp.set_default_icon()
        self._messages.show()

    def publish(self, message):
        """ Messaggi in arrivo dai server
        """
        if message[SRV_MSG_LVL] == ERR_SRV_MSG_LVL:  # messaggio di errore
            msg = '[%s %s] %s' % (message[SRV_NAME], message[SRV_MSG_HMS], message[SRV_MSG_TXT])
            #self._systrayapp.set_error_icon('aGaiMp: fai click su Messaggi')
            self._messages.log(msg)
