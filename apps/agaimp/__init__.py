from settings import TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from apps.localparam.controllers import params

from .views import SystrayApp


class aGaiMpSysApp(SystrayApp):
    def __init__(self, frame=None):
        super(aGaiMpSysApp, self).__init__(TRAY_ICON, TRAY_TOOLTIP, frame)
        self.menu = [
            ('Parametri', params.OnEdit),
            ('Exit', self.OnClose),
        ]

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
