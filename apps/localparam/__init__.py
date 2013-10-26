import uuid


# Parametri locali e loro valori di default.
# I nomi dei parametri devono essere identici ai nomi
#  dei controlli a loro associati nella form di editing.

PARAM_UUID = 'param_uuid'  # identificativo installazione
PARAM_IP_DELTA = 'param_ip_delta'  # indirizzo IP del server DELTA
PARAM_IP_SIGMA = 'param_ip_sigma'  # indirizzo IP del server SIGMA

LOCAL_PARAMETERS = {
    PARAM_UUID: str(uuid.uuid4()),
    PARAM_IP_DELTA: '0.0.0.0',
    PARAM_IP_SIGMA: '0.0.0.0',
}
