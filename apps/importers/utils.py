import ftplib
import hashlib
import os


# -------------------- md5 --------------------
def md5(file_path):
    """ Calcola md5 anche di file di grandi dimensioni
    @param file_path: file di cui calcolare md5
    """
    BLOCKSIZE = 65536
    hasher = hashlib.md5()

    with open(file_path, 'rb') as f:
        buf = f.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(BLOCKSIZE)
    return hasher.hexdigest()

# -------------------- (md5) --------------------


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
