import wx


class DashboardForm(wx.Frame):
    def __init__(self, parent, title):
        super(DashboardForm, self).__init__(parent, title=title, size=(300, 200),
                                            style=wx.DEFAULT_DIALOG_STYLE)

        self.Centre()
        self.Show()



from .models import dashboards


def dashboard(request):
    dashboards_notices = []
    for dashboard in dashboards:
        try:
            # genera le notices per ogni dashboard registrato
            dashboards_notices.append({ 'name': dashboard.name,
                                        'notices': dashboard.get_notices(request)})
        except ValueError:
            continue

