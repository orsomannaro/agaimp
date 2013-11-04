# coding: latin-1

import os

from settings import DATA_UPLOAD_DIR

from apps import uploader
from apps.localparam import PARAM_IP_SIGMA
from apps import localparam

from libs.utils import ftp_download

from .. import Importer


ID_IMPORTER = 'sai_sigma'  # importers ID su aGain

SIGMA_USR = 'sigmaout'
SIGMA_PWD = 'fondisai'
SIGMA_FILE = 'dtwhouse.dwh'

site = localparam.get(PARAM_IP_SIGMA)
download_dir = DATA_UPLOAD_DIR


class SigmaImporter(Importer):

    name = ID_IMPORTER

    def __init__(self):
        super(SigmaImporter, self).__init__()

    def run(self):
        self.message.log('Inizio import')
        file_path = os.path.join(download_dir, SIGMA_FILE)
        try:
            #ftp_download(file_path, site, user=SIGMA_USR, password=SIGMA_PWD)
            ftp_download(file_path, '192.168.1.11', user='leandro', password='L34ndr0-2009', remote_dir='home')
        except:
            self.message.error('Errore su import')
        else:
            uploader.upload(file_path, ID_IMPORTER)
        self.message.log('Fine import')
