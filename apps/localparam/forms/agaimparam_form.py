# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class ParametersForm
###########################################################################

class ParametersForm ( wx.Frame ):

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

		self.text_uuid = wx.StaticText( self.m_panel_main, wx.ID_ANY, u"Importer ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_uuid.Wrap( -1 )
		fgSizer_parameters.Add( self.text_uuid, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.param_uuid = wx.TextCtrl( self.m_panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer_parameters.Add( self.param_uuid, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_ip_delta = wx.StaticText( self.m_panel_main, wx.ID_ANY, u"IP DELTA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_ip_delta.Wrap( -1 )
		fgSizer_parameters.Add( self.text_ip_delta, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.param_ip_delta = wx.TextCtrl( self.m_panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_parameters.Add( self.param_ip_delta, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_ip_sigma = wx.StaticText( self.m_panel_main, wx.ID_ANY, u"IP SIGMA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_ip_sigma.Wrap( -1 )
		fgSizer_parameters.Add( self.text_ip_sigma, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.param_ip_sigma = wx.TextCtrl( self.m_panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_parameters.Add( self.param_ip_sigma, 0, wx.ALL|wx.EXPAND, 5 )

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
		self.m_button_salva.Bind( wx.EVT_BUTTON, self.OnSaveClick )
		self.m_button_annulla.Bind( wx.EVT_BUTTON, self.OnCancelClick )

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def OnSaveClick( self, event ):
		event.Skip()

	def OnCancelClick( self, event ):
		event.Skip()


