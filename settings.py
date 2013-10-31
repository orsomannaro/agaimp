import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

ASSETS_DIR = os.path.join(PROJECT_ROOT, 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'img')
LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
UPLOAD_DIR = os.path.join(DATA_DIR, 'upload')

PARAM_FILE = os.path.join(PROJECT_ROOT, 'data/param.json')

LOGO = os.path.join(IMAGES_DIR, 'logo.png')

SITE_URL = 'http://213.187.9.92'

# Schedulazione esecuzione dei server
RUN_AT = {
    'd': 'mon-fri',
    'h': 5,
    'm': 30
}

# Server installati
INSTALLED_SERVERS = [
    'apps.server.delta',
    'apps.server.sigma',
]
