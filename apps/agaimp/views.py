import wx

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


class ResetCancelDialog(wx.Dialog):
    """
    Crea una finestra di dialogo che visualizza:
     - un messaggio
     - due pulsanti: Annulla e Reset
    Ritorna:
     - 0 se e' stato premuto Annulla
     - 1 se e' stato premuto Reset
    """

    def __init__(self, *args, **kwargs):
        super(ResetCancelDialog, self).__init__(*args, **kwargs)

    def response(self, message):
        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, message)
        sizer.Add(label, 0, wx.ALIGN_CENTRE | wx.ALL, 5)

        btn_sizer = wx.StdDialogButtonSizer()

        btn = wx.Button(self, wx.ID_OK, label='Reset')
        btn_sizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL, label='Annulla')
        btn.SetDefault()
        btn_sizer.AddButton(btn)

        btn_sizer.Realize()  # sistema i pulsanti sul sizer

        sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
        self.CenterOnScreen()
        val = self.ShowModal()  # this does not return until the dialog is closed.
        self.Destroy()
        return 0 if val == wx.ID_CANCEL else 1
