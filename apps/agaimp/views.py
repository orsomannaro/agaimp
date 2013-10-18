import wx
import wx.lib.scrolledpanel as scrolled

from libs.wx_utils import get_wx_icon


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


class ResetCloseDialog(wx.Dialog):
    """
    Crea una finestra di dialogo che visualizza:
     - un messaggio
     - due pulsanti: Annulla e Reset
    Ritorna:
     - 0 se e' stato premuto Annulla
     - 1 se e' stato premuto Reset
    """

    def __init__(self, *args, **kwargs):
        super(ResetCloseDialog, self).__init__(*args, **kwargs)

    def response(self, message):

        # Sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # ScrolledPanel
        panel = scrolled.ScrolledPanel(self, -1, size=(500, 300),
                                 style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="panel" )

        label = wx.StaticText(panel, -1, message)
        msgbox = wx.BoxSizer(wx.VERTICAL)
        msgbox.Add(label, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        panel.SetSizer(msgbox)
        panel.SetAutoLayout(1)
        panel.SetupScrolling()

        sizer.Add(panel, 0, wx.ALIGN_CENTRE | wx.ALL, 5)

        #label = wx.StaticText(self, -1, message)
        #sizer.Add(label, 0, wx.ALIGN_CENTRE | wx.ALL, 5)

        # Linea divisione
        #line = wx.StaticLine(self, -1, size=(20, -1), style=wx.LI_HORIZONTAL)
        #sizer.Add(line, 0, wx.GROW | wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.TOP, 5)

        # Pulsanti
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self, wx.ID_OK, label='Reset')
        btn.SetToolTip(wx.ToolTip('Cancella tutti i messaggi'))
        btn_sizer.Add(btn)

        btn_sizer.Add((0, 0), 1, wx.EXPAND)

        btn = wx.Button(self, wx.ID_CANCEL, label='Chiudi')
        btn.SetDefault()
        btn_sizer.Add(btn)

        sizer.Add(btn_sizer, flag=wx.ALL | wx.EXPAND)

        self.SetSizer(sizer)
        sizer.Fit(self)
        self.CenterOnScreen()
        val = self.ShowModal()  # this does not return until the dialog is closed.
        self.Destroy()
        return 0 if val == wx.ID_CANCEL else 1
