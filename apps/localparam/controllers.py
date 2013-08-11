from settings import PARAM_FILE

from .models import LocalParam
from .views import EditParams


class Params(LocalParam):

    def edit_frame(self, parent=None):
        edit_frm = EditParams(parent, self)
        edit_frm.Show()

    def OnEdit(self, event):
        self.edit_frame()


params = Params(PARAM_FILE)
