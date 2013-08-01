from settings import PARAM_FILE

from .models import LocalParam
from .views import AgaimparamView


class EditParams(AgaimparamView):
    """
    Edit parametri tramite form.
    (?forse il posto corretto e' con le views?)
    """
    def __init__(self, parent, params_obj):
        """
        :param params_obj: istanza della classe LocalParam
        """
        AgaimparamView.__init__(self, parent)
        self.params_obj = params_obj

    def OnLoadData(self, event):
        """ Carica i parametri.
        """
        if event.Show:
            params = self.params_obj.params()
            for key, value in params.items():
                if key in self.__dict__.keys():
                    self.__dict__[key].Value = value

    def OnSalvaClick(self, event):
        """ Salva i parametri.
        """
        #TODO: i valori dei parametri devono essere validati prima di salvarli
        params = self.params_obj.params()
        for name in params.keys():
            if name in self.__dict__.keys():
                value = self.__dict__[name].Value
                params[name] = value
        self.params_obj.save()
        self.Close()

    def OnAnnullaClick(self, event):
        self.Close()


class Params(LocalParam):

    def edit_frame(self, parent=None):
        edit_frm = EditParams(parent, self)
        edit_frm.Show()

    def OnEdit(self, event):
        self.edit_frame()


params = Params(PARAM_FILE)
