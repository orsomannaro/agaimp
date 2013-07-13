import os
import wx
import settings


TRAY_ICON = os.path.join(settings.IMAGES_DIR, 'trayicon.ico')
TRAY_TOOLTIP = 'aGain'


class TaskBarIcon(wx.TaskBarIcon):

    def __init__(self):
        super(TaskBarIcon, self).__init__()
        # set icon
        self.set_icon(TRAY_ICON)
        # bind some events
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
        # voci fisse del menu
        self.item_list = {}
        self.add_menu_item('Exit', self.on_exit)
        self.add_menu_item('Say Hello', self.on_hello)

    def CreatePopupMenu(self):
        """
        Al click-destro crea il menu in base
        al contenuto di self.item_list.
        E' quindi possibile aggiungere dinamicamente
        metodi e voci del menu.
        """
        menu = wx.Menu()
        for label, event in self.item_list.items():
            item = wx.MenuItem(menu, -1, label)
            menu.Bind(wx.EVT_MENU, event, id=item.GetId())
            menu.AppendItem(item)
        return menu

    def add_menu_item(self, label, func):
        self.item_list[label] = func

    def set_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):
        print 'Tray icon was left-clicked.'

    def on_hello(self, event):
        print 'Hello, world!'

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
