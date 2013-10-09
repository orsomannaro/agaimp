

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


class SubscriberStdOut(object):
    """
    Usata per debug al fine di stampare sulla console
    messaggi dei Publisher
    """
    def publish(self, message):
        print message
