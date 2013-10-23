from settings import TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from .views import SystrayApp


class aGaiMpSysApp(SystrayApp):
    def __init__(self, frame, menu, icon=TRAY_ICON, tooltip=TRAY_TOOLTIP):
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
