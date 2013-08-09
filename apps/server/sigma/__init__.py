from .. import Server


class SigmaServer(Server):
    def __init__(self):
        super(SigmaServer, self).__init__()
        self.id_srv = 'SIGMA'

    def run(self):
        import datetime
        import time

        self.publisher.write('*** SIGMA star import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        for i in range(8):
            time.sleep(1)
            sec = i+1
            self.publisher.write('SIGMA started since %s seconds.' % sec)
