from settings import PARAM_FILE

from .models import LocalParam
from .views import AgaimparamView


class EditParams(AgaimparamView):
    #TODO: forse il posto corretto e' con le views?
    """
    Edit parametri tramite form.
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
            for key, value in self.params_obj.params.items():
                if key in self.__dict__.keys():
                    self.__dict__[key].Value = value

    def OnSalvaClick(self, event):
        """ Salva i parametri.
        """
        #TODO: i valori dei parametri devono essere validati prima di salvarli
        for name in self.params_obj.params.keys():
            if name in self.__dict__.keys():
                value = self.__dict__[name].Value
                self.params_obj.params[name] = value
        self.params_obj.save()
        self.Close()

    def OnAnnullaClick(self, event):
        self.Close()


class Params(LocalParam):
    def __init__(self, file_name):
        super(Params, self).__init__(file_name)

    def edit(self, parent=None):
        edit_frm = EditParams(parent, self.params)
        edit_frm.Show()

    def OnEdit(self, event):
        self.edit()


params = Params(PARAM_FILE)
