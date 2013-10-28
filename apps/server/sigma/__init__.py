# coding: latin-1

from .. import Server
from time import sleep


ID_SERVER = 'SIGMA'  # server ID su aGain


class SigmaServer(Server):

    def __init__(self):
        super(SigmaServer, self).__init__(ID_SERVER)

    def run(self):
        sleep(3)
        self.message.log('start import')
        for i in range(1, 100):
            if i % 2 == 0:
                self.message.warning('%s' % i)
            else:
                self.message.error('%s' % i)
            sleep(1)
