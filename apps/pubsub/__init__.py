import threading


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
            t = threading.Thread(target=subscriber.publish, args=([message]))
            t.daemon = True
            t.start()


class SubscriberStdOut(object):
    def publish(self, message):
        print message
