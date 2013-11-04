import os
import wx


def get_wx_icon(full_path):
    file_ext = os.path.splitext(full_path)[1]
    if file_ext == '.ico':
        icon = wx.Icon(full_path, wx.BITMAP_TYPE_ICO)
        return icon
    elif file_ext == '.png':
        icon = wx.Icon(full_path, wx.BITMAP_TYPE_PNG)
        return icon
    raise NotImplementedError('Unknown icon type')


class SystrayApp(wx.TaskBarIcon):
    """
    App sulla barra delle notifiche.
    """
    def __init__(self, icon, tooltip, menu, frame=None):
        wx.TaskBarIcon.__init__(self)
        self.frame = wx.Frame(None)  # serve su OSX altrimenti MainLoop termina
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnLeftClick)

        self.menu = menu
        self._current_icon = ''
        self.icon(icon, tooltip)

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

    def icon(self, icon_file, icon_tooltip):
        """ Imposta icona e tooltip """
        if self._current_icon != icon_file:
            try:
                icon = get_wx_icon(icon_file)
                self.SetIcon(icon, icon_tooltip)
            except:
                raise
            else:
                self._current_icon = icon_file
