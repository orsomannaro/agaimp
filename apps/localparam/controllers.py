import os

from settings import DATA_DIR, PARAM_FILE

from .models import LocalParam


localparam = LocalParam(os.path.join(DATA_DIR, PARAM_FILE))
