import wx


class DashboardForm(wx.Frame):
    def __init__(self, parent, title, name, notices):
        super(DashboardForm, self).__init__(parent, title=title, size=(300, 200),
                                            style=wx.DEFAULT_DIALOG_STYLE)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(name, 0, wx.ALL, 5)
        for message, action, auth in notices:
            self.sizer.Add(message, 0, wx.ALL, 5)
        self.SetSizer(self.sizer)
        self.Centre()
        self.Show()
