from settings import TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_ERR

from apps.localparam.controllers import params

from .views import SystrayApp


class aGaiMp(SystrayApp):
    def __init__(self, frame=None):
        super(aGaiMp, self).__init__(TRAY_ICON, TRAY_TOOLTIP, frame)
        self.add_menu_item('Exit', self.OnExit)
        self.add_menu_item('Parametri', params.OnEdit)

    def OnExit(self, event):
        self.exit()

    def set_error(self, tooltip=''):
        """ Imposta icona di errore self.err_icon.
        :param tooltip: eventuale tooltip di errore
        """
        self.set_icon(TRAY_ICON_ERR, tooltip)

