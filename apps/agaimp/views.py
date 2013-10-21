import wx
import threading
import Queue

from wx.lib.newevent import NewEvent

myNewMsg, EVT_NEW_MSG = NewEvent()  # ci sono messaggi da visualizzare


from gui.agaimp_gui import frm_srv_msg

from libs.wx_utils import get_wx_icon, wx_call


class SystrayApp(wx.TaskBarIcon):
    """
    App sulla barra delle notifiche.
    """

    def __init__(self, icon, tooltip, menu, frame=None):
        wx.TaskBarIcon.__init__(self)
        self.menu = menu
        self.set_icon(icon, tooltip)
        self.frame = wx.Frame(None)  # serve su OSX altrimenti MainLoop termina
        # event handlers
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnLeftClick)

    def CreatePopupMenu(self):
        """
        Al click-destro crea il menu in base al contenuto di self.menu.
        E' quindi possibile aggiungere dinamicamente metodi e voci del menu.
        """
        menu = wx.Menu()
        for label, func in reversed(self.menu):
            item = wx.MenuItem(menu, -1, label)
            menu.Bind(wx.EVT_MENU, func, id=item.GetId())
            menu.AppendItem(item)
        return menu

    def OnClose(self, event):
        self.close()

    def OnLeftClick(self, event):
        pass

    def close(self):
        self.frame.Destroy()
        wx.CallAfter(self.Destroy)

    def set_icon(self, icon_file, icon_tooltip):
        """ Imposta icona e tooltip.
        """
        try:
            icon = get_wx_icon(icon_file)
            self.SetIcon(icon, icon_tooltip)
        except:
            raise


class aGaiMpMessages(frm_srv_msg):
    """ Subclass of frm_srv_msg, which is generated by wxFormBuilder.
    """
    def __init__(self, parent, messages):
        frm_srv_msg.__init__(self, parent)

        self._messages = messages
        self.Show()  # NB: dopo l'inizializzazione del timer

    def OnClose(self, event):
        #self.tmr_txt_messages.Stop()
        self.Close()

    def OnReset(self, event):
        self._messages.reset()
        self.txt_messages.Clear()

    def OnShow(self, event):
        """ Mostra i messaggi.
        """
        if event.Show:
            message = u'%s' % self._messages.getvalue()
            self.txt_messages.SetValue(message)
            print '1'

    def update(self):
        message = u'%s' % self._messages.getvalue()
        self.txt_messages.SetValue(message)
        print '2'
