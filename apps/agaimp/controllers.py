from settings import TRAY_ICON, TRAY_ICON_WRN, TRAY_ICON_ERR, TRAY_TOOLTIP, TRAY_TOOLTIP_WRN, TRAY_TOOLTIP_ERR

from .views import SystrayApp


class aGaiMpSysApp(SystrayApp):
    APP_WORKING = 0
    APP_WARNING = 1
    APP_ERROR = 2

    def __init__(self, frame, menu, icon=TRAY_ICON, tooltip=TRAY_TOOLTIP):
        super(aGaiMpSysApp, self).__init__(icon, tooltip, menu, frame)
        self._status = self.APP_WORKING

    def set_status(self, status):
        """ Imposta icona e tooltip
        :param status: APP_WORKING | APP_WARNING | APP_ERROR
        :param tooltip: tooltip
        """
        try:
            tray = {
                self.APP_WORKING: (TRAY_ICON, TRAY_TOOLTIP),
                self.APP_WARNING: (TRAY_ICON_WRN, TRAY_TOOLTIP_WRN),
                self.APP_ERROR: (TRAY_ICON_ERR, TRAY_TOOLTIP_ERR)
            }[status]
        except KeyError:
            pass  # case statement default action
        else:
            if self._status != status:
                self._status = status
                icon, tooltip = tray
                self.set_icon(icon, tooltip)
