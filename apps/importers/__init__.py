"""
Plug-in pattern per la gestione degli importer.

Il metodo __init__ di <sottoclasse 'type'> viene eseguito ogni volta che una classe *dichiara*:

 __metaclass__ = <sottoclasse 'type'>

NB: in fase di dichiarazione non di istanziamento!

Quindi, in questo caso, la prima volta viene eseguito in fase di dichiarazione della classe Importer
 e successivamente per ogni importer che eredita da questa.
"""

import threading

from settings import INSTALLED_IMPORTERS

from .controllers import ImportersPublisher, ImportersMessenger


_importers = {}  # importers installati


class ImporterMount(type):
    """
    Sistema di plugin per le classi che dichiarano
    __metaclass__ = ImporterMount
    """
    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        """
        @param name: Name of the class
        @param bases: Base classes (tuple)
        @param attrs: Attributes defined for the class
        """
        new_cls = type.__new__(cls, name, bases, attrs)
        if attrs['name']:  # classe Importer esclusa
            cls.REGISTRY[attrs['name']] = new_cls
        return new_cls


class Importer(object):
    """
    Importer importers.
    Tutti gli importers devono estendere questa classe,
    """
    __metaclass__ = ImporterMount

    name = ''  # ogni sottoclasse deve avere un nome diverso

    def __init__(self):
        self._thread = self._new_thread()

    def _new_thread(self):
        return threading.Thread(target=self.run)

    def run(self):
        """ Logica importers """
        pass

    def start(self):
        """ Avvia importer """
        if not self._thread.is_alive():
            self._thread = self._new_thread()
            self._thread.daemon = True
            self._thread.start()


def stop(name):
    global _importers
    del _importers[name]


def start(name):
    global _importers
    _importers[name].start()


publisher = ImportersPublisher('importers_publisher')  # Qui ci si registra per leggere i messaggi dei importers
messenger = ImportersMessenger(publisher)  # Qui gli importers possono lanciare messaggi

# Caricamento degli importers installati
for _importer in INSTALLED_IMPORTERS:
    __import__(_importer)

# Istanziamento degli importers caricati
for _class_name, _class_type in ImporterMount.REGISTRY.items():
    _importers[_class_name] = _class_type()

