from settings import AGAIN_URL

from apps.localparam.controllers import params

from .models import UserAuth


def get_pwd(uuid):
    """
    Calcola la password in base all'uuid dell'installazione.
    :param uuid: uuid dell'installazione
    :return: password
    """
    import hashlib
    return str(hashlib.sha1(uuid).hexdigest())


#user_auth = UserAuth(AGAIN_URL, params.param_uuid, get_pwd(params.param_uuid))
user_auth = UserAuth('https://api.github.com/', 'orsomannaro@gmail.com', '')
