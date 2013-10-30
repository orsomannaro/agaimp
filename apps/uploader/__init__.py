"""
NOTA:
il codice fa fede nella convenzione che il nome del file corrisponde al nome dell'impoter.
"""

import os
import shutil
from time import sleep
from threading import Thread

import requests

from settings import SITE_URL, DATA_DIR
from apps.localparam import PARAM_UUID
from apps.localparam.controllers import localparam
from apps.server.importer import get_server_id


importer_uuid = localparam.params[PARAM_UUID]
site = SITE_URL

upload_dir = os.path.join(DATA_DIR, 'upload')  # directory file da uploadare
os.path.exists(upload_dir) or os.makedirs(upload_dir)

send_dir = os.path.join(DATA_DIR, 'sending')  # directory di lavoro
os.path.exists(send_dir) or os.makedirs(send_dir)


def _supply_file(file_path, importer=''):
    if importer:
        dest = os.path.join(upload_dir, importer)  # per convenzione <nome file> = <nome importer>
        supplier = shutil.copy
    else:
        dest = os.path.join(send_dir, os.path.basename(file_path))
        supplier = shutil.move
    try:
        supplier(file_path, dest)
    except shutil.Error as e:  # eg. src and dest are the same file
        return None  # print('Error: %s' % e)
    except IOError as e:  # eg. source or destination doesn't exist
        return None  # print('Error: %s' % e.strerror)
    return dest


def _list_dir(dir_name):
    return [os.path.join(dir_name, name) for name in os.listdir(dir_name) if
            os.path.isfile(os.path.join(dir_name, name)) and name in get_server_id()]


def _send_file(file_path):
    importer = os.path.basename(file_path)
    url = '%s/api/v0/agent/%s/send/' % (site, importer_uuid)
    payload = {'importer': importer, 'file_path': file_path}
    r = requests.post(url, data=payload)
    os.remove(file_path)


def _sending():
    while True:
        for file_path in _list_dir(send_dir):
            _send_file(file_path)
        sleep(60)


def upload(file_path, importer):
    _supply_file(file_path, importer)  # import file


def _uploading():
    while True:
        for file_path in _list_dir(upload_dir):
            _supply_file(file_path)
        sleep(60)


uploader = Thread(target=_uploading)
uploader.daemon = True
uploader.start()

sender = Thread(target=_sending)
sender.daemon = True
sender.start()
