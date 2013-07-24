from forms.agaimparamParamenters import agaimparamParamenters


class AgaimpParamenters(object):
    """
    Gestisce i parametri di aGaimp.
    """
    def __init__(self, data_file_name):
        self.data_file = data_file_name

    def edit(self):
        """ Usa una wxForm (AgaimpParamentersForm) per editare i parametri.
        """
        self.form = agaimparamParamenters(None)
        self.form.Show()

    def usr(self):
        # TODO: ricavare il nome utente
        return

    def pwd(self):
        # TODO: ricavare la password
        return
