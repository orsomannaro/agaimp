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
    Permette di collezionare le sue sottoclassi.
    _servers: lista delle sottoclassi
    """

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, '_servers'):
            cls._servers = []
        else:
            cls._servers.append(cls)

    def get_servers(self, *args, **kwargs):
        """ Torna una lista di tuple con le classi derivate da Server """
        return [srv(*args, **kwargs) for srv in self._servers]


class Server(object):
    """
    Una app che importa dati da un server deve estendere questa classe,
    """
    __metaclass__ = ServerMount

    def __init__(self, id_srv):
        self.id_srv = id_srv  # id del server
        self.message = Messenger(self.id_srv, servers_publisher)
        self.__thread = self.__new_thread()

    def __new_thread(self):
        return threading.Thread(target=self.run)

    def isAlive(self):
        return self.__thread.isAlive()

    def run(self):
        """ Implementazione logica del server """
        pass

    def start(self):
        """ Avvia il server """
        self.__thread = self.__new_thread()
        self.__thread.daemon = True
        self.__thread.start()
