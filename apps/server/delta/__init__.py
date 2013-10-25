# coding: latin-1

from .. import Server
from time import sleep


class DeltaServer(Server):
    def __init__(self):
        super(DeltaServer, self).__init__()
        self.id_srv = 'DELTA'

    def run(self):
        sleep(3)
        self.message('start import')
        for i in range(1, 100):
            if i % 2 == 0:
                self.warning('%s' % i)
            else:
                self.error('%s' % i)
            sleep(1)
