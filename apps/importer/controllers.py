from apscheduler.scheduler import Scheduler

from settings import RUN_AT

from apps.userauth.controllers import user_auth

from . import Server


class Importer(object):
    """ Importazione dai server
    """
    def __init__(self):
        self._sched = Scheduler()
        self._sched.start()

    def schedule(self):
        self._sched.add_interval_job(self.execute, seconds=3)
        self._sched.add_cron_job(self.execute,
                                 day_of_week=RUN_AT['day_of_week'],
                                 hour=RUN_AT['hour'],
                                 minute=RUN_AT['minute'])

    def execute(self):
        for server in Server.get_servers():
            if user_auth.sever(server.id_srv):
                server.read()

    def shutdown(self):
        self._sched.shutdown()
