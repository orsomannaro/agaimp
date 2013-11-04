import requests
from settings import SITE_URL

from apps.localparam import PARAM_USR, PARAM_PWD
from apps import localparam


IMPORTS_AUTH = 'IMPORTERS'  # List importer abilitati


#_site = SITE_URL
#_usr = localparam.get(PARAM_USR)
#_pwd = localparam.get(PARAM_PWD)
_site = 'https://api.github.com/'
_usr = 'orsomannaro@gmail.com'
_pwd = ''


def _read_auth():
    #req = requests.get(_site, auth=(_usr, _pwd))
    #return req.json() if req.ok else {}
    return {IMPORTS_AUTH: ['sai_delta', 'sai_sigma']}


def _get_auth(auth):
    return _read_auth()[auth]


def get_importers():
    return _get_auth(IMPORTS_AUTH)
