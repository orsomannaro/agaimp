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
        """
        Effettua login a self.ulr e legge autorizzazioni.
        :param usr: UUID installazione registrato sul sito (params.param_uuid)
        :return: dizionario autorizzazioni.
        """
        req = requests.get(self.url, auth=(self.usr, self.pwd))
        if req.ok:
            # Recupero dizionario autorizzazioni utente.
            #user_auth = req.json()
            user_auth = {'servers': [('delta', False), ('sigma', True)]}
            return user_auth
        return {}

    def sever(self, id_srv):
        """ Ritorna True se id_srv e' abilitato.
        """
        try:
            server_auth = dict(self.auth(SERVERS_AUTH))
            return server_auth[id_srv]
        except:
            return False
