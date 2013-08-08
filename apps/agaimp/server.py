import wx

from apps.importer import Server
from wx.lib.pubsub.pub import Publisher


SERVER_TOPIC = 'server.messages'  # Publisher topic


class wxServer(Server):

    def send_message(self, message):
        """ Send message to publisher
        """
        wx.CallAfter(Publisher().sendMessage, SERVER_TOPIC, message)
