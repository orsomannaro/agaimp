"""
Gestione dei parametri LOCAL_PARAMETERS su file in formato json.

Istanziando un oggetto LocalParam i parametri sono disponibili
 come dizionario tramite il suo attributo 'params'.

"""

import json


class LocalParam(object):
    """ Parametri locali """
    def __init__(self, file_path, default_params):
        self._file = file_path  # full path
        self.params = default_params  # parametri di default
        self.load()

    def load(self):
        """ Carica i parametri dal file """
        try:
            with open(self._file) as f:
                json_param = json.load(f)
            self.params = json.loads(json_param)
        except IOError:  # il file se non esiste
            self.save()  # crea parametri di default

    def save(self):
        """ Salva i parametri sul file """
        try:
            json_param = json.dumps(self.params)
            with open(self._file, 'w') as f:
                json.dump(json_param, f)
        except IOError:
            raise
