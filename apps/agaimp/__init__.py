import wx

from settings import AGAIN_LOGO, TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from apps.server import servers_publisher
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
