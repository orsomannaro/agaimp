from settings import INSTALLED_SERVERS

from apps.userauth.controllers import user_auth

from . import Server


# Inizializza tutti i server installati
for server in INSTALLED_SERVERS:
    __import__(server)

# Generazione istanze dei server installati (get_servers())
__servers = []  # lista istanze server
for server in Server.get_servers():
    __servers.append(server)


# Esegue i server attivi
def execute():
    for server in __servers:
        user_auth.sever(server.id_srv)and server.start()
