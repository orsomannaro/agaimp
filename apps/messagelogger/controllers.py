import wx

from Queue import Queue
from threading import Thread
from wx.lib.newevent import NewEvent

from gui.agaimp_gui import FrmSrvMsg

from .models import MessageBuffer


wxShowMessageEvent, EVT_WX_SHOW_MSG = wx.lib.newevent.NewEvent()


class MessageLogger(object):
    """ Gestisce i messaggi in arrivo dal server.
    """

    def __init__(self, parent):
        self._frm = FrmSrvMsg(parent)
        self._frm.btn_close.Bind(wx.EVT_BUTTON, self.on_close)
        self._frm.btn_pause.Bind(wx.EVT_BUTTON, self.on_pause)
        self._frm.btn_reset.Bind(wx.EVT_BUTTON, self.on_reset)
        self._frm.txt_messages.Bind(EVT_WX_SHOW_MSG, self.on_log_event)

        self._log = MessageBuffer()  # messaggi arrivati
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
