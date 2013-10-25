import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

ASSETS_DIR = os.path.join(PROJECT_ROOT, 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'img')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')

PARAM_FILE = os.path.join(PROJECT_ROOT, 'data/param.json')

AGAIN_URL = 'http://www.again.it/'
AGAIN_URL_SSL = 'https://www.again.it/'

AGAIN_LOGO = os.path.join(IMAGES_DIR, 'logo_small.png')

# Systray
TRAY_ICON = os.path.join(IMAGES_DIR, 'trayicon.ico')
TRAY_ICON_WRN = os.path.join(IMAGES_DIR, 'trayicon_wrn.ico')
TRAY_ICON_ERR = os.path.join(IMAGES_DIR, 'trayicon_err.ico')
TRAY_TOOLTIP_TITLE = 'aGaiMp: '
TRAY_TOOLTIP = TRAY_TOOLTIP_TITLE+'working'
TRAY_TOOLTIP_WRN = TRAY_TOOLTIP_TITLE+'avvisi (fai click su Messaggi)'
TRAY_TOOLTIP_ERR = TRAY_TOOLTIP_TITLE+'ERRORI (fai click su Messaggi)'

# Server
RUN_AT = {
    'd': 'mon-fri',
    'h': 5,
    'm': 30
}

INSTALLED_SERVERS = [
    'apps.server.delta',
    'apps.server.sigma',
]
