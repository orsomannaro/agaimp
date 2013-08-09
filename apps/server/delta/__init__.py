from .. import Server


class DeltaServer(Server):
    def __init__(self):
        super(DeltaServer, self).__init__()
        self.id_srv = 'DELTA'

    def run(self):
        import datetime
        import time

        self.publisher.write('*** DELTA start import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        for i in range(5):
            time.sleep(1)
            sec = i+1
            self.publisher.write('DELTA started since %s seconds.' % sec)
