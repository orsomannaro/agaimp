import uuid

from settings import PARAM_FILE


def init_param():
    """ Inizializzazione parametri.
    Impostazione dei parametri non editabili.
    """
    params = {'param_uuid': str(uuid.uuid4())}  # identificativo dell'installazione
    save_param(params)
    return params


def load_param():
    """ Carica parametri da file.
    Se il file se non esiste richiede l'inizializzazione dei parametri.
    """
    try:
        import json

        with open(PARAM_FILE, 'r') as f:
            json_param = json.load(f)
        params = json.loads(json_param)
        return params
    except IOError:
        return init_param()  # Creazione parametri.


def save_param(params):
    """ Salva parametri su file.
    :param params: dizionario contenete i parametri
    """
    try:
        import json

        json_param = json.dumps(params)
        with open(PARAM_FILE, 'w') as f:
            json.dump(json_param, f)
    except:
        raise
