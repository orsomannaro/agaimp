import io
import wx

from Queue import Queue
from threading import Thread
from wx.lib.newevent import NewEvent

from gui.agaimp_gui import FrmSrvMsg


wxShowMessageEvent, EVT_WX_SHOW_MSG = wx.lib.newevent.NewEvent()


class MessageBuffer(object):
    """ Conserva messaggi
    """
    def __init__(self):
        self._buffer = io.StringIO()

    def log(self, message):
        self._buffer.write(message)

    def get(self):
        return self._buffer.getvalue()

    def reset(self):
        self._buffer.close()
        self._buffer .__init__()


class MessageMonitor(Thread):

    def __init__(self, widget, log_queue):
        super(MessageMonitor, self).__init__()
        self._widget = widget
        self._logs = log_queue
        self._running = True
        self._pause = False
        self.daemon = True

    def pause(self):
        self._pause = not self._pause

    def stop(self):
        self._pause = False
        self._running = False

    def run(self):
        print 'start'
        while self._running:
            if not self._logs.empty() and not self._pause:
                evt = wxShowMessageEvent(message=self._logs.get())
                wx.PostEvent(self._widget, evt)
        print 'stop'


class MessageViewer(object):

    def __init__(self, widget):
        super(MessageViewer, self).__init__()
        self._widget = widget  # wx.TextCtrl interessato
        self._logs = Queue()  # coda messaggi da visualizzare
        self._monitor = MessageMonitor(self._widget, self._logs)

    def log(self, text):
        self._widget.IsShown() and self._logs.put(text)

    def reset(self):
        self._logs.queue.clear()

    def pause(self):
        self._monitor.pause()

    def start(self, text):
        self._logs.queue.clear()
        self._logs.put(text)
        if not self._monitor.is_alive():
            self._monitor = MessageMonitor(self._widget, self._logs)
            self._monitor.start()

    def stop(self):
        self._logs.queue.clear()
        self._monitor.stop()
        self._monitor.join()


class MessageLogger(object):
    """
    Gestisce i messaggi in arrivo dai server.
    """

    def __init__(self, parent):
        self._frm = FrmSrvMsg(parent)
        self._frm.Bind(wx.EVT_CLOSE, self.on_close)
        self._frm.btn_close.Bind(wx.EVT_BUTTON, self.on_close)
        self._frm.btn_pause.Bind(wx.EVT_BUTTON, self.on_pause)
        self._frm.btn_reset.Bind(wx.EVT_BUTTON, self.on_reset)
        self._frm.txt_messages.Bind(EVT_WX_SHOW_MSG, self.on_log_event)

        self._buffer = MessageBuffer()  # messaggi arrivati
        self._viewer = MessageViewer(self._frm.txt_messages)  # messaggi da visualizzare

    def on_close(self, event):
        self._viewer.stop()
        self._frm.Hide()

    def on_pause(self, event):
        self._viewer.pause()

    def on_reset(self, event):
        self._buffer.reset()
        self._viewer.reset()
        self._frm.txt_messages.SetValue('')

    def on_log_event(self, event):
        self._frm.txt_messages.AppendText(event.message)
        #wx.CallAfter(self._frm.txt_messages.AppendText, event.message)

    def close(self):
        self._frm.Close()

    def log(self, message):
        msg = message.strip('\r') + '\n'  # formatta
        self._buffer.log(msg)  # memorizza
        self._viewer.log(msg)  # visualizza

    def show(self):
        self._frm.Show()
        self._viewer.start(self._buffer.get())
