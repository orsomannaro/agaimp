"""
Plug-in pattern per server
"""


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
    assegnare un valore a 'id_srv' e implementare il metodo 'read'.
    """
    __metaclass__ = ServerMount

    id_srv =''

    def read(self):
        raise NotImplementedError("Must subclass me")
