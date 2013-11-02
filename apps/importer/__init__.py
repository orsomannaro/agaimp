from settings import INSTALLED_SERVERS

from apps.server import Server
from apps.userauth.controllers import user_auth


# Inizializza tutti i server installati
for server in INSTALLED_SERVERS:
    __import__(server)

# Generazione istanze dei server installati (get_servers())
__servers = []  # lista istanze server
for server in Server.get_servers():
    __servers.append(server)


# Esegue i server attivi
def start():
    global __servers
    for server in __servers:
        user_auth.sever(server.id_srv) and server.start()


# Lista degli id_srv
def get_auth_servers():
    return [server.id_srv for server in __servers if user_auth.sever(server.id_srv)]
