# coding: latin-1

import time

from .. import Server


ID_SERVER = 'sai_sigma'  # server ID su aGain


class SigmaServer(Server):

    def __init__(self):
        super(SigmaServer, self).__init__(ID_SERVER)

    def run(self):
        self.message.log('Inizio import')
        for i in range(1, 10):
            self.message.log('%s' % i)
            time.sleep(1)
        self.message.log('Fine import')
