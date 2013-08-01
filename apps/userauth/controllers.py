from settings import AGAIN_URL

from apps.localparam.controllers import params

from .models import UserAuth
from .utils import get_pwd


#user_auth = UserAuth(AGAIN_URL, params.param_uuid, get_pwd(params.param_uuid))
user_auth = UserAuth('https://api.github.com/', 'orsomannaro@gmail.com', 'lewis501')
