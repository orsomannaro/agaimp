from . import ICON, ICON_MSG, TOOLTIP, TOOLTIP_MSG
from .views import SystrayApp

from apps.messagelogger.controllers import MessageLogger


class aGaiMpSysApp(SystrayApp):

    APP_WORKING = 0
    APP_WARNING = 1

    APP_STATUS = {
        APP_WORKING: (ICON, TOOLTIP),
        APP_WARNING: (ICON_MSG, TOOLTIP_MSG),
    }

    def __init__(self, frame, menu, icon=ICON, tooltip=TOOLTIP):
        super(aGaiMpSysApp, self).__init__(icon, tooltip, menu, frame)
        self._messages = MessageLogger(None)

    def exit(self):
        self._messages.close()
        self.close()

    def message(self, text):
        self._messages.log(text)
        self.status(self.APP_WARNING)

    def status(self, status):
        """ Imposta icona e tooltip """
        try:
            tray = self.APP_STATUS[status]
        except KeyError:
            pass  # case statement default action
        else:
            self.icon(*tray)

    def show_messages(self):
        self._messages.show()
        self.status(self.APP_WORKING)
