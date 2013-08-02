from apps.importer.models import Server


class DeltaServer(Server):
    def __init__(self):
        super(DeltaServer, self).__init__()
        self.id_srv = 'delta'

    def read(self):
        import datetime
        print 'DELTA: star import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f")
