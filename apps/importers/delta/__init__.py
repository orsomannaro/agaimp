# coding: latin-1

import time

from .. import Importer, messenger


ID_IMPORTER = 'sai_delta'  # importers ID su aGain


class DeltaImporter(Importer):

    name = ID_IMPORTER

    def __init__(self):
        super(DeltaImporter, self).__init__()

    def run(self):
        messenger.log(self.name, 'Inizio import')
        for i in range(1, 10):
            messenger.log(self.name, '%s' % i)
            time.sleep(1)
        messenger.log(self.name, 'Fine import')
