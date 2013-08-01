"""
Register pattern per dashboad (cruscotti)
"""

class DashboardMount(type):

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'dashboards'):
            # questa parte viene eseguita solo quando si scrive
            # una classe dichiarando DashboardMount come sua __metaclass__
            cls.dashboards = []
        else:
            # questa parte viene eseguita ogni volta che poi si istanzia
            # un oggetto della classe avente DashboardMount come  __metaclass__
            cls.dashboards.append(cls)

    def get_dashboards(self, *args, **kwargs):
        """
        Torna una lista di ISTANZE delle sottoclassi Dashboard registrate.
        (nulla vieta di farlo direttamente nel codice)
        """
        return [d(*args, **kwargs) for d in self.dashboards]


class Dashboard(object):
    """
    Una app che desidera inserire notifiche nella Dashboard deve:
    - estendere questa classe
    - impostare l'attibuto 'name'
    - implementare il metodo .get_notices()
    """
    __metaclass__ = DashboardMount

    name = ''

    def get_notices(self, request):
        """
        Ritorna una LISTA di dizionari.
        Ogni DIZIONARIO costituisce una notifica
         e deve essere composto dalle seguenti chiavi:
         - message : messaggio da visualizzare
         - action  : link da associare al messaggio
         - auth    : livello minimo del destinatario
        """
        return []


dashboards = Dashboard.get_dashboards()
