# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrmSrvMsg
###########################################################################

class FrmSrvMsg ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"aGaiMp - messaggi", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		szr_main = wx.BoxSizer( wx.VERTICAL )
		
		self.pnl_main = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		szr_srv_msg = wx.BoxSizer( wx.VERTICAL )
		
		szr_messages = wx.BoxSizer( wx.VERTICAL )
		
		self.txt_messages = wx.TextCtrl( self.pnl_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		szr_messages.Add( self.txt_messages, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		szr_srv_msg.Add( szr_messages, 1, wx.EXPAND, 5 )
		
		szr_buttons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_pause = wx.Button( self.pnl_main, wx.ID_ANY, u"Pausa", wx.DefaultPosition, wx.DefaultSize, 0 )
		szr_buttons.Add( self.btn_pause, 0, wx.ALL, 5 )
		
		self.btn_reset = wx.Button( self.pnl_main, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		szr_buttons.Add( self.btn_reset, 0, wx.ALL, 5 )
		
		
		szr_buttons.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn_close = wx.Button( self.pnl_main, wx.ID_ANY, u"Chiudi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_close.SetDefault() 
		szr_buttons.Add( self.btn_close, 0, wx.ALL, 5 )
		
		
		szr_srv_msg.Add( szr_buttons, 0, wx.EXPAND, 5 )
		
		
		self.pnl_main.SetSizer( szr_srv_msg )
		self.pnl_main.Layout()
		szr_srv_msg.Fit( self.pnl_main )
		szr_main.Add( self.pnl_main, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( szr_main )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_pause.Bind( wx.EVT_BUTTON, self.OnPause )
		self.btn_reset.Bind( wx.EVT_BUTTON, self.OnReset )
		self.btn_close.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPause( self, event ):
		event.Skip()
	
	def OnReset( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	

###########################################################################
## Class FrmSettings
###########################################################################

class FrmSettings ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"aGaiMp - impostazioni", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		szr_main = wx.BoxSizer( wx.VERTICAL )
		
		self.pnl_main = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		szr_srv_msg = wx.BoxSizer( wx.VERTICAL )
		
		szr_settings = wx.BoxSizer( wx.VERTICAL )
		
		self.nb_settings = wx.Notebook( self.pnl_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pnl_common = wx.Panel( self.nb_settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		szr_common = wx.BoxSizer( wx.VERTICAL )
		
		szr_uuid = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl_uuid = wx.StaticText( self.pnl_common, wx.ID_ANY, u"Importer ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_uuid.Wrap( -1 )
		szr_uuid.Add( self.lbl_uuid, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.param_uuid = wx.TextCtrl( self.pnl_common, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		szr_uuid.Add( self.param_uuid, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		szr_common.Add( szr_uuid, 0, wx.EXPAND, 5 )
		
		
		self.pnl_common.SetSizer( szr_common )
		self.pnl_common.Layout()
		szr_common.Fit( self.pnl_common )
		self.nb_settings.AddPage( self.pnl_common, u"aGaiMp", True )
		self.pnl_delta = wx.Panel( self.nb_settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		szr_delta = wx.BoxSizer( wx.VERTICAL )
		
		szr_ip_delta = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl_ip_delta = wx.StaticText( self.pnl_delta, wx.ID_ANY, u"IP DELTA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_ip_delta.Wrap( -1 )
		szr_ip_delta.Add( self.lbl_ip_delta, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.param_ip_delta = wx.TextCtrl( self.pnl_delta, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szr_ip_delta.Add( self.param_ip_delta, 1, wx.ALL, 5 )
		
		
		szr_delta.Add( szr_ip_delta, 0, wx.EXPAND, 5 )
		
		
		self.pnl_delta.SetSizer( szr_delta )
		self.pnl_delta.Layout()
		szr_delta.Fit( self.pnl_delta )
		self.nb_settings.AddPage( self.pnl_delta, u"DELTA", False )
		self.pnl_sigma = wx.Panel( self.nb_settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		szr_sigma = wx.BoxSizer( wx.VERTICAL )
		
		szr_ip_sigma = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl_ip_sigma = wx.StaticText( self.pnl_sigma, wx.ID_ANY, u"IP SIGMA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_ip_sigma.Wrap( -1 )
		szr_ip_sigma.Add( self.lbl_ip_sigma, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.param_ip_sigma = wx.TextCtrl( self.pnl_sigma, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szr_ip_sigma.Add( self.param_ip_sigma, 1, wx.ALL, 5 )
		
		
		szr_sigma.Add( szr_ip_sigma, 0, wx.EXPAND, 5 )
		
		
		self.pnl_sigma.SetSizer( szr_sigma )
		self.pnl_sigma.Layout()
		szr_sigma.Fit( self.pnl_sigma )
		self.nb_settings.AddPage( self.pnl_sigma, u"SIGMA", False )
		
		szr_settings.Add( self.nb_settings, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		szr_srv_msg.Add( szr_settings, 1, wx.EXPAND, 5 )
		
		szr_buttons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_save = wx.Button( self.pnl_main, wx.ID_ANY, u"Salva", wx.DefaultPosition, wx.DefaultSize, 0 )
		szr_buttons.Add( self.btn_save, 0, wx.ALL, 5 )
		
		
		szr_buttons.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn_cancel = wx.Button( self.pnl_main, wx.ID_ANY, u"Annulla", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_cancel.SetDefault() 
		szr_buttons.Add( self.btn_cancel, 0, wx.ALL, 5 )
		
		
		szr_srv_msg.Add( szr_buttons, 0, wx.EXPAND, 5 )
		
		
		self.pnl_main.SetSizer( szr_srv_msg )
		self.pnl_main.Layout()
		szr_srv_msg.Fit( self.pnl_main )
		szr_main.Add( self.pnl_main, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( szr_main )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_save.Bind( wx.EVT_BUTTON, self.OnSave )
		self.btn_cancel.Bind( wx.EVT_BUTTON, self.OnCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSave( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	

