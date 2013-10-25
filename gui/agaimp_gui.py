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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"aGaiMp - servers messages", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
	

