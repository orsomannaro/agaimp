

class Publisher:
    def __init__(self, name):
        self.name = name
        self._subscribers = set()

    def subscribe(self, task):
        self._subscribers.add(task)

    def unsubscribe(self, task):
        self._subscribers.remove(task)

    def write(self, message):
        for subscriber in self._subscribers:
            subscriber.write(message)
