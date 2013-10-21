import wx
import threading
import Queue

from wx.lib.newevent import NewEvent


myNewMsg, EVT_NEW_MSG = NewEvent()  # messaggi disponibili (bind con OnUpdateOutputWindow)
myMsgShown, EVT_MSG_SHOWN = NewEvent()  # messaggi visualizzati (bind con OnWorkerDone)



class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 300))
        self.requestQ = Queue.Queue()
        self.resultQ = Queue.Queue()

        #widgets
        p = wx.Panel(self)

        # controllo contenete il messaggio
        self.output_window = wx.TextCtrl(p, -1, style=wx.TE_AUTO_SCROLL | wx.TE_MULTILINE | wx.TE_READONLY)

        # timer
        self.output_window_timer = wx.Timer(self.output_window, -1)
        self.output_window.Bind(wx.EVT_TIMER, self.OnProcessPendingOutputWindowEvents)  # gestione timeout timer
        # TODO: capire bene a cosa serve il timer

        #frame sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.output_window, 10, wx.EXPAND)
        p.SetSizer(sizer)

        #events
        self.output_window.Bind(EVT_NEW_MSG, self.OnUpdateOutputWindow)  # gestione evento scatenato da SysOutListener
        self.Bind(EVT_MSG_SHOWN, self.OnWorkerDone)  # gestione evento scatenato da Worker.run

        #thread
        self.worker = Worker(self, self.requestQ, self.resultQ)

    def OnUpdateOutputWindow(self, event):
        value = '%s\n' % event.text
        self.output_window.AppendText(value)

    def OnBeginTest(self, event):
        self.output_window_timer.Start(50)  # da tempo a output_window di elaborare la coda di eventi scatenati
                                            # (tipicamente EVT_NEW_MSG e quindi OnUpdateOutputWindow,
                                            # cioe' le richieste di visualizzare un messaggio)

    def OnWorkerDone(self, event):  # bind con EVT_MSG_SHOWN
        self.output_window_timer.Stop()  # il timer non serve quando non ci sono lavori in coda

    def OnProcessPendingOutputWindowEvents(self, event):
        # ProcessPendingEvents process all events in the Pending Events list
        # It is necessary to call this function to process posted events.
        # Processes any waiting events, and any arriving during processing, then returns leaving the event queue empty.
        # ProcessPendingEvents only takes care of wx events that have been added to the pending queue, it does not process pending system events.
        self.output_window.ProcessPendingEvents()


class Worker(threading.Thread):
    """
    Thread in ascolto su requestQ.
    Avvisa che ha finito pushando su resultQ
    """

    requestID = 0

    def __init__(self, parent, requestQ, resultQ, **kwds):
        threading.Thread.__init__(self, **kwds)
        self.setDaemon(True)
        self.requestQ = requestQ
        self.resultQ = resultQ
        self.start()

    def beginTest(self, callable, *args, **kwds):
        Worker.requestID += 1
        self.requestQ.put((Worker.requestID, callable, args, kwds))
        return Worker.requestID

    def run(self):
        while True:
            requestID, callable, args, kwds = self.requestQ.get()  # suspend the thread untill the callable returns
            self.resultQ.put((requestID, callable(*args, **kwds)))  # tell us that the process has finished its task
            evt = myMsgShown()
            wx.PostEvent(wx.GetApp().frame, evt)  # invia evento 'messaggi visualizzati' a MyApp.frame


class SysOutListener:
    def publish(self, string):
        evt = myNewMsg(text=string)
        wx.PostEvent(wx.GetApp().frame.output_window, evt)  # invia evento 'messaggi disponibili' a MyApp.frame.output_window


sol = SysOutListener()