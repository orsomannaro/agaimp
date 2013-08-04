

class ServerMount(type):
    """
    Colleziona oggetti istanziati da classi aventi __metaclass__ = ServerMount.
    _servers: lista oggetti istanziati
    """
    def __init__(cls, name, bases, attrs):
        # Questa parte viene eseguita ogni volta che
        # una classe dichiara __metaclass__ = ServerMount
        if not hasattr(cls, '_servers'):
            cls._servers = []
        else:
            cls._servers.append(cls)

    def get_servers(self, *args, **kwargs):
        """ Torna la lista degli oggetti istanziati
        """
        return [d(*args, **kwargs) for d in self._servers]


class Server(object):
    """
    Una app che importa dati da un server deve estendere questa classe,
    assegnare un valore a 'id_srv' e implementare il metodo 'read'.
    """
    __metaclass__ = ServerMount

    id_srv =''

    def read(self):
        raise NotImplementedError("Must subclass me")
