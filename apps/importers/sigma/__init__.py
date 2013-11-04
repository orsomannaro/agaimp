# coding: latin-1

import os

from settings import DATA_UPLOAD_DIR

from apps import uploader
from apps import localparam

from .. import Importer, messenger
from ..utils import ftp_download, md5


ID_IMPORTER = 'sai_sigma'  # importers ID su aGain

SIGMA_USR = 'sigmaout'
SIGMA_PWD = 'fondisai'
SIGMA_FILE = 'dtwhouse.dwh'

site = localparam.get(localparam.PARAM_SIGMA_IP)
download_dir = DATA_UPLOAD_DIR


class SigmaImporter(Importer):

    name = ID_IMPORTER

    def __init__(self):
        super(SigmaImporter, self).__init__()

    def run(self):
        messenger.log(self.name, 'Inizio import')
        file_path = os.path.join(download_dir, SIGMA_FILE)
        try:
            #ftp_download(file_path, site, user=SIGMA_USR, password=SIGMA_PWD)
            ftp_download(file_path, '192.168.1.11', user='leandro', password='L34ndr0-2009', remote_dir='home')
        except:
            messenger.log(self.name, 'Errore su import')
        else:
            new_md5 = md5(file_path)
            if new_md5 != localparam.get(localparam.PARAM_SIGMA_MD5):
                uploader.upload(file_path, ID_IMPORTER)
                localparam.set(localparam.PARAM_SIGMA_MD5, new_md5)
                messenger.log(self.name, 'Dati aggiornati!')
            else:
                messenger.log(self.name, 'Nessun aggiornamento!')
            os.remove(file_path)
        messenger.log(self.name, 'Fine import')
