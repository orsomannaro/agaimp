import wx

from apscheduler.scheduler import Scheduler

from settings import AGAIN_LOGO, TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from apps.importer.controllers import Importer
from apps.localparam.controllers import params

from .views import SystrayApp, Popup

from wx.lib.pubsub.pub import Publisher

from .server import SERVER_TOPIC


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
    """ Main notifier app
    """

    def __init__(self):
        wx.App.__init__(self, redirect=0)

        menu = [
            ('Exit', self.OnClose),
            ('Parametri', params.OnEdit),
        ]
        self.systrayapp = aGaiMpSysApp(TRAY_ICON, TRAY_TOOLTIP, menu)  # systray app
        self.popup = Popup(AGAIN_LOGO)
        self.importer = Importer()

        # Create a pubsub receiver.
        Publisher().subscribe(self.update_display, SERVER_TOPIC)

        # Importer
        self.importer = Importer()
        try:
            self.importer.execute()
        except:
            raise
        # else:
        #     self.importer.schedule()

        # main timer routine
        # timer = wx.Timer(self, -1)
        # self.Bind(wx.EVT_TIMER, self.OnTimer, timer)
        # timer.Start(500)
        # self.MainLoop()

    def OnClose(self, event):
        self.exit()

    def OnTimer(self, event):
        self.main()

    def main(self):
        pass

        # for item in self.reader.items():
        #     print '%s\n' % item.title

        # if not self.popup.opened():
        #     # show popup for next new item
        #     msg = ''
        #     for item in self.reader.get_items():
        #         msg += '%s\n' % item.summary
        #     if msg:
        #         self.popup.show(msg)

    def exit(self):
        # close objects and end
        self.importer.shutdown()
        self.systrayapp.close()
        self.Exit()

    def status_update(self, event):
        """ Receives status from thread and updates the display.
        """
        print event.status

    def update_display(self, message):
        """ Receives message from thread and updates the display.
        """
        data = message.data
        print '%s' % data

