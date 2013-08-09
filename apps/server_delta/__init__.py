from apps.server import Server


class DeltaServer(Server):
    def __init__(self):
        super(DeltaServer, self).__init__()
        self.id_srv = 'delta'

    def run(self):
        import datetime
        import time

        self.send_message('DELTA: star import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        for i in range(5):
            time.sleep(1)
            sec = i+1
            self.send_message('Time since DELTA started: %s seconds.' % sec)
