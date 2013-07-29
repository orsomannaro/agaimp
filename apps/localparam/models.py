"""
I parametri vengono formattati in json e salvati in un file.
"""

import os
import uuid


class LocalParam(object):
    """ Parametri locali.
    """
    PARAM_UUID = 'param_uuid'  # identificativo dell'installazione
    PARAM_IP_DELTA = 'param_ip_delta'  # indirizzo IP del server DELTA
    PARAM_IP_SIGMA = 'param_ip_sigma'  # indirizzo IP del server SIGMA

    def __init__(self, file_name):
        self.file_name = file_name
        if not os.path.isfile(self.file_name):
            self.create()
            self.save()
        else:
            self.load()

    def create(self):
        """ Inizializza e crea i parametri.
        """
        self.params = {
            self.PARAM_UUID: str(uuid.uuid4()),
            self.PARAM_IP_DELTA: '0.0.0.0',
            self.PARAM_IP_SIGMA: '0.0.0.0',
        }

    def load(self):
        """ Carica i parametri dal file.
        """
        import json

        try:
            with open(self.file_name, 'r') as f:
                json_param = json.load(f)
            self.params = json.loads(json_param)
        except:
            #TODO: gestire eccezione
            raise

    def save(self):
        """ Salva i parametri sul file.
        """
        import json

        try:
            json_param = json.dumps(self.params)
            with open(self.file_name, 'w') as f:
                json.dump(json_param, f)
        except:
            #TODO: gestire eccezione
            raise

    @property
    def param_uuid(self):
        return self.params[self.PARAM_UUID]

    @param_uuid.setter
    def param_uuid(self, value):
        self.params[self.PARAM_UUID] = value

    @property
    def param_ip_delta(self):
        return self.params[self.PARAM_IP_DELTA]

    @param_ip_delta.setter
    def param_ip_delta(self, value):
        self.params[self.PARAM_IP_DELTA] = value

    @property
    def param_ip_sigma(self):
        return self.params[self.PARAM_IP_SIGMA]

    @param_ip_sigma.setter
    def param_ip_sigma(self, value):
        self.params[self.PARAM_IP_SIGMA] = value
