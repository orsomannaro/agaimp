"""
Plug-in pattern per la gestione dei server
"""

import datetime
import threading

from .publisher import servers_publisher


class ServerMount(type):
    """
    Colleziona classi derivate da Server.
    _servers: lista delle classi
    """

    def __init__(cls, name, bases, attrs):
        # Questa parte viene eseguita ogni volta che
        # una classe dichiara __metaclass__ = ServerMount
        if not hasattr(cls, '_servers'):
            cls._servers = []
        else:
            cls._servers.append(cls)

    def get_servers(self, *args, **kwargs):
        """ Torna una lista di tuple con le classi derivate da Server
        """
        return [srv(*args, **kwargs) for srv in self._servers]


class Server(object):
    """
    Una app che importa dati da un server deve estendere questa classe,
    """
    __metaclass__ = ServerMount

    def __init__(self):
        self.id_srv = ''  # id del server
        self.publisher = servers_publisher
        self.__thread = self.__new_thread()

    def __new_thread(self):
        return threading.Thread(target=self.run)

    def isAlive(self):
        return self.__thread.isAlive()

    def message(self, text, level='log'):
        """ Invia un messaggio di log
        """
        msg = ServerMessage(self.id_srv, level, text)
        self.publisher.publish(msg)

    def error(self, text):
        """ Invia un messaggio di errore
        """
        self.message(text, 'error')

    def warning(self, text):
        """ Invia un messaggio di warning
        """
        self.message(text, 'warning')

    def run(self):
        """ Logica del server
        """
        pass

    def start(self):
        self.__thread = self.__new_thread()
        self.__thread.daemon = True
        self.__thread.start()


class ServerMessage(object):
    def __init__(self, server, level, text):
        self._server = server
        self._level = level
        self._text = text
        self._time = datetime.datetime.now().strftime("%H:%M:%S")

    @property
    def level(self):
        return self._level

    @property
    def text(self):
        return self._text

    @property
    def server(self):
        return self._server

    @property
    def time(self):
        return self._time
