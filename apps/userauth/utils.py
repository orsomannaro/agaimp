import pycurl

from settings import AGAIN_URL
from apps.parameters import agaimparam

from .models import Account


def getUserData():
    """
    Legge i dati dell'utente da aGain.
    """
    c = pycurl.Curl()
    c.setopt(pycurl.URL, AGAIN_URL)
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
    c.setopt(pycurl.VERBOSE, 0)
    c.setopt(pycurl.USERPWD, '%s:%s' % (agaimparam.usr(),agaimparam.pwd()))
    c.perform()


def authenticate(func):
    """
    Decorator for methods, which require authentication.
    """

    def authenticate_and_call(*args, **kwargs):
        if not Account.is_authenticated:
            raise Exception('Authentication Failed.')
        return func(*args, **kwargs)
    return authenticate_and_call


===========================================================
http://www.dmclaughlin.com/2011/04/14/ssl-client-authentication-with-python/

import pycurl

class Response(object):
    """ utility class to collect the response """
    def __init__(self):
        self.chunks = []
    def callback(self, chunk):
        self.chunks.append(chunk)
    def content(self):
        return ''.join(self.chunks)

res = Response()

curl = pycurl.Curl()
curl.setopt(curl.URL, "https://yourservice/path")
curl.setopt(curl.WRITEFUNCTION, res.callback)
curl.setopt(curl.CAINFO, "/path/to/CA.crt")
curl.setopt(curl.SSLCERT, "/path/to/client.pem")
curl.setopt(curl.SSL_VERIFYHOST, 0)
curl.perform()

print res.content()

===========================================================
