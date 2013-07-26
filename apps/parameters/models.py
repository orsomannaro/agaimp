import uuid

from settings import PARAM_FILE


def load_param():
    """ Carica parametri da file.
    """
    import json

    try:
        with open(PARAM_FILE, 'r') as f:
            json_param = json.load(f)
        params = json.loads(json_param)
        return params
    except:
        raise


def save_param(params):
    """ Salva parametri su file.
    :param params: dizionario contenete i parametri
    """
    import json

    if not 'param_uuid' in params:
        params['param_uuid'] = str(uuid.uuid4())  # primo salvataggio
    json_param = json.dumps(params)
    try:
        with open(PARAM_FILE, 'w') as f:
            json.dump(json_param, f)
    except:
        raise
