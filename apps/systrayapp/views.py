import wx


class SystrayApp(wx.TaskBarIcon):
    """
    App sulla barra delle notifiche.
    """
    def __init__(self, path, tooltip, frame=None):
        wx.TaskBarIcon.__init__(self)
        self.frame = wx.Frame(None)  # serve su OSX altrimenti MainLoop termina
        self.set_icon(path, tooltip)
        self.menu = []

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

    def OnExit(self, event):
        self.frame.Destroy()
        wx.CallAfter(self.Destroy)

    def _get_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        return icon

    def add_menu_item(self, label, func):
        self.menu.append((label, func))

    def set_icon(self, path, tooltip):
        icon = self._get_icon(path)
        self.SetIcon(icon, tooltip)
