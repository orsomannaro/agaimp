import wx

from gui.agaimp_gui import FrmSettings


class aGaiMpFrmSettings(FrmSettings):
    """
    Editing dei parametri.
    Sono automaticamente considerati tutti e soli
     i parametri che hanno un controllo con lo stesso nome.
    """
    def __init__(self, parent, localparam):
        super(aGaiMpFrmSettings, self).__init__(parent)
        self.Bind(wx.EVT_SHOW, self.OnShow)
        self.localparam = localparam
        self.Show()

    def OnCancel(self, event):
        self.Close()

    def OnSave(self, event):
        """  Salva i controlli che hanno nome uguale a quello di un parametro """
        #TODO: validare i dati prima di salvarli
        params_names = self.localparam.params.keys()
        for name in params_names:
            if name in self.__dict__.keys():
                value = self.__dict__[name].Value
                self.localparam.params[name] = value
        self.localparam.save()
        self.Close()

    def OnShow(self, event):
        """  Carica i parametri che hanno nome uguale a quello di un controllo """
        if event.Show:
            params = self.localparam.params.items()
            for name, value in params:
                if name in self.__dict__.keys():
                    self.__dict__[name].Value = value
