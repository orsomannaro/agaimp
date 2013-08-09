

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
            #TODO: qui e' meglio usare un thread (magari daemon)?
            subscriber.publish(message)


class SubscriberStdOut(object):
    def publish(self, message):
        print message
