import requests

from settings import AGAIN_URL

from apps.parameters.views import get_uuid


def authenticate(func):
    """
    Decorator for methods, which require authentication.
    """
    def authenticate_and_call(*args, **kwargs):
        if not login():
            raise Exception('Authentication Failed.')
        #print 'autentificato'
        return func(*args, **kwargs)
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
    usr = get_uuid()
    pwd = get_pwd(usr)
    req = requests.get(AGAIN_URL, auth=(usr, pwd))  # requests.get('https://github.com/nome_utente', auth=('nome_utente', 'pwd'))
    user_auth = {}
    return user_auth
