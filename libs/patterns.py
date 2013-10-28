"""
Implementazione di design patterns.
"""

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


class Publisher(object):
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
