

def get_pwd(uuid):
    """
    Calcola la password in base all'uuid dell'installazione.
    :param uuid: uuid dell'installazione
    :return: password
    """
    import hashlib
    return str(hashlib.sha1(uuid).hexdigest())
