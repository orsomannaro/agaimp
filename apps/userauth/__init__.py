"""
Autorizzazioni utente.
"""

# SERVER_AUTH: autorizzazioni servers.
# Lista di tuple (<ID_SRV>, <True/False>) dove True = schedule e False = unschedule.
# Gli ID_SRV rispecchiano il modo in cui i server sono identificati in SERVER_AUTH.
SERVERS_AUTH = 'servers'
ID_SRV_DELTA = 'delta'
ID_SRV_SIGMA = 'sigma'

# Lista di tutte le autorizzazioni.
AUTH = [SERVERS_AUTH,]

# NOTE:
# Il login viene effettuato con user=UUID installazione e password=get_pwd(UUID)
