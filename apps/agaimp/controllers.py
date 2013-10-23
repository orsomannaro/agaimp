import wx

from wx.lib.newevent import NewEvent

from gui.agaimp_gui import frm_srv_msg

from settings import TRAY_ICON, TRAY_TOOLTIP, TRAY_ICON_WRN, TRAY_ICON_ERR

from .views import SystrayApp


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


wxShowMessageEvent, EVT_WX_SHOW_MSG = wx.lib.newevent.NewEvent()

class aGaiMpMessages(object):
    """ Gestisce la visualizzazione dei massaggi in arrivo dal server.
    """

    def __init__(self, parent):
        # TODO: mettere in camel case il nome della classe frm_srv_msg
        self._frm = frm_srv_msg(parent)
        self._frm.btn_reset.Bind(wx.EVT_BUTTON, self.on_reset)
        self._frm.btn_close.Bind(wx.EVT_BUTTON, self.on_close)
        self._frm.txt_messages.Bind(EVT_WX_SHOW_MSG, self.on_log_event)

    def on_close(self, event):
        self._frm.Hide()

    def on_reset(self, event):
        pass

    def on_log_event(self, event):
        if self._frm.IsShown():
            msg = event.message.strip('\r')+'\n'
            self._frm.txt_messages.AppendText(msg)
            #wx.CallAfter(self.txt_messages.AppendText, msg)
            event.Skip()

    def close(self):
        self._frm.Close()

    def log(self, message):
        evt = wxShowMessageEvent(message=message)
        wx.PostEvent(self._frm.txt_messages, evt)

    def show(self):
        self._frm.Show()
