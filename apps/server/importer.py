from apps.userauth.controllers import user_auth

from settings import INSTALLED_SERVERS

from . import Server


# Carica server
for server in INSTALLED_SERVERS:
    __import__(server)

__servers = []
for server in Server.get_servers():
    __servers.append(server)


def execute():
    for server in __servers:
        if user_auth.sever(server.id_srv):
            if not server.isAlive():
                server.start()
