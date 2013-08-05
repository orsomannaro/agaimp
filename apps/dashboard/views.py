from .forms import DashboardForm
from .models import Dashboard


def dashboard_view():
    dashboards_notices = []
    for dashboard in Dashboard.get_dashboards():
        try:
            # genera le notices per ogni dashboard registrato
            dashboards_notices.append({
                'name': dashboard.name,
                'notices': dashboard.get_notices()
            })
        except ValueError:
            continue
