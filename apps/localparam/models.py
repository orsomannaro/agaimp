"""
Gestione dei parametri LOCAL_PARAMETERS su file in formato json.
"""

from . import LOCAL_PARAMETERS
from .views import aGaiMpFrmSettings


class LocalParam(object):
    """ Parametri locali """
    def __init__(self, file_name):
        self.file = file_name  # full path
        self.params = LOCAL_PARAMETERS  # parametri di default
        self.load()

    def edit(self):
        aGaiMpFrmSettings(None, self)

    def load(self):
        """ Carica i parametri dal file """
        import json

        try:
            with open(self.file, 'r') as f:
                json_param = json.load(f)
            self.params = json.loads(json_param)
        except IOError:
            self.save()  # crea il file se non esiste

    def save(self):
        """ Salva i parametri sul file """
        import json

        try:
            json_param = json.dumps(self.params)
            with open(self.file, 'w') as f:
                json.dump(json_param, f)
        except IOError:
            raise
