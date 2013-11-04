import io
import threading
import wx

from Queue import Queue
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

    def clear(self):
        self._buffer.close()
        self._buffer .__init__()


class MessageViewer(object):
    """
    Gestisce la visualizzazione di messaggi su wx widget.
    I messaggi vengono inseriti in una coda.
    La coda viene evasa da un thread
     che per ogni messaggio invia evento wxShowMessageEvent a wx widget.
    """

    def __init__(self, widget):
        super(MessageViewer, self).__init__()
        self._widget = widget  # wx.TextCtrl interessato
        self._logs = Queue()  # coda messaggi da visualizzare
        self._running = True  # fine elaborazione coda messaggi
        self.pause = False  # pausa elaborazione coda messaggi
        self._monitor = self._get_monitor()  # settare prima running e pause

    def clear(self):
        """ Svuota coda messaggi """
        self._logs.queue.clear()

    def log(self, text):
        """ Inserisce messaggio in coda messaggi """
        self._logs.put(text)

    def start(self):
        """ Avvia elaborazione coda messaggi """
        self.pause = False
        self._running = True
        self._monitor = self._get_monitor()
        self._monitor.start()

    def stop(self):
        """ Termina elaborazione coda messaggi """
        if self._monitor.is_alive():
            self.pause = False
            self._running = False
            self._monitor.join()

    def _get_monitor(self):
        monitor = threading.Thread(target=self._run)
        monitor.daemon = True
        return monitor

    def _run(self):
        while self._running:
            if not self._logs.empty() and not self.pause:
                evt = wxShowMessageEvent(message=self._logs.get())
                wx.PostEvent(self._widget, evt)


class MessageLogger(object):
    """
    Gestisce i messaggi in arrivo dai importers.
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
        self._viewer.clear()
        self._viewer.stop()
        self._frm.Hide()

    def on_pause(self, event):
        self._viewer.pause = not self._viewer.pause  # pausa elaborazione coda messaggi
        self._frm.btn_reset.Disable() if self._viewer.pause else self._frm.btn_reset.Enable()

    def on_reset(self, event):
        self._buffer.clear()
        self._viewer.clear()
        self._frm.txt_messages.SetValue('')

    def on_log_event(self, event):
        try:
            self._frm.txt_messages.AppendText(event.message)
            #wx.CallAfter(self._frm.txt_messages.AppendText, event.message)
        except:
            pass

    def close(self):
        self._frm.Close()

    def log(self, message):
        msg = message.strip('\r') + '\n'  # formatta
        self._buffer.log(msg)  # memorizza
        self._frm.IsShown() and self._viewer.log(msg)  # visualizza

    def show(self):
        self._frm.Show()
        self._frm.txt_messages.SetValue(self._buffer.get())
        self._viewer.clear()
        self._viewer.start()
