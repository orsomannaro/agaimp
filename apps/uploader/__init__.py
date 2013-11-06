"""
Gestione upload su aGain.

upload():
 i file da inviare vengono copiati nella directory di lavoro
  aggiungendo al nome il suffisso <separatore><importer>
  e estensione '.agaimp'

La directory di lavoro viene monitorata verificando la presenza di file '*.agaimp'
 i quali, uno alla volta, vengono uploadati su aGain.

Un file in fase di upload viene rinominato con estensione '.again'

"""

import os
import requests
import shutil
import time
import threading

from settings import SITE_URL, DATA_UPLOAD_DIR

from apps import localparam
from apps.userauth import get_importers


CHECK_FREQ = 5

site = SITE_URL
upload_dir = DATA_UPLOAD_DIR
uuid = localparam.get(localparam.PARAM_UUID)

uploading_fixed_name = uuid
separator = '_-__-_'
ready_ext = '.ready'
waiting_ext = '.waiting'


def _get_importer(file_path, suffix=ready_ext):
    name_sep_importer, ext = os.path.splitext(os.path.basename(file_path))
    if ext == suffix:
        try:
            name, importer = name_sep_importer.split(separator, 1)
        except:
            return ''
        else:
            return importer
    return ''


def _get_ready_file(file_path):
    name_sep_importer, ext = os.path.splitext(os.path.basename(file_path))
    if ext == waiting_ext:
        return os.path.join(upload_dir, '%s%s' % (name_sep_importer, ready_ext))
    return ''


def _get_waiting_file(file_path, importer):
    return os.path.join(upload_dir, '%s%s%s%s' % (os.path.basename(file_path), separator, importer, waiting_ext))


def _list_dir(ext):
    """
    Restituisce la lista dei file con estensione 'ext'
     presenti nella directory di lavoro.
    """
    return [os.path.join(upload_dir, name) for name in os.listdir(upload_dir) if
            os.path.isfile(os.path.join(upload_dir, name)) and name.endswith(ext)]


def _upload():
    """
    Considera i file in fase di invio presenti nella directory di lavoro
     (tipicamente uno solo).
    Controlla se il importers e' abilitato all'invio e in caso affermativo
     carica il file su aGain.
    """
    for file_path in _list_dir(ready_ext):
        importer = _get_importer(file_path)
        if importer in get_importers():
            print 'Inizio upload file %s' % file_path

            url = '%s/api/v0/agent/%s/send/' % (site, uuid)
            req = requests.post(url, data={'importers': importer}, files={'filepath': open(file_path)})

            # --- debug ---
            print url
            print req.status_code
            #with open(os.path.join(upload_dir, '../reg.html'), 'w') as f:
            #    f.write(req.text)
            # --- (debug) ---

            if req.status_code == requests.codes.ok:
                print 'Upload avvenuto con successo'
                os.remove(file_path)
            else:
                print 'Upload fallito'
        else:
            os.remove(file_path)
        print 'Fine upload'


def _uploading():
    """
    Considera i file in attesa di invio presenti nella directory di lavoro.
    Uno alla volta li rinomina in modo adeguato e li invia.
    """
    while True:
        _upload()  # elabora eventuale upload sospeso
        for file_path in _list_dir(waiting_ext):
            try:
                shutil.move(file_path, _get_ready_file(file_path))
            except:
                pass
            else:
                _upload()  # esegui upload
        time.sleep(CHECK_FREQ)


def start():
    global _sender
    _sender.start()


def upload(file_path, importer, zip_ext=''):
    """
    Importa i file nella directory di lavoro
     rinominandoli in modo adeguato.
    """
    if zip_ext:
        file_zip = os.path.join(upload_dir, os.path.basename(file_path))
        shutil.make_archive(file_zip, zip_ext, file_path)  # zip
        file_zip = '%s.%s' % (file_zip, zip_ext)
        shutil.move(file_zip, _get_waiting_file(file_path, importer))
    else:
        shutil.copy(file_path, _get_waiting_file(file_path, importer))


_sender = threading.Thread(target=_uploading)
_sender.daemon = True
