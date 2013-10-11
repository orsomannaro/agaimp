from .. import Server

from ..publisher import SRV_NAME, SRV_MSG_LVL, SRV_MSG_TXT, LOG_SRV_MSG_LVL, WRN_SRV_MSG_LVL, ERR_SRV_MSG_LVL


class SigmaServer(Server):
    def __init__(self):
        super(SigmaServer, self).__init__()
        self.id_srv = 'SIGMA'

    def run(self):
        import datetime
        import time

        self.publisher.publish({
            SRV_NAME: self.id_srv,
            SRV_MSG_LVL: LOG_SRV_MSG_LVL,
            SRV_MSG_TXT: 'start import at ' + datetime.datetime.now().strftime("%H:%M:%S.%f"),
            })
        for i in range(8):
            time.sleep(1)
            sec = i+1
            self.publisher.publish({
                SRV_NAME: self.id_srv,
                SRV_MSG_LVL: LOG_SRV_MSG_LVL,
                SRV_MSG_TXT: 'started since %s seconds' % sec,
            })
