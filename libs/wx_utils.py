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
