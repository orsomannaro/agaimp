from apscheduler.scheduler import Scheduler

from .models import servers
from apps.userauth.controllers import user_auth


class Importer(object):
    """ Importazione dai server
    """
    def __init__(self):
        self._sched = Scheduler()
        self._sched.start()

    def schedule(self):
        self._sched.add_interval_job(self.execute, seconds=3)

    def execute(self):
        for server in servers:
            if user_auth.sever(server.id_srv):
                server.read()

    def shutdown(self):
        self._sched.shutdown()


importer = Importer()
