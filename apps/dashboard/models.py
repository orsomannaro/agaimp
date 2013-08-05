"""
Register pattern per dashboad (cruscotti)


If you put the PluginMount.__init__ logic in PluginMount.__new__ it is called whenver a new instance of a Plugin derived class is created.
(http://stackoverflow.com/questions/14510286/plugin-architecture-plugin-manager-vs-inspecting-from-plugins-import)
"""


class DashboardMount(type):
    """
    Colleziona classi derivate da Server.
    _servers: lista delle classi
    """
    def __init__(cls, name, bases, attrs):
        """ Called when a Dashboard derived class is imported
        """
        if not hasattr(cls, '_dashboards'):
            cls._dashboards = []
        else:
            cls._dashboards.append(cls)

    def get_dashboards(self, *args, **kwargs):
        """
        Torna una lista di ISTANZE delle sottoclassi Dashboard registrate.
        (nulla vieta di farlo direttamente nel codice)
        """
        return [d(*args, **kwargs) for d in self._dashboards]


class Dashboard(object):
    """
    Una app che desidera inserire notifiche nella Dashboard deve:
    - estendere questa classe
    - impostare l'attibuto 'name'
    - implementare il metodo .get_notices()
    """
    __metaclass__ = DashboardMount

    name = ''

    def get_notices(self):
        """
        Ritorna una LISTA di dizionari.
        Ogni DIZIONARIO costituisce una notifica
         e deve essere composto dalle seguenti chiavi:
         - message : messaggio da visualizzare
         - action  : link da associare al messaggio
         - auth    : livello minimo del destinatario
        """
        return []
