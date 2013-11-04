import ftplib
import os


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
