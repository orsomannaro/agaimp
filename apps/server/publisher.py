"""
Sistema di comunicazione dei server secondo il pattern Publisher/Subscriber.

I server possono inviare messaggi tramite il loro attributo 'publisher'
 che corrisponde all'oggetto 'servers_publisher' qui istanziato.
"""

from libs.patterns import Publisher


servers_publisher = Publisher('servers_publisher')  # messaggi dei server


# ----- DEBUG -----
#class SubscriberStdOut(object):
#    """ Stampa i messaggi dei Publisher su console
#    """
#    def publish(self, message):
#        print '%s %s: %s' % (message[SRV_NAME], message[SRV_MSG_LVL], message[SRV_MSG_TXT])
#
#servers_publisher.subscribe(SubscriberStdOut())
# -----------------
