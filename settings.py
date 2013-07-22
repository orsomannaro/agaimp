import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

SECRET_KEY = '@@h5gtm9=t@)ug7fc*fv)627l(py3^fh%2yxm8x5s16ah+ler+'

ASSETS_DIR = os.path.join(PROJECT_ROOT, 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'img')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')

TRAY_ICON = os.path.join(IMAGES_DIR, 'trayicon.ico')
TRAY_TOOLTIP = 'aGain'

AGAIN_URL = ''
AGAIN_URL_SSL = ''
