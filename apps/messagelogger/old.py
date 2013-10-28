import wx

from Queue import Queue
from threading import Thread
from wx.lib.newevent import NewEvent

from gui.agaimp_gui import FrmSrvMsg

from .models import MessageBuffer


wxShowMessageEvent, EVT_WX_SHOW_MSG = wx.lib.newevent.NewEvent()


class MessageLogger(object):
    """
    Gestisce i messaggi in arrivo dal server.
    """

    def __init__(self, parent):
        self._frm = FrmSrvMsg(parent)
        self._frm.Bind(wx.EVT_CLOSE, self.on_close)
        self._frm.btn_close.Bind(wx.EVT_BUTTON, self.on_close)
        self._frm.btn_pause.Bind(wx.EVT_BUTTON, self.on_pause)
        self._frm.btn_reset.Bind(wx.EVT_BUTTON, self.on_reset)
        self._frm.txt_messages.Bind(EVT_WX_SHOW_MSG, self.on_log_event)

        self._log = MessageBuffer()  # messaggi arrivati
        self._screen = Queue()  # coda messaggi ancora da visualizzare

        # controllore coda messaggi ancora da visualizzare
        self._viewer = None
        self._viewer_running = False
        self._viewer_pause = False  # ferma la visualizzazione dei messaggi

    def on_close(self, event):
        self._stop_monitor()
        self._frm.Hide()

    def on_pause(self, event):
        self._viewer_pause = not self._viewer_pause

    def on_reset(self, event):
        self._log.reset()
        self._screen.queue.clear()
        self._frm.txt_messages.SetValue('')

    def on_log_event(self, event):
        self._frm.txt_messages.AppendText(event.message)
        #wx.CallAfter(self._frm.txt_messages.AppendText, event.message)

    def close(self):
        self._frm.Close()

    def log(self, message):
        msg = message.strip('\r') + '\n'  # formatta
        self._log.note(msg)  # memorizza
        self._frm.IsShown() and self._screen.put(msg)  # visualizza

    def show(self):
        self._start_monitor(self._log.get())
        self._frm.Show()

    def _monitor(self):
        while self._viewer_running:
            if not self._screen.empty() and not self._viewer_pause:
                evt = wxShowMessageEvent(message=self._screen.get())
                wx.PostEvent(self._frm.txt_messages, evt)  # PostEvent garantisce corretta sequenza

    def _start_monitor(self, text):
        self._frm.txt_messages.SetValue(text)
        self._viewer_pause = False
        self._viewer_running = True
        self._viewer = Thread(target=self._monitor)
        self._viewer.daemon = True
        self._viewer.start()

    def _stop_monitor(self):
        self._screen.queue.clear()
        self._viewer_pause = False
        self._viewer_running = False


class MessageMonitor(Thread):

    def __init__(self, widget):
        super(MessageMonitor, self).__init__()
        self._widget = widget
        self.daemon = True
        self._running = True
        self._pause = False
        self._logs = Queue()  # coda messaggi ancora da visualizzare

    def log(self, text):
        self._widget.IsShown() and self._logs.put(text)

    def terminate(self):
        self._logs.queue.clear()
        self._pause = False
        self._running = False

    def run(self):
        while self._running:
            if not self._logs.empty() and not self._pause:
                evt = wxShowMessageEvent(message=self._logs.get())
                wx.PostEvent(self._widget, evt)  # PostEvent garantisce corretta sequenza

