import threading


class Publisher(object):
    def __init__(self, name):
        self.name = name
        self._subscribers = set()

    def subscribe(self, subscriber):
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def __publish(self, message):
        for subscriber in self._subscribers:
            if hasattr(subscriber, 'publish'):
                subscriber.publish(message)

    def publish(self, message):
        t = threading.Thread(target=self.__publish, args=([message]))
        t.daemon = True
        t.start()


class SubscriberStdOut(object):
    def publis(self, message):
        print message
