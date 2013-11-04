import os
import uuid

from settings import DATA_DIR, PARAM_FILE

from .models import LocalParam
from .views import aGaiMpFrmSettings


# Parametri locali e loro valori di default.
# I nomi dei parametri devono essere identici ai nomi
#  dei controlli a loro associati nella form di editing.

PARAM_USR = 'param_usr'  # utente
PARAM_PWD = 'param_pwd'  # password
PARAM_UUID = 'param_uuid'  # identificativo installazione

PARAM_DELTA_IP = 'param_delta_ip'  # indirizzo IP del importers DELTA
PARAM_SIGMA_IP = 'param_sigma_ip'  # indirizzo IP del importers SIGMA
PARAM_SIGMA_MD5 = 'param_sigma_md5'  # md5 ultimo file uploadato

_DEFAULT_PARAMETERS = {
    PARAM_USR: '',
    PARAM_PWD: '',
    PARAM_UUID: str(uuid.uuid4()),
    PARAM_DELTA_IP: '0.0.0.0',
    PARAM_SIGMA_IP: '0.0.0.0',
    PARAM_SIGMA_MD5: '',
}


def edit():
    _localparam = LocalParam(os.path.join(DATA_DIR, PARAM_FILE), _DEFAULT_PARAMETERS)
    aGaiMpFrmSettings(None, _localparam)


def get(param):
    _localparam = LocalParam(os.path.join(DATA_DIR, PARAM_FILE), _DEFAULT_PARAMETERS)
    return _localparam.params[param]


def set(param, new_value):
    _localparam = LocalParam(os.path.join(DATA_DIR, PARAM_FILE), _DEFAULT_PARAMETERS)
    _localparam[param] = new_value
    _localparam.save()
