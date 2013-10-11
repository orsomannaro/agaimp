"""
Gestione dei parametri su <file_name>.

Creazione, caricamento e salvataggio in formato json.
Ogni parametro e' leggibile e aggiornabile come proprieta'.

In fase di istanziamento i parametri vengono letti/creati e poi conservati in memoria.
La lettura e scrittura su disco e' effettuabile con i metodi 'load' e 'save'.

Per l'editing a mezzo form la convenzione e' di utilizzare per i nomi
dei controlli associati ai parametri, le relative costanti PARAM_.
"""

import os
import uuid

from . import PARAM_UUID, PARAM_IP_DELTA, PARAM_IP_SIGMA
from .views import EditParamsView


class LocalParam(object):
    """ Parametri locali
    """
    def __init__(self, file_name):
        self.file = file_name  # full path
        self._params = {}  # parametri
        if not os.path.isfile(self.file):
            self.reset()
            self.save()
        else:
            self.load()

    def reset(self):
        """ Inizializza e crea i parametri """
        self._params = {
            PARAM_UUID: str(uuid.uuid4()),
            PARAM_IP_DELTA: '0.0.0.0',
            PARAM_IP_SIGMA: '0.0.0.0',
        }

    def edit(self):
        EditParamsView(self)

    def load(self):
        """ Carica i parametri dal file """
        import json

        try:
            with open(self.file, 'r') as f:
                json_param = json.load(f)
            self._params = json.loads(json_param)
        except:
            raise

    def save(self):
        """ Salva i parametri sul file """
        import json

        try:
            json_param = json.dumps(self._params)
            with open(self.file, 'w') as f:
                json.dump(json_param, f)
        except:
            raise

    @property
    def param_uuid(self):
        return self._params[PARAM_UUID]

    @param_uuid.setter
    def param_uuid(self, value):
        self._params[PARAM_UUID] = value

    @property
    def param_ip_delta(self):
        return self._params[PARAM_IP_DELTA]

    @param_ip_delta.setter
    def param_ip_delta(self, value):
        self._params[PARAM_IP_DELTA] = value

    @property
    def param_ip_sigma(self):
        return self._params[PARAM_IP_SIGMA]

    @param_ip_sigma.setter
    def param_ip_sigma(self, value):
        self._params[PARAM_IP_SIGMA] = value

    def params(self):
        return self._params
