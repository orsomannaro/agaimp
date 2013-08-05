from apps.importer import Server


class SigmaServer(Server):
    def __init__(self):
        super(SigmaServer, self).__init__()
        self.id_srv = 'sigma'

    def read(self):
        import datetime
        print 'SIGMA: star import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f")
