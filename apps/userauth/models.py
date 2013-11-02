import requests

from . import SERVERS_AUTH


class UserAuth(object):

    def __init__(self, url, usr, pwd):
        self.url = url
        self.usr = usr
        self.pwd = pwd

    def auth(self, auth):
        """ Ritorna autorizzazione auth """
        return self.read_auth()[auth]

    def read_auth(self):
        """ Effettua login a self.url e ritorna la lista delle autorizzazioni """
        #req = requests.get(self.url, auth=(self.usr, self.pwd))
        #return req.json() if req.ok else {}
        return {SERVERS_AUTH: [('sai_delta', False), ('sai_sigma', True)]}

    def sever(self, id_srv):
        """ Ritorna True se id_srv e' abilitato """
        server_auth = dict(self.auth(SERVERS_AUTH))
        if id_srv in server_auth:
            return server_auth[id_srv]
        return False
