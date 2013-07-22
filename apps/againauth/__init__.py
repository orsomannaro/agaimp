import requests

from apps.parameters import agaimparam
from settings import AGAIN_URL


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


def login():
    #req = requests.get(AGAIN_URL, auth=(agaimparam.usr, agaimparam.pwd))
    req = requests.get('https://github.com/orsomannaro', auth=('orsomannaro@gmail.com', 'lewis501'))
    return req.ok
