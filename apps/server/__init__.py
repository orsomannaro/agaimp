import threading
# import wx
#
# from wx.lib.pubsub.pub import Publisher


#SERVER_TOPIC = 'server.messages'  # Publisher topic

from apps.pubsub import Publisher, SubscriberStdOut

servers_publisher = Publisher('servers_publisher')  # chi vuole leggere i messaggi dei server si iscrive qui


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
        print '  %s server is alive: %s' % (self.id_srv, self.__thread.isAlive())
        return self.__thread.isAlive()

    def run(self):
        """ Logica del server
        """
        pass

    # def send_message(self, message):
    #     """ Send message to publisher
    #     """
    #     wx.CallAfter(Publisher().sendMessage, SERVER_TOPIC, message)

    def start(self):
        self.__thread = self.__new_thread()
        self.__thread.start()


servers_publisher.subscribe(SubscriberStdOut())