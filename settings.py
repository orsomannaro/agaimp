import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

ASSETS_DIR = os.path.join(PROJECT_ROOT, 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'img')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')

TRAY_ICON = os.path.join(IMAGES_DIR, 'trayicon.ico')
TRAY_ICON_ERR = os.path.join(IMAGES_DIR, 'trayicon_err.ico')
TRAY_TOOLTIP = 'aGain'

AGAIN_URL = 'http://www.again.it/'
AGAIN_URL_SSL = 'https://www.again.it/'

PARAM_FILE = os.path.join(PROJECT_ROOT, 'param.json')
