import logging
import wx

from settings import AGAIN_LOGO, TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from apps.server import servers_publisher
from apps.server.publisher import SRV_NAME, SRV_MSG_LVL, SRV_MSG_TXT, ERR_SRV_MSG_LVL, LOG_SRV_MSG_LVL
from apps.localparam.controllers import localparam

from .views import SystrayApp


class aGaiMpSysApp(SystrayApp):
    def __init__(self, icon, tooltip, menu, frame=None):
        super(aGaiMpSysApp, self).__init__(icon, tooltip, menu, frame)

    def set_error(self, tooltip=''):
        """ Imposta icona di errore self.err_icon.
        :param tooltip: eventuale tooltip di errore
        """
        self.set_icon(TRAY_ICON_ERR, tooltip)

    def set_default(self, tooltip=''):
        """ Imposta icona di errore self.err_icon.
        :param tooltip: eventuale tooltip di errore
        """
        self.set_icon(TRAY_ICON, TRAY_TOOLTIP)

    def set_warning(self, tooltip=''):
        """ Imposta icona di errore self.err_icon.
        :param tooltip: eventuale tooltip di errore
        """
        self.set_icon(TRAY_ICON_WRN, tooltip)


class aGaiMp(wx.App):
    """
    Main notifier app
    """

    def __init__(self):
        wx.App.__init__(self, redirect=0)

        # Systray
        menu = [
            ('Exit', self.OnClose),
            ('Logs', self.OnShowLogs),
            ('Parametri', self.OnEditParams),
        ]
        self.systrayapp = aGaiMpSysApp(TRAY_ICON, TRAY_TOOLTIP, menu)  # systray app

        self.logs = ''

    def OnClose(self, event):
        self.exit()

    def OnEditParams(self, event):
        localparam.edit()

    def OnShowLogs(self, event):
        pass

    def publish(self, message):
        self.logs += '%s\n' % message

    def exit(self):
        self.systrayapp.close()
        self.Exit()


class aGaiMpServerSubscriber(object):
    """
    Stampa i messaggi dei Publisher su console
    """

    def __init__(self, sub_name):
        self.filename='%s.log' % sub_name,

    def publish(self, message):
        if message[SRV_MSG_LVL] == LOG_SRV_MSG_LVL:
            print '%s %s: %s' % (message[SRV_NAME], message[SRV_MSG_LVL], message[SRV_MSG_TXT])


agaimp_server_sub = aGaiMpServerSubscriber('agaimp_server_sub')
servers_publisher.subscribe(agaimp_server_sub)
