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
