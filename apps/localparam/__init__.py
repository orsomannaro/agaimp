import os
import uuid

from settings import DATA_DIR, PARAM_FILE

from .models import LocalParam
from .views import aGaiMpFrmSettings


# Parametri locali e loro valori di default.
# I nomi dei parametri devono essere identici ai nomi
#  dei controlli a loro associati nella form di editing.

PARAM_USR = 'param_user'  # utente
PARAM_PWD = 'param_password'  # password
PARAM_UUID = 'param_uuid'  # identificativo installazione
PARAM_IP_DELTA = 'param_ip_delta'  # indirizzo IP del importers DELTA
PARAM_IP_SIGMA = 'param_ip_sigma'  # indirizzo IP del importers SIGMA

DEFAULT_PARAMETERS = {
    PARAM_UUID: str(uuid.uuid4()),
    PARAM_IP_DELTA: '0.0.0.0',
    PARAM_IP_SIGMA: '0.0.0.0',
}


def edit():
    _localparam = LocalParam(os.path.join(DATA_DIR, PARAM_FILE), DEFAULT_PARAMETERS)
    aGaiMpFrmSettings(None, _localparam)


def get(param):
    _localparam = LocalParam(os.path.join(DATA_DIR, PARAM_FILE), DEFAULT_PARAMETERS)
    return _localparam.params[param]
