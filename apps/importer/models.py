import datetime

from apscheduler.scheduler import Scheduler

from apps.userauth import server_auth, SIGMA_AUTH


class Importer(object):
    def __init__(self):
        self.scheduler = Scheduler()

    def add(self, funct, **kargs):
        self.scheduler.add_interval_job(funct, **kargs)

    def shutdown(self):
        """ Termina importer """
        self.scheduler.shutdown()

    def start(self):
        """ Avvia importer """
        self.scheduler.start()

    def stop(self, name='all'):
        """ Ferma importer
        :param name: nome server da fermare (all=tutti i server)
        """
        for job in self.scheduler.get_jobs():
            if name=='all' or job.name == name:
                self.scheduler.unschedule_job(job)


class Server(object):
    """
    Interfaccia standard di un server.
    """
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def connect(self):
        """ Stabilisce una connessione con il server
        """
        pass

    def read(self):
        """ Legge i dati dal server
        """
        pass


class SigmaServer(Server):
    """
    Server SIGMA.
    """
    #@server_auth(SIGMA_AUTH)
    def __init__(self, ip_address):
        super(SigmaServer, self).__init__()
        self.ip = ip_address

    def read(self):
        print 'SIGMA: star import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f")
