

class ServerMount(type):
    """
    Colleziona oggetti istanziati da classi aventi __metaclass__ = ServerMount.
    __servers: lista oggetti istanziati
    """
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, '__serverscollector'):
            # Questa parte viene eseguita solo la prima volta che
            # una classe dichiara __metaclass__ = ServerMount
            cls.__servers = []
        else:
            # Questa parte viene eseguita ogni volta che si istanzia
            # un oggetto di una classe avente __metaclass__ = ServerMount
            cls.__servers.append(cls)

    def get_servers(self, *args, **kwargs):
        """ Torna la lista degli oggetti istanziati
        """
        return [d(*args, **kwargs) for d in self.__servers]


class Server(object):
    """
    Una app che importa dati da un server deve estendere questa classe,
    assegnare un valore a 'id_srv' e implementare il metodo 'read'.
    """
    __metaclass__ = ServerMount

    id_srv =''

    def read(self):
        raise NotImplementedError("Must subclass me")


servers = Server.get_servers()