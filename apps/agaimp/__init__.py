import wx

from settings import AGAIN_LOGO, TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from apps.server import servers_publisher
from apps.localparam.controllers import params

from .views import SystrayApp, Popup

from .mysol import MainFrame, SysOutListener


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
            ('Parametri', params.OnEdit),
        ]
        self.systrayapp = aGaiMpSysApp(TRAY_ICON, TRAY_TOOLTIP, menu)  # systray app

        # Popup
        # self.popup = Popup(AGAIN_LOGO)
        # servers_publisher.subscribe(self)

        self.frame = MainFrame(None, -1, 'rebinding stdout')
        self.frame.Show(True)
        self.frame.Center()
        servers_publisher.subscribe(SysOutListener)

    def OnClose(self, event):
        self.exit()

    def publish(self, message):
        dlg = wx.MessageDialog(self, message, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def exit(self):
        self.systrayapp.close()
        self.Exit()
