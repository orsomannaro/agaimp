"""
I parametri vengono formattati in json e salvati in un file.

Si e' scelto di non tenere i parametri in memoria ma di leggerli da file alla bisogna.
Per questo motivo non li si e' gestiti con una classe.
"""

import uuid

from settings import PARAM_FILE


PARAM_PREFIX = 'param_'
UUID_PARAM = PARAM_PREFIX + 'uuid'  # identificativo dell'installazione
IP_DELTA_PARAM = PARAM_PREFIX + 'ip_delta'  # indirizzo IP del server DELTA
IP_SIGMA_PARAM = PARAM_PREFIX + 'ip_sigma'  # indirizzo IP del server SIGMA


class AgaimParam(object):
    PARAM_PREFIX = 'param_'
    UUID_PARAM = PARAM_PREFIX + 'uuid'  # identificativo dell'installazione
    IP_DELTA_PARAM = PARAM_PREFIX + 'ip_delta'  # indirizzo IP del server DELTA
    IP_SIGMA_PARAM = PARAM_PREFIX + 'ip_sigma'  # indirizzo IP del server SIGMA

    def __index__(self, file_name):
        self.file_name = file_name
        self._params = self.load() or self.init()

    def init(self):
        params = {
            self.UUID_PARAM: str(uuid.uuid4()),
            self.IP_DELTA_PARAM: '0.0.0.0',
            self.IP_SIGMA_PARAM: '0.0.0.0',
        }
        self.save(params)
        return params

    def load(self):
        import json

        try:
            with open(self.file_name, 'r') as f:
                json_param = json.load(f)
            params = json.loads(json_param)
        except:
            return {}
        return params

    def save(self, params):
        import json

        try:
            json_param = json.dumps(params)
            with open(self.file_name, 'w') as f:
                json.dump(json_param, f)
        except:
            #TODO: gestire eccezione
            raise

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, param, value):
        self._params[param] = value

def init_param():
    """ Creazione parametri.
    Inizializzazione dei parametri non editabili.
    """
    params = {UUID_PARAM: str(uuid.uuid4())}
    save_param(params)
    return params


def load_param():
    """ Carica i parametri.
    Se il parametri non esistono lo crea e inizializza.
    """
    import json

    try:
        with open(PARAM_FILE, 'r') as f:
            json_param = json.load(f)
        params = json.loads(json_param)
        return params
    except IOError:
        return init_param()  # Creazione parametri.


def save_param(params):
    """ Salva i parametri.
    :param params: dizionario contenete i parametri
    """
    import json

    try:
        json_param = json.dumps(params)
        with open(PARAM_FILE, 'w') as f:
            json.dump(json_param, f)
    except:
        raise
