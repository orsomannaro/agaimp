import io
import wx

from Queue import Queue
from threading import Thread
from wx.lib.newevent import NewEvent

from gui.agaimp_gui import FrmSrvMsg

from settings import TRAY_TOOLTIP, TRAY_TOOLTIP_TITLE, TRAY_ICON, TRAY_ICON_WRN, TRAY_ICON_ERR

from .views import SystrayApp


class aGaiMpSysApp(SystrayApp):

    APP_WORKING = 0
    APP_WARNING = 1
    APP_ERROR = 2

    def __init__(self, frame, menu, icon=TRAY_ICON, tooltip=TRAY_TOOLTIP):
        super(aGaiMpSysApp, self).__init__(icon, tooltip, menu, frame)
        self._status = self.APP_WORKING

    def set_status(self, status, tooltip=TRAY_TOOLTIP):
        """ Imposta icona e tooltip
        :param status: APP_WORKING | APP_WARNING | APP_ERROR
        :param tooltip: tooltip
        """
        try:
            tray_icon = {
                self.APP_WORKING: TRAY_ICON,
                self.APP_WARNING: TRAY_ICON_WRN,
                self.APP_ERROR: TRAY_ICON_ERR,
            }[status]
        except KeyError:
            pass  # case statement default action
        else:
            if self._status != status:
                self._status = status
                self.set_icon(tray_icon, '%s: %s' % (TRAY_TOOLTIP_TITLE, tooltip))


wxShowMessageEvent, EVT_WX_SHOW_MSG = wx.lib.newevent.NewEvent()


class MeggageBuffer(object):
    """ Conserva i messaggi arrivati da server
    """
    def __init__(self):
        self._buffer = io.StringIO()

    def note(self, message):
        self._buffer.write(message)

    def get(self):
        return self._buffer.getvalue()

    def reset(self):
        self._buffer.close()
        self._buffer .__init__()


class aGaiMpMessages(object):
    """ Gestisce i messaggi in arrivo dal server.
    """

    def __init__(self, parent):
        self._frm = FrmSrvMsg(parent)
        self._frm.btn_close.Bind(wx.EVT_BUTTON, self.on_close)
        self._frm.btn_pause.Bind(wx.EVT_BUTTON, self.on_pause)
        self._frm.btn_reset.Bind(wx.EVT_BUTTON, self.on_reset)
        self._frm.txt_messages.Bind(EVT_WX_SHOW_MSG, self.on_log_event)

        self._log = MeggageBuffer()  # messaggi arrivati
        self._screen = Queue()  # coda messaggi ancora da visualizzare
        self._pause = False  # ferma la visualizzazione dei messaggi

        self._viewer = Thread(target=self.__monitor)  # visualizza i messaggi in coda
        self._viewer.daemon = True
        self._viewer.start()

    def on_close(self, event):
        self._frm.Hide()
        self._screen.queue.clear()

    def on_pause(self, event):
        self._pause = not self._pause

    def on_reset(self, event):
        self._log.reset()
        self._screen.queue.clear()
        self._frm.txt_messages.SetValue('')

    def on_log_event(self, event):
        msg = event.message.strip('\r')+'\n'  # formatta
        self._log.note(msg)  # memorizza
        self._frm.IsShown() and self._screen.put(msg)  # mostra

    def close(self):
        self._frm.Close()

    def log(self, message):
        evt = wxShowMessageEvent(message=message)
        wx.PostEvent(self._frm.txt_messages, evt)

    def show(self):
        self._frm.txt_messages.SetValue(self._log.get())
        self._frm.Show()
        self._pause = False

    def __monitor(self):
        while True:
            if not self._pause and not self._screen.empty():
                message = self._screen.get()
                wx.CallAfter(self._frm.txt_messages.AppendText, message)
