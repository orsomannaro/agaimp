from settings import AGAIN_URL

from apps.localparam.controllers import localparam

from .models import UserAuth


def get_pwd(uuid):
    """
    Calcola la password in base all'uuid dell'installazione.
    :param uuid: uuid dell'installazione
    :return: password
    """
    import hashlib
    return str(hashlib.sha1(uuid).hexdigest())


#user_auth = UserAuth(AGAIN_URL, localparam.param_uuid, get_pwd(localparam.param_uuid))
user_auth = UserAuth('https://api.github.com/', 'orsomannaro@gmail.com', '')
