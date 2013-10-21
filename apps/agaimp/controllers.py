import io

from settings import TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from .views import SystrayApp, aGaiMpMessages


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


class ServerMessages(object):
    """
    Gestione dei messaggi provenienti dai server
    """

    def __init__(self):
        self._messages = io.StringIO()
        self._gui = None

    def add(self, message):
        """
        Archivia i messaggi inviati dai server.
        Nota:
         i server girano su thread; se i loro arresto non viene debitamente gestito
         potrebbero arrivare messaggi anche quando self._messages e' gia' stato chiuso.
        """
        try:
            self._messages.write(message)
            if self._gui:
                self._gui.update()
        except:
            pass

    def close(self):
        if not self._messages.closed:
            self._messages.close()

    def get(self):
        return self._messages.getvalue()

    def show(self):
        if not self._gui:
            self._gui = aGaiMpMessages(None, self._messages)

    def reset(self):
        self.close()
        self._messages = io.StringIO()
