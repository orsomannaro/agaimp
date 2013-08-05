import wx


class SystrayApp(wx.TaskBarIcon):
    """
    App sulla barra delle notifiche.
    """
    def __init__(self, icon, tooltip, frame=None):
        wx.TaskBarIcon.__init__(self)
        self.menu = []
        self.set_icon(icon, tooltip)
        self.frame = wx.Frame(None)  # serve su OSX altrimenti MainLoop termina

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

    def _get_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        return icon

    def add_menu_item(self, label, func):
        """
        Aggiunge una voce al menu' associandola alla relativa funzione.
        """
        self.menu.append((label, func))

    def exit(self):
        """ Chiusura app.
        """
        self.frame.Destroy()
        wx.CallAfter(self.Destroy)

    def set_icon(self, icon, tooltip):
        """ Imposta icona e tooltip.
        :param icon: full path icona
        """
        path = self._get_icon(icon)
        try:
            self.SetIcon(path, tooltip)
        except:
            raise
