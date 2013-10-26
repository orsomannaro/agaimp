import wx

from gui.agaimp_gui import FrmSettings


class aGaiMpFrmSettings(FrmSettings):
    def __init__(self, parent, localparam):
        super(aGaiMpFrmSettings, self).__init__(parent)
        self.Bind(wx.EVT_SHOW, self.OnShow)

        self.localparam = localparam

        self.Show()

    def OnCancel(self, event):
        self.Close()

    def OnSave(self, event):
        """ Salva i parametri """
        #TODO: i valori dei parametri devono essere validati prima di salvarli
        params_names = self.localparam.params.keys()
        for name in params_names:
            if name in self.__dict__.keys():
                value = self.__dict__[name].Value
                self.localparam.params[name] = value
        self.localparam.save()
        self.Close()

    def OnShow(self, event):
        """ Carica i parametri.
        NB: i nomi dei controlli che nella form sono associati ai parametri
            devono essere indicati nel file __init__
        """
        if event.Show:
            params = self.localparam.params.items()
            for name, value in params:
                if name in self.__dict__.keys():
                    self.__dict__[name].Value = value
