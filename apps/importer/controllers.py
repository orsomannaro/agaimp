from apps.localparam import params

from .models import Importer, SigmaServer


def get_importer(auth_servers):
    importer = Importer()
    for (name, enabled) in auth_servers:
        if enabled:
            if name == 'delta':
                pass
            elif name == 'sigma':
                importer.add(SigmaServer, args=[params.param_ip_sigma], seconds=3, name='sigma')
            else:
                pass
    return importer
