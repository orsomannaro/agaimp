"""
Sistema di comunicazione dei server secondo il pattern Publisher/Subscriber.

I server possono inviare messaggi tramite il loro attributo 'publisher'
 che corrisponde all'oggetto 'servers_publisher' qui istanziato.

I messaggi pubblicati dei server devono essere dizionari composti dalle seguenti chiavi;
   SRV_NAME: nome del server (SIGMA, DELTA, ...)
SRV_MSG_LVL: tipo di messaggio (message|warning|error|...)
SRV_MSG_HMS: ora del messaggio (ore, minuti, secondi)
SRV_MSG_TXT: testo del messaggio
"""


from libs.patterns import Publisher


SRV_NAME = 'server_name'
SRV_MSG_LVL = 'message_level'
SRV_MSG_HMS = 'message_time'
SRV_MSG_TXT = 'message_text'

LOG_SRV_MSG_LVL = 'log'
WRN_SRV_MSG_LVL = 'warning'
ERR_SRV_MSG_LVL = 'error'


servers_publisher = Publisher('servers_publisher')  # messaggi dei server


# ===== DEBUG =====

#class SubscriberStdOut(object):
#    """ Stampa i messaggi dei Publisher su console
#    """
#    def publish(self, message):
#        print '%s %s: %s' % (message[SRV_NAME], message[SRV_MSG_LVL], message[SRV_MSG_TXT])
#
#servers_publisher.subscribe(SubscriberStdOut())

# ==========
