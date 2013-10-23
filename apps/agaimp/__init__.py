import logging
import wx

from apps.localparam.controllers import localparam
from apps.server.publisher import SRV_NAME, SRV_MSG_LVL, SRV_MSG_HMS, SRV_MSG_TXT, ERR_SRV_MSG_LVL

from .controllers import aGaiMpSysApp
from .views import wxLogHandler, aGaiMpMessages


logger = logging.getLogger(__name__)


class aGaiMp(wx.App):
    """
    Main app
    """

    def __init__(self):
        wx.App.__init__(self, redirect=0)

        # Systray app
        menu = [
            ('Exit', self.OnClose),
            ('Messaggi', self.OnShowMessages),
            ('Parametri', self.OnEditParams),
        ]
        self._systrayapp = aGaiMpSysApp(None, menu)

        # Messaggi dai server
        self._gui = aGaiMpMessages(None)

        FORMAT = "%(asctime)s %(levelname)s %(message)s"
        handler = wxLogHandler(self._gui.txt_messages)
        handler.setFormatter(logging.Formatter(FORMAT))
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

    def OnClose(self, event):
        #TODO: bisognerebbe gestire arresto dei server
        self.exit()

    def OnEditParams(self, event):
        localparam.edit()

    def OnShowMessages(self, event):
        self._systrayapp.set_default_icon()
        self._gui.Show()

    def publish(self, message):
        """ Messaggi in arrivo dai server
        """
        if message[SRV_MSG_LVL] == ERR_SRV_MSG_LVL:  # messaggio di errore
            msg = '[%s %s] %s\n' % (message[SRV_NAME], message[SRV_MSG_HMS], message[SRV_MSG_TXT])
            #self._systrayapp.set_error_icon('aGaiMp: fai click su Messaggi')
            logger.log(logging.DEBUG, "More? click again!")

    def exit(self):
        self._systrayapp.close()
        self.Exit()
