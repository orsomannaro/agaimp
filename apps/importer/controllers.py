from apps import userauth
from apps.userauth.controllers import user_auth

from . import models


class Importer(object):
    """ Importazione dai server
    """
    server_importers = {
        (userauth.ID_SRV_DELTA, models.DeltaServer),
        (userauth.ID_SRV_SIGMA, models.SigmaServer),
    }

    def execute(self):
        for id_srv, server in self.server_importers:
            if user_auth.sever(id_srv):
                server().read()
