import io


class MessageBuffer(object):
    """ Conserva messaggi
    """
    def __init__(self):
        self._buffer = io.StringIO()

    def note(self, message):
        self._buffer.write(message)

    def get(self):
        return self._buffer.getvalue()

    def reset(self):
        self._buffer.close()
        self._buffer .__init__()
