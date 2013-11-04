"""
ImportersPublisher():
 classe che definisce un publisher dal quale leggere i messaggi lanciati dagli importer attivi.

ImportersMessenger():
 classe che definisce un messenger dove gli importer possono lanciare i loro messagggi.

"""

import datetime


# -------------------- Pub/Sub --------------------
#
# pub = Publisher('nome_publisher')
#
#class sub(object):
#    def publish(self, message):
#        for key, value in message.items():
#            print '%s: %s' % (key, value)
#
#pub.subscribe(sub())


class ImportersPublisher(object):
    def __init__(self, name):
        self.name = name
        self._subscribers = set()

    def subscribe(self, subscriber):
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def publish(self, message):
        for subscriber in self._subscribers:
            if hasattr(subscriber, 'publish'):
                subscriber.publish(message)

# -------------------- (Pub/Sub) --------------------


# -------------------- Messenger --------------------
# Istanziando Messenger si possono inviare messaggi di tipo Message via publisher


MSG_LVL_ERR = 'error'
MSG_LVL_LOG = 'log'
MSG_LVL_WRN = 'warning'


class ImportersMessage(object):
    def __init__(self, sender, level, text):
        self.level = level
        self.sender = sender
        self.text = text
        self.time = datetime.datetime.now().strftime("%H:%M:%S")


class ImportersMessenger(object):
    """
    Invia Message con publisher.
    NB: publisher deve implementare publish (secondo il pattern pub/sub)
    """

    def __init__(self, publisher):
        self.publisher = publisher

    def __message(self, sender, text, level):
        msg = ImportersMessage(sender, level, text)
        self.publisher.publish(msg)

    def error(self, sender, text):
        return self.__message(sender, text, MSG_LVL_ERR)

    def log(self, sender, text):
        return self.__message(sender, text, MSG_LVL_LOG)

    def warning(self, sender, text):
        return self.__message(sender, text, MSG_LVL_WRN)

# -------------------- (Messenger) --------------------
