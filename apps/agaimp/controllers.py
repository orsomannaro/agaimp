import io

from .views import ResetCloseDialog


class ServerMessages(object):
    """
    Gestione dei messaggi provenienti dai server
    """

    def __init__(self):
        self.reset()

    def add(self, message):
        self._messages.write(message)

    def close(self):
        self._messages.close()

    def get(self):
        return u'%s' % self._messages.getvalue()

    def show(self):
        """
        Mostra i messaggi.
        Ritorna True se l'utente desidera eliminarli.
        """
        messages = self._messages.getvalue()
        msg_dlg = ResetCloseDialog()
        #resp = msg_dlg.response(messages)
        #return messages and resp and self.reset()
        msg_dlg.Show(True)

    def reset(self):
        self._messages = io.StringIO()
        return True
