import uuid


inst_uuid = str(uuid.uuid4())
file_name = 'param'
params = {}


def load_param():
    """ Carica params da file_name.
    """
    import json

    try:
        with open(file_name, 'r') as f:
            json_param = json.load(f)
            f.close()
        params = json.loads(json_param)
        return True
    except EnvironmentError:
        return False


def save_param():
    """ Salva params su file_name.
    """
    import json

    params['inst_uuid'] = inst_uuid
    json_param = json.dumps(params)
    try:
        with open(file_name, 'w') as f:
            json.dump(json_param, f)
    except EnvironmentError:
        return False


load_param() or save_param()

