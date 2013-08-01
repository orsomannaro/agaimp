from .models import UserAuth


# user_auth = UserAuth(AGAIN_URL, params.param_uuid, get_pwd(params.param_uuid))
user_auth = UserAuth('https://api.github.com/', 'orsomannaro@gmail.com', 'lewis501')
