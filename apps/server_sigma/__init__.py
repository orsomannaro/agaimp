from apps.agaimp.server import wxServer


class SigmaServer(wxServer):
    def __init__(self):
        super(SigmaServer, self).__init__()
        self.id_srv = 'sigma'

    def run(self):
        import datetime
        import time

        self.send_message('SIGMA: star import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        for i in range(5):
            time.sleep(1)
            sec = i+1
            self.send_message('Time since SIGMA started: %s seconds.' % sec)
