# coding: latin-1

from .. import Server

from ..publisher import SRV_NAME, SRV_MSG_LVL, SRV_MSG_HMS, SRV_MSG_TXT, \
                        LOG_SRV_MSG_LVL, WRN_SRV_MSG_LVL, ERR_SRV_MSG_LVL


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
            SRV_MSG_HMS: datetime.datetime.now().strftime("%H:%M:%S"),
            SRV_MSG_TXT: 'start import',
            })
        for i in range(8):
            time.sleep(1)
            sec = i+1
            if i==5:
                # simulazione errore
                self.publisher.publish({
                    SRV_NAME: self.id_srv,
                    SRV_MSG_LVL: ERR_SRV_MSG_LVL,
                    SRV_MSG_HMS: datetime.datetime.now().strftime("%H:%M:%S"),
                    SRV_MSG_TXT: u'Questo è un messaggio di errore',
                })
            else:
                self.publisher.publish({
                    SRV_NAME: self.id_srv,
                    SRV_MSG_LVL: ERR_SRV_MSG_LVL,
                    SRV_MSG_HMS: datetime.datetime.now().strftime("%H:%M:%S"),
                    SRV_MSG_TXT: u'started since %s seconds' % sec,
                })
