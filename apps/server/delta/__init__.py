# coding: latin-1

from .. import Server
from time import sleep


ID_SERVER = 'DELTA'  # server ID su aGain
DATA_FILE = 'delta.dat'


class DeltaServer(Server):

    def __init__(self):
        super(DeltaServer, self).__init__(ID_SERVER)

    def run(self):
        self.message.log('Inizio import')
        for i in range(1, 10):
            if i % 2 == 0:
                self.message.warning('%s' % i)
            else:
                self.message.error('%s' % i)
            sleep(1)
        self.message.log('Fine import')
