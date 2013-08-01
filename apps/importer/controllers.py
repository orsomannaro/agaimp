from apscheduler.scheduler import Scheduler

from apps import userauth
from apps.userauth.controllers import user_auth

from . import models


class Importer(object):
    """ Importazione dai server
    """
    server_importers = {
        (userauth.ID_SRV_DELTA, models.DeltaServer),
        (userauth.ID_SRV_SIGMA, models.SigmaServer),
    }

    def __init__(self):
        self._sched = Scheduler()
        self._sched.start()

    def schedule(self):
        self._sched.add_interval_job(self.execute, seconds=3)

    def execute(self):
        for id_srv, server in self.server_importers:
            if user_auth.sever(id_srv):
                server().read()

    def shutdown(self):
        self._sched.shutdown()


importer = Importer()
