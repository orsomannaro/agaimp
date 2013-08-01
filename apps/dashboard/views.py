import wx


class DashboardForm(wx.Frame):
    def __init__(self, parent, title):
        super(DashboardForm, self).__init__(parent, title=title, size=(300, 200),
                                            style=wx.DEFAULT_DIALOG_STYLE)

        self.Centre()
        self.Show()
