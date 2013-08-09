from settings import RUN_AT, INSTALLED_SERVERS

# Carica server
for server in INSTALLED_SERVERS:
    __import__(server)


from apscheduler.scheduler import Scheduler
from threading import Thread

from apps.userauth.controllers import user_auth

from apps.server import Server


class Importer(object):
    """ Importazione dai server
    """
    def __init__(self):
        self._sched = Scheduler()
        self._sched.start()
        self._servers = []
        for server in Server.get_servers():
            print 'Add %s server' % server.id_srv
            self._servers.append(server)
        print '\n'

    def schedule(self):
        # By default, no two instances of the same job will be run concurrently.
        self._sched.add_interval_job(self.execute, seconds=3)
        # self._sched.add_cron_job(self.execute,
        #                          day_of_week=RUN_AT['day_of_week'],
        #                          hour=RUN_AT['hour'],
        #                          minute=RUN_AT['minute'])

    def execute(self):
        for server in self._servers:
            # if user_auth.sever(server.id_srv):
            print '%s server is alive: %s' % (server.id_srv, server.isAlive())
            if not server.isAlive():
                print ' %s server start' % server.id_srv
                server.start()
        print '\n'

    def shutdown(self):
        self._sched.shutdown()


importer = Importer()
