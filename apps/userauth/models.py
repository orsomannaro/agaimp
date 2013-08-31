import requests

from . import SERVERS_AUTH


class UserAuth(object):
    """
    Ricava autorizzazioni utente.
    """
    def __init__(self, url, usr, pwd):
        self.url = url
        self.usr = usr
        self.pwd = pwd

    def auth(self, auth):
        """
        :return: autorizzazione 'auth'.
        """
        try:
            return self.get()[auth]
        except:
            return None

    def get(self):
        return {'SERVERS': [('DELTA', True), ('SIGMA', True)]}

    def get_CORRETTA(self):
        """
        Effettua login a self.ulr e legge autorizzazioni.
        :param usr: UUID installazione registrato sul sito (localparam.param_uuid)
        :return: dizionario autorizzazioni.
        """
        req = requests.get(self.url, auth=(self.usr, self.pwd))
        # if req.ok:
        #     # Recupero dizionario autorizzazioni utente.
        #     user_auth = req.json()
        #     return user_auth
        return req.json() if req.ok else {}

    def sever(self, id_srv):
        """ Ritorna True se id_srv e' abilitato.
        """
        try:
            s = self.auth(SERVERS_AUTH)
            server_auth = dict(self.auth(SERVERS_AUTH))
            return server_auth[id_srv]
        except:
            return False
