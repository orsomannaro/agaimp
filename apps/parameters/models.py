from forms.agaimparamParamenters import agaimparamParamenters


class AgaimpParamenters(object):
    """
    Gestisce i parametri di aGaimp.
    I parametri sono salvati in self.file_name in formato json.
    """
    def __init__(self, param_file_name):
        self.file_name = param_file_name + '.json'

    def edit(self):
        """ Usa una wxForm (AgaimpParamentersForm) per editare i parametri.
        """
        self.form = agaimparamParamenters(None)
        self.form.Show()



    def save_data(self):
        pass
