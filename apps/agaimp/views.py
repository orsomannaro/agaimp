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


class ResetCloseDialog(wx.Frame):
    """
    Crea una finestra di dialogo che visualizza:
     - un messaggio
     - due pulsanti: Annulla e Reset
    Ritorna:
     - 0 se e' stato premuto Annulla
     - 1 se e' stato premuto Reset
    """

    def __init__(self):
        wx.Frame.__init__(self, None, - 1, "My Frame", size=(600, 600))
        panel = wx.Panel(self, - 1)
        button = wx.Button(panel, label="Add button", pos=wx.DefaultPosition,
                           size=wx.DefaultSize)
        self.Bind(wx.EVT_BUTTON, self.OnAddButton, button)

        self.scrolledPanel = scrolled.ScrolledPanel(panel, - 1,
                                                    size=wx.DefaultSize)
        self.scrollPanelSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.scrolledPanel.SetSizer(self.scrollPanelSizer)
        self.scrollPanelSizer.Fit(self)

        self.scrolledPanel.SetupScrolling(scroll_x=True, scroll_y=False)
        self.FitInside()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button)
        sizer.Add(self.scrolledPanel)
        panel.SetSizer(sizer)
        panel.Fit()

    def OnAddButton(self, event):
        self.buttonCount = self.buttonCount + 1
        print "Add button clicked: ", self.buttonCount
        button = wx.Button(self.scrolledPanel,
                           label="Button " + str(self.buttonCount),
                           pos=(0, 0), size=wx.DefaultSize)

        self.scrollPanelSizer.Add(button, 0, wx.ALL, 1)
        self.scrollPanelSizer.Fit(self.scrolledPanel)
        self.SetSizer(self.scrollPanelSizer)
        self.scrolledPanel.SetupScrolling(scroll_x=True, scroll_y=False)
        self.scrolledPanel.FitInside()


    def response(self, message):

        # Sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # ScrolledPanel
        scrl_pnl = scrolled.ScrolledPanel(self, -1, size=(500, 300),
                                 style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="scrl_pnl" )

        label = wx.StaticText(scrl_pnl, -1, message)
        msgbox = wx.BoxSizer(wx.VERTICAL)
        msgbox.Add(label, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        scrl_pnl.SetSizer(msgbox)
        scrl_pnl.SetAutoLayout(1)
        scrl_pnl.SetupScrolling()

        sizer.Add(scrl_pnl, 0, wx.ALIGN_CENTRE | wx.ALL, 5)

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
        val = self.Show()  # this does not return until the dialog is closed.
        self.Destroy()
        return 0 if val == wx.ID_CANCEL else 1
