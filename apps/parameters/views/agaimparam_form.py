# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class Paramenters
###########################################################################

class Paramenters ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"aGain import - parametri", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer_main = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel_main = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_body = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer_parameters = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer_parameters.AddGrowableCol( 1 )
		fgSizer_parameters.SetFlexibleDirection( wx.BOTH )
		fgSizer_parameters.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText_id = wx.StaticText( self.m_panel_main, wx.ID_ANY, u"Importer ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_id.Wrap( -1 )
		fgSizer_parameters.Add( self.m_staticText_id, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl_id = wx.TextCtrl( self.m_panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer_parameters.Add( self.m_textCtrl_id, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText_username = wx.StaticText( self.m_panel_main, wx.ID_ANY, u"username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_username.Wrap( -1 )
		fgSizer_parameters.Add( self.m_staticText_username, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl_username = wx.TextCtrl( self.m_panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_parameters.Add( self.m_textCtrl_username, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText_password = wx.StaticText( self.m_panel_main, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_password.Wrap( -1 )
		fgSizer_parameters.Add( self.m_staticText_password, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl_password = wx.TextCtrl( self.m_panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_parameters.Add( self.m_textCtrl_password, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer_body.Add( fgSizer_parameters, 1, wx.EXPAND, 5 )
		
		self.m_staticline_body = wx.StaticLine( self.m_panel_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_body.Add( self.m_staticline_body, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer_button = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button_salva = wx.Button( self.m_panel_main, wx.ID_ANY, u"Salva", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_button.Add( self.m_button_salva, 0, wx.ALL, 5 )
		
		self.m_button_annulla = wx.Button( self.m_panel_main, wx.ID_ANY, u"Annulla", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_button.Add( self.m_button_annulla, 0, wx.ALL, 5 )
		
		bSizer_body.Add( bSizer_button, 0, wx.ALIGN_RIGHT, 5 )
		
		self.m_panel_main.SetSizer( bSizer_body )
		self.m_panel_main.Layout()
		bSizer_body.Fit( self.m_panel_main )
		bSizer_main.Add( self.m_panel_main, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer_main )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button_salva.Bind( wx.EVT_BUTTON, self.OnSalvaClick )
		self.m_button_annulla.Bind( wx.EVT_BUTTON, self.OnAnnullaClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSalvaClick( self, event ):
		event.Skip()
	
	def OnAnnullaClick( self, event ):
		event.Skip()
	

