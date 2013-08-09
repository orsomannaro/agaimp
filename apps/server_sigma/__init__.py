from apps.server import Server


class SigmaServer(Server):
    def __init__(self):
        super(SigmaServer, self).__init__()
        self.id_srv = 'sigma'

    def run(self):
        import datetime
        import time

        self.send_message('SIGMA: star import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        for i in range(8):
            time.sleep(1)
            sec = i+1
            self.send_message('Time since SIGMA started: %s seconds.' % sec)
