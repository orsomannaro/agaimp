
# -------------------- Messenger --------------------
# Istanziando Messenger si possono inviare Message via publisher

import datetime


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
