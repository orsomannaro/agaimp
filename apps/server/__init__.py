"""
Plug-in pattern per la gestione dei server.

Il metodo __init__ di <sottoclasse 'type'> viene eseguito ogni volta che una classe *dichiara*:

 __metaclass__ = <sottoclasse 'type'>

NB: in fase di dichiarazione non di istanziamento!

Quindi, in questo caso, la prima volta viene eseguito in fase di dichiarazione della classe Server
 e successivamente per ogni server che eredita da questa.
"""

import threading

from libs.utils import Messenger

from .publisher import servers_publisher


class ServerMount(type):
    """
    Sistema di plugin per le classi che dichiarano
    __metaclass__ = ServerMount
    """

    def __init__(cls, name, bases, attrs):
        """ Colleziona le sottoclassi nella lista _servers """
        if not hasattr(cls, '_servers'):
            cls._servers = []
        else:
            cls._servers.append(cls)

    def get_servers(self, *args, **kwargs):
        """ Torna una lista di istanze, una per ogni sottoclasse """
        return [srv(*args, **kwargs) for srv in self._servers]


class Server(object):
    """
    Server importer.
    Tutti gli importer devono estendere questa classe,
    """
    __metaclass__ = ServerMount

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
