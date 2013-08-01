

class Server(object):
    """ Interfaccia standard di un server """
    def __init__(self):
        pass

    def connect(self):
        """ Stabilisce una connessione con il server """
        pass

    def read(self):
        """ Legge i dati dal server """
        pass


class DeltaServer(Server):
    """ Server SIGMA """
    def __init__(self):
        super(DeltaServer, self).__init__()

    def read(self):
        import datetime
        print 'DELTA: star import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f")


class SigmaServer(Server):
    """ Server SIGMA """
    def __init__(self):
        super(SigmaServer, self).__init__()

    def read(self):
        import datetime
        print 'SIGMA: star import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f")
