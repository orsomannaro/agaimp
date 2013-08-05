import os
import wx
import feedparser

from settings import AGAIN_LOGO, TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from apps.localparam.controllers import params

from .views import SystrayApp, Popup


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


class Reader(object):
    """
    Lettore di feed.
    Genera le voci dei feed aggiunti.
    """

    def __init__(self):
        self.feeds = {}

    def add_feed(self, name, source, max_items=10):
        self.feeds[name] = (source, max_items)

    def del_feed(self, name):
        del self.feeds[name]

    def items(self):
        for name in self.feeds.keys():
            source, max_items = self.feeds[name]
            feed = feedparser.parse(r'%s' if os.path.isfile(source) else '%s' % source)
            for entry in feed.entries[:max_items]:
                yield entry


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
        self.reader = Reader()
        self.reader.add_feed('digg', 'http://digg.com/rss/index.xml')

        # main timer routine
        timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self.OnTimer, timer)
        timer.Start(500)
        self.MainLoop()

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

    def again(self):
        print "again"

    def settings(self):
        print "settings"

    def exit(self):
        # close objects and end
        self.systrayapp.close()
        self.Exit()
