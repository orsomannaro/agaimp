"""
Plug-in pattern per la gestione dei server.

Il metodo __init__ di <sottoclasse 'type'> viene eseguito ogni volta che una classe *dichiara*:

 __metaclass__ = <sottoclasse 'type'>

NB: in fase di dichiarazione non di istanziamento!

Quindi, in questo caso, la prima volta viene eseguito in fase di dichiarazione della classe Server
 e successivamente per ogni server che eredita da questa.
"""

import threading

from settings import INSTALLED_SERVERS

from libs.utils import Messenger
from libs.patterns import Publisher


_servers = {}  # server installati


class ServerMount(type):
    """
    Sistema di plugin per le classi che dichiarano
    __metaclass__ = ServerMount
    """
    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        """
        @param name: Name of the class
        @param bases: Base classes (tuple)
        @param attrs: Attributes defined for the class
        """
        new_cls = type.__new__(cls, name, bases, attrs)
        if attrs['name']:  # classe Server esclusa
            cls.REGISTRY[attrs['name']] = new_cls
        return new_cls


class Server(object):
    """
    Server importer.
    Tutti gli importer devono estendere questa classe,
    """
    __metaclass__ = ServerMount

    name = ''  # ogni sottoclasse deve avere un nome diverso

    def __init__(self, id_srv):
        self.id_srv = id_srv  # id del server
        self.message = Messenger(self.id_srv, servers_publisher)
        self._thread = self._new_thread()

    def _new_thread(self):
        return threading.Thread(target=self.run)

    def run(self):
        """ Implementazione logica del server """
        pass

    def start(self):
        """ Avvia il server """
        if not self._thread.is_alive():
            self._thread = self._new_thread()
            self._thread.daemon = True
            self._thread.start()


# Publisher per i messaggi dei server
servers_publisher = Publisher('servers_publisher')


# Inizializza tutti i server installati
def load():
    global _servers

    for server in _servers:
        del server

    for server in INSTALLED_SERVERS:
        __import__(server)

    for class_name, class_type in ServerMount.REGISTRY.items():
        _servers[class_name] = class_type()  # un server per ogni sottoclasse


# Lista degli id_srv
#def get_auth_servers():
#    global _servers
#    return [server.id_srv for server in _servers if user_auth.sever(server.id_srv)]


# Avvia server abilitati
#def start():
#    global _servers
#    for server in _servers:
#        server.start()
