# coding: latin-1

import time

from .. import Importer


ID_IMPORTER = 'sai_delta'  # importers ID su aGain


class DeltaImporter(Importer):

    name = ID_IMPORTER

    def __init__(self):
        super(DeltaImporter, self).__init__()

    def run(self):
        self.message.log('Inizio import')
        for i in range(1, 10):
            self.message.log('%s' % i)
            time.sleep(1)
        self.message.log('Fine import')
