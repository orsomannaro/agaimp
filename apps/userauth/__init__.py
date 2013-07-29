import requests

from settings import AGAIN_URL

from apps.localparam import params


DELTA_AUTH = 'delta_auth'
SIGMA_AUTH = 'sigma_auth'


def authenticate(func):
    """
    Decorator for methods, which require authentication.
    """
    def authenticate_and_call(*args, **kwargs):
        if login():
            return func(*args, **kwargs)
        raise Exception
    return authenticate_and_call


def get_pwd(usr):
    """
    Calcola la password in base all'uuid dell'installazione.
    :param usr: uuid dell'installazione
    :return: password
    """
    import hashlib
    return str(hashlib.sha1(usr).hexdigest())


def login():
    """
    Effettua il login alla web-app.
    :return: dizionario delle autorizzazioni dell'utente.
    """
    global user_auth

    usr = params.param_uuid
    pwd = get_pwd(usr)
    #req = requests.get(AGAIN_URL, auth=(usr, pwd), timeout = 5)
    req = requests.get('https://api.github.com/', auth=('orsomannaro@gmail.com', 'lewis501'))
    if req.ok:
        # Recupero dalla web-app il dizionario con autorizzazioni dell'utente
        #user_auth = req.json()
        user_auth = {SIGMA_AUTH: True}
    return req.ok


@authenticate
def server(server_auth):
    """
    Verifica l'autorizzazione ad importare dal server SIGMA
    :param server_auth:
    """
    def chk_server_auth(func):
        def chk_srv(*args, **kwargs):
            return func(*args, **kwargs) if server_auth in user_auth and user_auth[server_auth] else False
        return chk_srv
    return chk_server_auth


user_auth = {}
