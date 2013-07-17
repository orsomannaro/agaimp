import wx
import settings


class TaskBarIcon(wx.TaskBarIcon):
    """
    Menu sulla barra delle notifiche.
    """
    def __init__(self):
        super(TaskBarIcon, self).__init__()
        # set icon
        self.set_icon(settings.TRAY_ICON)

        # bind wx.taskbarapp events
        # self.Bind(wx.EVT_TASKBAR_CLICK, self.on_click)
        # self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.on_left_dclick)
        # self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
        # self.Bind(wx.EVT_TASKBAR_LEFT_UP, self.on_left_up)
        # self.Bind(wx.EVT_TASKBAR_MOVE, self.on_move)
        # self.Bind(wx.EVT_TASKBAR_RIGHT_DCLICK, self.on_right_dclick)
        # self.Bind(wx.EVT_TASKBAR_RIGHT_DOWN, self.on_right_down)
        # self.Bind(wx.EVT_TASKBAR_RIGHT_UP, self.on_right_up)

        # voci fisse del menu
        self.menu_items = []
        self.add_menu_item('Exit', self.on_exit)

    def CreatePopupMenu(self):
        """
        Al click-destro crea il menu in base al contenuto di self.menu_items.
        E' quindi possibile aggiungere dinamicamente metodi e voci del menu.
        """
        menu = wx.Menu()
        for label, func in reversed(self.menu_items):
            item = wx.MenuItem(menu, -1, label)
            menu.Bind(wx.EVT_MENU, func, id=item.GetId())
            menu.AppendItem(item)
        return menu

    def add_menu_item(self, label, func):
        self.menu_items.append((label, func))

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)

    def set_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, settings.TRAY_TOOLTIP)


taskbarapp = TaskBarIcon()