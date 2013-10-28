from settings import INSTALLED_SERVERS

from apps.userauth.controllers import user_auth

from . import Server


# Inizializza tutti i server installati
for server in INSTALLED_SERVERS:
    __import__(server)


# Esegue i server attivi
def execute():
    for server in Server.get_servers():
        if user_auth.sever(server.id_srv):
            if not server.isAlive():
                server.start()
