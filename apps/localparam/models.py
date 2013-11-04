"""
Gestione dei parametri LOCAL_PARAMETERS su file in formato json.
"""


class LocalParam(object):
    """ Parametri locali """
    def __init__(self, file_name, default_params):
        self.file = file_name  # full path
        self.params = default_params  # parametri di default
        self.load()

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
