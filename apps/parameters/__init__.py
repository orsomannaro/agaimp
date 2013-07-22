"""
Gestisce i parametri di aGaimp.

     agaimparam: oggetto le cui proprieta' sono i parametri utili in aGaiMP
ParamentersForm: form per editare i parametri
"""

from forms import agaimparam_form


class ParamentersForm(agaimparam_form.Paramenters):
    """
    Form di gestione parametri di configurazione
    sottoclasse della form Paramenters generata da wxFormBuilder.
    """
    def __init__(self, parent):
        agaimparam_form.Paramenters.__init__(self, parent)

    def OnSalvaClick(self, event):
        # TODO: Implement OnSalvaClick
        pass

    def OnAnnullaClick(self, event):
        # TODO: Implement OnAnnullaClick
        pass


class Paramenters(object):

    def edit(self):
        self.form = ParamentersForm(None)
        self.form.Show()

    def usr(self):
        # TODO: ricavare il nome utente
        return

    def pwd(self):
        # TODO: ricavare la password
        return


agaimparam = Paramenters()
