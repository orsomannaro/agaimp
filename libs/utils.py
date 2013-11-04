import datetime
import ftplib
import os


# -------------------- Messenger --------------------
# Istanziando Messenger si possono inviare Message via publisher


MSG_LVL_ERR = 'error'
MSG_LVL_LOG = 'log'
MSG_LVL_WRN = 'warning'


class Messenger(object):
    """
    Invia Message con publisher.
    NB: publisher deve implementare publish (secondo il pattern pub/sub)
    """

    def __init__(self, sender, publisher):
        self.sender = sender
        self.publisher = publisher

    def __message(self, text, level):
        msg = Message(self.sender, level, text)
        self.publisher.publish(msg)

    def error(self, text):
        return self.__message(text, MSG_LVL_ERR)

    def log(self, text):
        return self.__message(text, MSG_LVL_LOG)

    def warning(self, text):
        return self.__message(text, MSG_LVL_WRN)


class Message(object):
    def __init__(self, sender, level, text):
        self.level = level
        self.sender = sender
        self.text = text
        self.time = datetime.datetime.now().strftime("%H:%M:%S")

# -------------------- (Messenger) --------------------


# -------------------- ftp_download --------------------

def ftp_download(file_path, site, port=21, user='', password='', remote_dir=''):
    """
    Fetch a file by FTP with binary method from a site/directory
     anonymous unless you pass a user=(name, pswd) tuple.

    @param file_path: full path del file locale da cui viene ricavato anche il nome del file da scaricare
    """
    file_name = os.path.basename(file_path)
    local = open(file_path, 'wb')
    remote = ftplib.FTP()
    remote.connect(site, port,)
    remote.login(user, password)
    if remote_dir:
        remote.cwd(remote_dir)
    remote.retrbinary('RETR %s' % file_name, local.write, 1024)
    remote.quit()
    local.close()

# -------------------- (ftp_download) --------------------
