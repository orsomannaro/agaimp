import Queue
import os
import wx


def get_wx_icon(full_path):
    file_ext = os.path.splitext(full_path)[1]
    if file_ext == '.ico':
        icon = wx.Icon(full_path, wx.BITMAP_TYPE_ICO)
        return icon
    elif file_ext == '.png':
        icon = wx.Icon(full_path, wx.BITMAP_TYPE_PNG)
        return icon
    raise NotImplementedError("Unknown icon type")


def wx_call(f):
    """
    http://radekpodgorny.blogspot.cz/2012/12/working-with-wxpython-in-separate-thread.html
    """
    def return_to_queue(func, q, *args, **kwargs):
        ret = func(*args)
        q.put(ret)

    def wrapper(*args, **kwargs):
        q = Queue.Queue()
        wx.CallAfter(return_to_queue, f, q, *args, **kwargs)
        return q.get()

    return wrapper
