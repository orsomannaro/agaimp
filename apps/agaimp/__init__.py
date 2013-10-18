import wx

from settings import AGAIN_LOGO, TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from apps.server.publisher import SRV_NAME, SRV_MSG_LVL, SRV_MSG_TXT, ERR_SRV_MSG_LVL, LOG_SRV_MSG_LVL
from apps.localparam.controllers import localparam

from .controllers import ServerMessages
from .views import SystrayApp


class aGaiMpSysApp(SystrayApp):
    def __init__(self, icon, tooltip, menu, frame=None):
        super(aGaiMpSysApp, self).__init__(icon, tooltip, menu, frame)

    def set_default_icon(self, tooltip=''):
        """ Imposta icona di errore self.err_icon.
        :param tooltip: eventuale tooltip di errore
        """
        self.set_icon(TRAY_ICON, TRAY_TOOLTIP)

    def set_error_icon(self, tooltip=''):
        """ Imposta icona di errore self.err_icon.
        :param tooltip: eventuale tooltip di errore
        """
        self.set_icon(TRAY_ICON_ERR, tooltip)

    def set_warning_icon(self, tooltip=''):
        """ Imposta icona di errore self.err_icon.
        :param tooltip: eventuale tooltip di errore
        """
        self.set_icon(TRAY_ICON_WRN, tooltip)


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
        self._systrayapp = aGaiMpSysApp(TRAY_ICON, TRAY_TOOLTIP, menu)

        # Messaggi dai server
        self._messages = ServerMessages()

    def OnClose(self, event):
        self.exit()

    def OnEditParams(self, event):
        localparam.edit()

    def OnShowMessages(self, event):
        if self._messages.show():
            self._systrayapp.set_default_icon()

    def publish(self, message):
        """ Messaggi in arrivo dai server
        """
        if message[SRV_MSG_LVL] == ERR_SRV_MSG_LVL:  # messaggio di errore
            msg = u'%s %s: %s\n' % (message[SRV_NAME], message[SRV_MSG_LVL], message[SRV_MSG_TXT])
            self._messages.add(msg)
            self._systrayapp.set_error_icon('aGaiMp: fai click su Messaggi')

    def exit(self):
        self._messages.close()
        self._systrayapp.close()
        self.Exit()
