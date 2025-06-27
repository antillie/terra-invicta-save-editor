# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Terra Invicta Save Editor", pos = wx.DefaultPosition, size = wx.Size( 840,710 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.menubar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.open = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Open"+ u"\t" + u"CTRL+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.open )

		self.save = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Save"+ u"\t" + u"CTRL+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.save )

		self.saveas = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Save As"+ u"\t" + u"CTRL+SHIFT+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.saveas )

		self.quit = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Quit"+ u"\t" + u"CTRL+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.quit )

		self.menubar.Append( self.file_menu, u"File" )

		self.help_menu = wx.Menu()
		self.github = wx.MenuItem( self.help_menu, wx.ID_ANY, u"Open Github Repository", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.Append( self.github )

		self.about = wx.MenuItem( self.help_menu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.Append( self.about )

		self.menubar.Append( self.help_menu, u"Help" )

		self.SetMenuBar( self.menubar )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		fgSizer61 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer61.SetFlexibleDirection( wx.BOTH )
		fgSizer61.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.app_tabs = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.app_tabs.SetMinSize( wx.Size( 840,-1 ) )

		self.research_panel = wx.Panel( self.app_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText13 = wx.StaticText( self.research_panel, wx.ID_ANY, u"Current Project", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		fgSizer1.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self.research_panel, wx.ID_ANY, u"Current Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )

		research_slot1Choices = []
		self.research_slot1 = wx.Choice( self.research_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, research_slot1Choices, 0 )
		self.research_slot1.SetSelection( 0 )
		self.research_slot1.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer1.Add( self.research_slot1, 0, wx.ALL, 5 )

		self.research1_progress = wx.TextCtrl( self.research_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.research1_progress, 0, wx.ALL, 5 )

		research_slot2Choices = []
		self.research_slot2 = wx.Choice( self.research_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, research_slot2Choices, 0 )
		self.research_slot2.SetSelection( 0 )
		self.research_slot2.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer1.Add( self.research_slot2, 0, wx.ALL, 5 )

		self.research2_progress = wx.TextCtrl( self.research_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.research2_progress, 0, wx.ALL, 5 )

		research_slot3Choices = []
		self.research_slot3 = wx.Choice( self.research_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, research_slot3Choices, 0 )
		self.research_slot3.SetSelection( 0 )
		self.research_slot3.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer1.Add( self.research_slot3, 0, wx.ALL, 5 )

		self.research3_progress = wx.TextCtrl( self.research_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.research3_progress, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.research_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self.research_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText587 = wx.StaticText( self.research_panel, wx.ID_ANY, u"Rouge Warheads:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText587.Wrap( -1 )

		fgSizer1.Add( self.m_staticText587, 0, wx.ALL, 5 )

		self.rouge_nuke_count = wx.SpinCtrl( self.research_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		fgSizer1.Add( self.rouge_nuke_count, 0, wx.ALL, 5 )


		self.research_panel.SetSizer( fgSizer1 )
		self.research_panel.Layout()
		fgSizer1.Fit( self.research_panel )
		self.app_tabs.AddPage( self.research_panel, u"Global Research", True )
		self.resist_panel = wx.Panel( self.app_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )

		self.player_flag = wx.CheckBox( self.resist_panel, wx.ID_ANY, u"Player Faction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.player_flag, 0, wx.ALL, 5 )

		self.m_staticText5811 = wx.StaticText( self.resist_panel, wx.ID_ANY, u"Alien Hate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5811.Wrap( -1 )

		gSizer1.Add( self.m_staticText5811, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self.resist_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer1.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )


		bSizer3.Add( gSizer1, 1, wx.EXPAND, 5 )

		self.resist_sub_tabs = wx.Notebook( self.resist_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_resource_panel = wx.Panel( self.resist_sub_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Money", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.resist_money = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_money, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Influence", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.resist_influence = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_influence, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Ops", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.resist_ops = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_ops, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Boost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.resist_boost = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_boost, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Water", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.resist_water = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_water, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Volatiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.resist_volatiles = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_volatiles, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Base Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.resist_basemetals = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_basemetals, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Noble Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.resist_noblemetals = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_noblemetals, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Fissiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.resist_fissiles = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_fissiles, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Exotics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.resist_exotics = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_exotics, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self.resist_resource_panel, wx.ID_ANY, u"Antimatter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.resist_antimatter = wx.TextCtrl( self.resist_resource_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.resist_antimatter, 0, wx.ALL, 5 )


		self.resist_resource_panel.SetSizer( fgSizer2 )
		self.resist_resource_panel.Layout()
		fgSizer2.Fit( self.resist_resource_panel )
		self.resist_sub_tabs.AddPage( self.resist_resource_panel, u"Resources", True )
		self.resist_projects = wx.Panel( self.resist_sub_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText15 = wx.StaticText( self.resist_projects, wx.ID_ANY, u"Active Project", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText15.Wrap( -1 )

		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self.resist_projects, wx.ID_ANY, u"Current Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.resist_project1 = wx.StaticText( self.resist_projects, wx.ID_ANY, u"Project 1 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project1.Wrap( -1 )

		fgSizer3.Add( self.resist_project1, 0, wx.ALL, 5 )

		self.resist_project1_progress = wx.TextCtrl( self.resist_projects, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.resist_project1_progress, 0, wx.ALL, 5 )

		self.resist_project2 = wx.StaticText( self.resist_projects, wx.ID_ANY, u"Project 2 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project2.Wrap( -1 )

		fgSizer3.Add( self.resist_project2, 0, wx.ALL, 5 )

		self.resist_project2_progress = wx.TextCtrl( self.resist_projects, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.resist_project2_progress, 0, wx.ALL, 5 )

		self.resist_project3 = wx.StaticText( self.resist_projects, wx.ID_ANY, u"Project 3 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project3.Wrap( -1 )

		fgSizer3.Add( self.resist_project3, 0, wx.ALL, 5 )

		self.resist_project3_progress = wx.TextCtrl( self.resist_projects, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.resist_project3_progress, 0, wx.ALL, 5 )


		self.resist_projects.SetSizer( fgSizer3 )
		self.resist_projects.Layout()
		fgSizer3.Fit( self.resist_projects )
		self.resist_sub_tabs.AddPage( self.resist_projects, u"Project Research", False )
		self.resist_council_1 = wx.Panel( self.resist_sub_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname.Wrap( -1 )

		fgSizer4.Add( self.resist_c_fname, 0, wx.ALL, 5 )

		self.resist_c_lname = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname.Wrap( -1 )

		fgSizer4.Add( self.resist_c_lname, 0, wx.ALL, 5 )

		self.m_staticText84 = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer4.Add( self.m_staticText84, 0, wx.ALL, 5 )

		resist_c_classChoices = []
		self.resist_c_class = wx.Choice( self.resist_council_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_classChoices, 0 )
		self.resist_c_class.SetSelection( 0 )
		fgSizer4.Add( self.resist_c_class, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		fgSizer4.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.resist_c_persuasion = wx.TextCtrl( self.resist_council_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.resist_c_persuasion, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		fgSizer4.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.resist_c_investigation = wx.TextCtrl( self.resist_council_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.resist_c_investigation, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		fgSizer4.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.resist_c_espionage = wx.TextCtrl( self.resist_council_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.resist_c_espionage, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		fgSizer4.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.resist_c_command = wx.TextCtrl( self.resist_council_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.resist_c_command, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		fgSizer4.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.resist_c_administration = wx.TextCtrl( self.resist_council_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.resist_c_administration, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer4.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.resist_c_science = wx.TextCtrl( self.resist_council_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.resist_c_science, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer4.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.resist_c_security = wx.TextCtrl( self.resist_council_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.resist_c_security, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self.resist_council_1, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer4.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.resist_c_loyalty = wx.TextCtrl( self.resist_council_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.resist_c_loyalty, 0, wx.ALL, 5 )


		self.resist_council_1.SetSizer( fgSizer4 )
		self.resist_council_1.Layout()
		fgSizer4.Fit( self.resist_council_1 )
		self.resist_sub_tabs.AddPage( self.resist_council_1, u"Councilor 1", False )
		self.resist_council_2 = wx.Panel( self.resist_sub_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer41 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname1 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname1.Wrap( -1 )

		fgSizer41.Add( self.resist_c_fname1, 0, wx.ALL, 5 )

		self.resist_c_lname1 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname1.Wrap( -1 )

		fgSizer41.Add( self.resist_c_lname1, 0, wx.ALL, 5 )

		self.m_staticText841 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText841.Wrap( -1 )

		fgSizer41.Add( self.m_staticText841, 0, wx.ALL, 5 )

		resist_c_class1Choices = []
		self.resist_c_class1 = wx.Choice( self.resist_council_2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class1Choices, 0 )
		self.resist_c_class1.SetSelection( 0 )
		fgSizer41.Add( self.resist_c_class1, 0, wx.ALL, 5 )

		self.m_staticText201 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )

		fgSizer41.Add( self.m_staticText201, 0, wx.ALL, 5 )

		self.resist_c_persuasion1 = wx.TextCtrl( self.resist_council_2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer41.Add( self.resist_c_persuasion1, 0, wx.ALL, 5 )

		self.m_staticText211 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		fgSizer41.Add( self.m_staticText211, 0, wx.ALL, 5 )

		self.resist_c_investigation1 = wx.TextCtrl( self.resist_council_2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer41.Add( self.resist_c_investigation1, 0, wx.ALL, 5 )

		self.m_staticText221 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		fgSizer41.Add( self.m_staticText221, 0, wx.ALL, 5 )

		self.resist_c_espionage1 = wx.TextCtrl( self.resist_council_2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer41.Add( self.resist_c_espionage1, 0, wx.ALL, 5 )

		self.m_staticText231 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )

		fgSizer41.Add( self.m_staticText231, 0, wx.ALL, 5 )

		self.resist_c_command1 = wx.TextCtrl( self.resist_council_2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer41.Add( self.resist_c_command1, 0, wx.ALL, 5 )

		self.m_staticText241 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText241.Wrap( -1 )

		fgSizer41.Add( self.m_staticText241, 0, wx.ALL, 5 )

		self.resist_c_administration1 = wx.TextCtrl( self.resist_council_2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer41.Add( self.resist_c_administration1, 0, wx.ALL, 5 )

		self.m_staticText251 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )

		fgSizer41.Add( self.m_staticText251, 0, wx.ALL, 5 )

		self.resist_c_science1 = wx.TextCtrl( self.resist_council_2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer41.Add( self.resist_c_science1, 0, wx.ALL, 5 )

		self.m_staticText261 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText261.Wrap( -1 )

		fgSizer41.Add( self.m_staticText261, 0, wx.ALL, 5 )

		self.resist_c_security1 = wx.TextCtrl( self.resist_council_2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer41.Add( self.resist_c_security1, 0, wx.ALL, 5 )

		self.m_staticText271 = wx.StaticText( self.resist_council_2, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText271.Wrap( -1 )

		fgSizer41.Add( self.m_staticText271, 0, wx.ALL, 5 )

		self.resist_c_loyalty1 = wx.TextCtrl( self.resist_council_2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer41.Add( self.resist_c_loyalty1, 0, wx.ALL, 5 )


		self.resist_council_2.SetSizer( fgSizer41 )
		self.resist_council_2.Layout()
		fgSizer41.Fit( self.resist_council_2 )
		self.resist_sub_tabs.AddPage( self.resist_council_2, u"Councilor 2", False )
		self.resist_council_3 = wx.Panel( self.resist_sub_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer42 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname2 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname2.Wrap( -1 )

		fgSizer42.Add( self.resist_c_fname2, 0, wx.ALL, 5 )

		self.resist_c_lname2 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname2.Wrap( -1 )

		fgSizer42.Add( self.resist_c_lname2, 0, wx.ALL, 5 )

		self.m_staticText842 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText842.Wrap( -1 )

		fgSizer42.Add( self.m_staticText842, 0, wx.ALL, 5 )

		resist_c_class2Choices = []
		self.resist_c_class2 = wx.Choice( self.resist_council_3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class2Choices, 0 )
		self.resist_c_class2.SetSelection( 0 )
		fgSizer42.Add( self.resist_c_class2, 0, wx.ALL, 5 )

		self.m_staticText202 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText202.Wrap( -1 )

		fgSizer42.Add( self.m_staticText202, 0, wx.ALL, 5 )

		self.resist_c_persuasion2 = wx.TextCtrl( self.resist_council_3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.resist_c_persuasion2, 0, wx.ALL, 5 )

		self.m_staticText212 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		fgSizer42.Add( self.m_staticText212, 0, wx.ALL, 5 )

		self.resist_c_investigation2 = wx.TextCtrl( self.resist_council_3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.resist_c_investigation2, 0, wx.ALL, 5 )

		self.m_staticText222 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText222.Wrap( -1 )

		fgSizer42.Add( self.m_staticText222, 0, wx.ALL, 5 )

		self.resist_c_espionage2 = wx.TextCtrl( self.resist_council_3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.resist_c_espionage2, 0, wx.ALL, 5 )

		self.m_staticText232 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText232.Wrap( -1 )

		fgSizer42.Add( self.m_staticText232, 0, wx.ALL, 5 )

		self.resist_c_command2 = wx.TextCtrl( self.resist_council_3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.resist_c_command2, 0, wx.ALL, 5 )

		self.m_staticText242 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText242.Wrap( -1 )

		fgSizer42.Add( self.m_staticText242, 0, wx.ALL, 5 )

		self.resist_c_administration2 = wx.TextCtrl( self.resist_council_3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.resist_c_administration2, 0, wx.ALL, 5 )

		self.m_staticText252 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText252.Wrap( -1 )

		fgSizer42.Add( self.m_staticText252, 0, wx.ALL, 5 )

		self.resist_c_science2 = wx.TextCtrl( self.resist_council_3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.resist_c_science2, 0, wx.ALL, 5 )

		self.m_staticText262 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText262.Wrap( -1 )

		fgSizer42.Add( self.m_staticText262, 0, wx.ALL, 5 )

		self.resist_c_security2 = wx.TextCtrl( self.resist_council_3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.resist_c_security2, 0, wx.ALL, 5 )

		self.m_staticText272 = wx.StaticText( self.resist_council_3, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText272.Wrap( -1 )

		fgSizer42.Add( self.m_staticText272, 0, wx.ALL, 5 )

		self.resist_c_loyalty2 = wx.TextCtrl( self.resist_council_3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.resist_c_loyalty2, 0, wx.ALL, 5 )


		self.resist_council_3.SetSizer( fgSizer42 )
		self.resist_council_3.Layout()
		fgSizer42.Fit( self.resist_council_3 )
		self.resist_sub_tabs.AddPage( self.resist_council_3, u"Councilor 3", False )
		self.resist_council_4 = wx.Panel( self.resist_sub_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer43 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer43.SetFlexibleDirection( wx.BOTH )
		fgSizer43.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname3 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname3.Wrap( -1 )

		fgSizer43.Add( self.resist_c_fname3, 0, wx.ALL, 5 )

		self.resist_c_lname3 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname3.Wrap( -1 )

		fgSizer43.Add( self.resist_c_lname3, 0, wx.ALL, 5 )

		self.m_staticText843 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText843.Wrap( -1 )

		fgSizer43.Add( self.m_staticText843, 0, wx.ALL, 5 )

		resist_c_class3Choices = []
		self.resist_c_class3 = wx.Choice( self.resist_council_4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class3Choices, 0 )
		self.resist_c_class3.SetSelection( 0 )
		fgSizer43.Add( self.resist_c_class3, 0, wx.ALL, 5 )

		self.m_staticText203 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText203.Wrap( -1 )

		fgSizer43.Add( self.m_staticText203, 0, wx.ALL, 5 )

		self.resist_c_persuasion3 = wx.TextCtrl( self.resist_council_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer43.Add( self.resist_c_persuasion3, 0, wx.ALL, 5 )

		self.m_staticText213 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )

		fgSizer43.Add( self.m_staticText213, 0, wx.ALL, 5 )

		self.resist_c_investigation3 = wx.TextCtrl( self.resist_council_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer43.Add( self.resist_c_investigation3, 0, wx.ALL, 5 )

		self.m_staticText223 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText223.Wrap( -1 )

		fgSizer43.Add( self.m_staticText223, 0, wx.ALL, 5 )

		self.resist_c_espionage3 = wx.TextCtrl( self.resist_council_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer43.Add( self.resist_c_espionage3, 0, wx.ALL, 5 )

		self.m_staticText233 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText233.Wrap( -1 )

		fgSizer43.Add( self.m_staticText233, 0, wx.ALL, 5 )

		self.resist_c_command3 = wx.TextCtrl( self.resist_council_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer43.Add( self.resist_c_command3, 0, wx.ALL, 5 )

		self.m_staticText243 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText243.Wrap( -1 )

		fgSizer43.Add( self.m_staticText243, 0, wx.ALL, 5 )

		self.resist_c_administration3 = wx.TextCtrl( self.resist_council_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer43.Add( self.resist_c_administration3, 0, wx.ALL, 5 )

		self.m_staticText253 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText253.Wrap( -1 )

		fgSizer43.Add( self.m_staticText253, 0, wx.ALL, 5 )

		self.resist_c_science3 = wx.TextCtrl( self.resist_council_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer43.Add( self.resist_c_science3, 0, wx.ALL, 5 )

		self.m_staticText263 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText263.Wrap( -1 )

		fgSizer43.Add( self.m_staticText263, 0, wx.ALL, 5 )

		self.resist_c_security3 = wx.TextCtrl( self.resist_council_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer43.Add( self.resist_c_security3, 0, wx.ALL, 5 )

		self.m_staticText273 = wx.StaticText( self.resist_council_4, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText273.Wrap( -1 )

		fgSizer43.Add( self.m_staticText273, 0, wx.ALL, 5 )

		self.resist_c_loyalty3 = wx.TextCtrl( self.resist_council_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer43.Add( self.resist_c_loyalty3, 0, wx.ALL, 5 )


		self.resist_council_4.SetSizer( fgSizer43 )
		self.resist_council_4.Layout()
		fgSizer43.Fit( self.resist_council_4 )
		self.resist_sub_tabs.AddPage( self.resist_council_4, u"Councilor 4", False )
		self.resist_council_5 = wx.Panel( self.resist_sub_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer44 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer44.SetFlexibleDirection( wx.BOTH )
		fgSizer44.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname4 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname4.Wrap( -1 )

		fgSizer44.Add( self.resist_c_fname4, 0, wx.ALL, 5 )

		self.resist_c_lname4 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname4.Wrap( -1 )

		fgSizer44.Add( self.resist_c_lname4, 0, wx.ALL, 5 )

		self.m_staticText844 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText844.Wrap( -1 )

		fgSizer44.Add( self.m_staticText844, 0, wx.ALL, 5 )

		resist_c_class4Choices = []
		self.resist_c_class4 = wx.Choice( self.resist_council_5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class4Choices, 0 )
		self.resist_c_class4.SetSelection( 0 )
		fgSizer44.Add( self.resist_c_class4, 0, wx.ALL, 5 )

		self.m_staticText204 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText204.Wrap( -1 )

		fgSizer44.Add( self.m_staticText204, 0, wx.ALL, 5 )

		self.resist_c_persuasion4 = wx.TextCtrl( self.resist_council_5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.resist_c_persuasion4, 0, wx.ALL, 5 )

		self.m_staticText214 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214.Wrap( -1 )

		fgSizer44.Add( self.m_staticText214, 0, wx.ALL, 5 )

		self.resist_c_investigation4 = wx.TextCtrl( self.resist_council_5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.resist_c_investigation4, 0, wx.ALL, 5 )

		self.m_staticText224 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText224.Wrap( -1 )

		fgSizer44.Add( self.m_staticText224, 0, wx.ALL, 5 )

		self.resist_c_espionage4 = wx.TextCtrl( self.resist_council_5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.resist_c_espionage4, 0, wx.ALL, 5 )

		self.m_staticText234 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText234.Wrap( -1 )

		fgSizer44.Add( self.m_staticText234, 0, wx.ALL, 5 )

		self.resist_c_command4 = wx.TextCtrl( self.resist_council_5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.resist_c_command4, 0, wx.ALL, 5 )

		self.m_staticText244 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText244.Wrap( -1 )

		fgSizer44.Add( self.m_staticText244, 0, wx.ALL, 5 )

		self.resist_c_administration4 = wx.TextCtrl( self.resist_council_5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.resist_c_administration4, 0, wx.ALL, 5 )

		self.m_staticText254 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText254.Wrap( -1 )

		fgSizer44.Add( self.m_staticText254, 0, wx.ALL, 5 )

		self.resist_c_science4 = wx.TextCtrl( self.resist_council_5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.resist_c_science4, 0, wx.ALL, 5 )

		self.m_staticText264 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText264.Wrap( -1 )

		fgSizer44.Add( self.m_staticText264, 0, wx.ALL, 5 )

		self.resist_c_security4 = wx.TextCtrl( self.resist_council_5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.resist_c_security4, 0, wx.ALL, 5 )

		self.m_staticText274 = wx.StaticText( self.resist_council_5, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText274.Wrap( -1 )

		fgSizer44.Add( self.m_staticText274, 0, wx.ALL, 5 )

		self.resist_c_loyalty4 = wx.TextCtrl( self.resist_council_5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.resist_c_loyalty4, 0, wx.ALL, 5 )


		self.resist_council_5.SetSizer( fgSizer44 )
		self.resist_council_5.Layout()
		fgSizer44.Fit( self.resist_council_5 )
		self.resist_sub_tabs.AddPage( self.resist_council_5, u"Councilor 5", False )
		self.resist_council_6 = wx.Panel( self.resist_sub_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer45 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer45.SetFlexibleDirection( wx.BOTH )
		fgSizer45.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname5 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname5.Wrap( -1 )

		fgSizer45.Add( self.resist_c_fname5, 0, wx.ALL, 5 )

		self.resist_c_lname5 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname5.Wrap( -1 )

		fgSizer45.Add( self.resist_c_lname5, 0, wx.ALL, 5 )

		self.m_staticText845 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText845.Wrap( -1 )

		fgSizer45.Add( self.m_staticText845, 0, wx.ALL, 5 )

		resist_c_class5Choices = []
		self.resist_c_class5 = wx.Choice( self.resist_council_6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class5Choices, 0 )
		self.resist_c_class5.SetSelection( 0 )
		fgSizer45.Add( self.resist_c_class5, 0, wx.ALL, 5 )

		self.m_staticText205 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText205.Wrap( -1 )

		fgSizer45.Add( self.m_staticText205, 0, wx.ALL, 5 )

		self.resist_c_persuasion5 = wx.TextCtrl( self.resist_council_6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.resist_c_persuasion5, 0, wx.ALL, 5 )

		self.m_staticText215 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText215.Wrap( -1 )

		fgSizer45.Add( self.m_staticText215, 0, wx.ALL, 5 )

		self.resist_c_investigation5 = wx.TextCtrl( self.resist_council_6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.resist_c_investigation5, 0, wx.ALL, 5 )

		self.m_staticText225 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText225.Wrap( -1 )

		fgSizer45.Add( self.m_staticText225, 0, wx.ALL, 5 )

		self.resist_c_espionage5 = wx.TextCtrl( self.resist_council_6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.resist_c_espionage5, 0, wx.ALL, 5 )

		self.m_staticText235 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText235.Wrap( -1 )

		fgSizer45.Add( self.m_staticText235, 0, wx.ALL, 5 )

		self.resist_c_command5 = wx.TextCtrl( self.resist_council_6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.resist_c_command5, 0, wx.ALL, 5 )

		self.m_staticText245 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText245.Wrap( -1 )

		fgSizer45.Add( self.m_staticText245, 0, wx.ALL, 5 )

		self.resist_c_administration5 = wx.TextCtrl( self.resist_council_6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.resist_c_administration5, 0, wx.ALL, 5 )

		self.m_staticText255 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText255.Wrap( -1 )

		fgSizer45.Add( self.m_staticText255, 0, wx.ALL, 5 )

		self.resist_c_science5 = wx.TextCtrl( self.resist_council_6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.resist_c_science5, 0, wx.ALL, 5 )

		self.m_staticText265 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText265.Wrap( -1 )

		fgSizer45.Add( self.m_staticText265, 0, wx.ALL, 5 )

		self.resist_c_security5 = wx.TextCtrl( self.resist_council_6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.resist_c_security5, 0, wx.ALL, 5 )

		self.m_staticText275 = wx.StaticText( self.resist_council_6, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText275.Wrap( -1 )

		fgSizer45.Add( self.m_staticText275, 0, wx.ALL, 5 )

		self.resist_c_loyalty5 = wx.TextCtrl( self.resist_council_6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.resist_c_loyalty5, 0, wx.ALL, 5 )


		self.resist_council_6.SetSizer( fgSizer45 )
		self.resist_council_6.Layout()
		fgSizer45.Fit( self.resist_council_6 )
		self.resist_sub_tabs.AddPage( self.resist_council_6, u"Councilor 6", False )

		bSizer3.Add( self.resist_sub_tabs, 0, wx.ALL|wx.EXPAND, 5 )


		self.resist_panel.SetSizer( bSizer3 )
		self.resist_panel.Layout()
		bSizer3.Fit( self.resist_panel )
		self.app_tabs.AddPage( self.resist_panel, u"The Resistance", False )
		self.imperium_panel = wx.Panel( self.app_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 0, 3, 0, 0 )

		self.player_flag1 = wx.CheckBox( self.imperium_panel, wx.ID_ANY, u"Player Faction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.player_flag1, 0, wx.ALL, 5 )

		self.m_staticText58111 = wx.StaticText( self.imperium_panel, wx.ID_ANY, u"Alien Hate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58111.Wrap( -1 )

		gSizer11.Add( self.m_staticText58111, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_spinCtrl21 = wx.SpinCtrl( self.imperium_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer11.Add( self.m_spinCtrl21, 0, wx.ALL, 5 )


		bSizer31.Add( gSizer11, 1, wx.EXPAND, 5 )

		self.resist_sub_tabs1 = wx.Notebook( self.imperium_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_resource_panel1 = wx.Panel( self.resist_sub_tabs1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText28 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Money", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer21.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.resist_money1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_money1, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Influence", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		fgSizer21.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.resist_influence1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_influence1, 0, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Ops", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		fgSizer21.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.resist_ops1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_ops1, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Boost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer21.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.resist_boost1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_boost1, 0, wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Water", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		fgSizer21.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.resist_water1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_water1, 0, wx.ALL, 5 )

		self.m_staticText71 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Volatiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		fgSizer21.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.resist_volatiles1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_volatiles1, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Base Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer21.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.resist_basemetals1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_basemetals1, 0, wx.ALL, 5 )

		self.m_staticText91 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Noble Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		fgSizer21.Add( self.m_staticText91, 0, wx.ALL, 5 )

		self.resist_noblemetals1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_noblemetals1, 0, wx.ALL, 5 )

		self.m_staticText101 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Fissiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		fgSizer21.Add( self.m_staticText101, 0, wx.ALL, 5 )

		self.resist_fissiles1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_fissiles1, 0, wx.ALL, 5 )

		self.m_staticText111 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Exotics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		fgSizer21.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.resist_exotics1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_exotics1, 0, wx.ALL, 5 )

		self.m_staticText121 = wx.StaticText( self.resist_resource_panel1, wx.ID_ANY, u"Antimatter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		fgSizer21.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.resist_antimatter1 = wx.TextCtrl( self.resist_resource_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.resist_antimatter1, 0, wx.ALL, 5 )


		self.resist_resource_panel1.SetSizer( fgSizer21 )
		self.resist_resource_panel1.Layout()
		fgSizer21.Fit( self.resist_resource_panel1 )
		self.resist_sub_tabs1.AddPage( self.resist_resource_panel1, u"Resources", True )
		self.resist_projects1 = wx.Panel( self.resist_sub_tabs1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer31 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText151 = wx.StaticText( self.resist_projects1, wx.ID_ANY, u"Active Project", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText151.Wrap( -1 )

		fgSizer31.Add( self.m_staticText151, 0, wx.ALL, 5 )

		self.m_staticText171 = wx.StaticText( self.resist_projects1, wx.ID_ANY, u"Current Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )

		fgSizer31.Add( self.m_staticText171, 0, wx.ALL, 5 )

		self.resist_project11 = wx.StaticText( self.resist_projects1, wx.ID_ANY, u"Project 1 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project11.Wrap( -1 )

		fgSizer31.Add( self.resist_project11, 0, wx.ALL, 5 )

		self.resist_project1_progress1 = wx.TextCtrl( self.resist_projects1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer31.Add( self.resist_project1_progress1, 0, wx.ALL, 5 )

		self.resist_project21 = wx.StaticText( self.resist_projects1, wx.ID_ANY, u"Project 2 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project21.Wrap( -1 )

		fgSizer31.Add( self.resist_project21, 0, wx.ALL, 5 )

		self.resist_project2_progress1 = wx.TextCtrl( self.resist_projects1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer31.Add( self.resist_project2_progress1, 0, wx.ALL, 5 )

		self.resist_project31 = wx.StaticText( self.resist_projects1, wx.ID_ANY, u"Project 3 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project31.Wrap( -1 )

		fgSizer31.Add( self.resist_project31, 0, wx.ALL, 5 )

		self.resist_project3_progress1 = wx.TextCtrl( self.resist_projects1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer31.Add( self.resist_project3_progress1, 0, wx.ALL, 5 )


		self.resist_projects1.SetSizer( fgSizer31 )
		self.resist_projects1.Layout()
		fgSizer31.Fit( self.resist_projects1 )
		self.resist_sub_tabs1.AddPage( self.resist_projects1, u"Project Research", False )
		self.resist_council_11 = wx.Panel( self.resist_sub_tabs1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer46 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer46.SetFlexibleDirection( wx.BOTH )
		fgSizer46.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname6 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname6.Wrap( -1 )

		fgSizer46.Add( self.resist_c_fname6, 0, wx.ALL, 5 )

		self.resist_c_lname6 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname6.Wrap( -1 )

		fgSizer46.Add( self.resist_c_lname6, 0, wx.ALL, 5 )

		self.m_staticText846 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText846.Wrap( -1 )

		fgSizer46.Add( self.m_staticText846, 0, wx.ALL, 5 )

		resist_c_class6Choices = []
		self.resist_c_class6 = wx.Choice( self.resist_council_11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class6Choices, 0 )
		self.resist_c_class6.SetSelection( 0 )
		fgSizer46.Add( self.resist_c_class6, 0, wx.ALL, 5 )

		self.m_staticText206 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText206.Wrap( -1 )

		fgSizer46.Add( self.m_staticText206, 0, wx.ALL, 5 )

		self.resist_c_persuasion6 = wx.TextCtrl( self.resist_council_11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.resist_c_persuasion6, 0, wx.ALL, 5 )

		self.m_staticText216 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText216.Wrap( -1 )

		fgSizer46.Add( self.m_staticText216, 0, wx.ALL, 5 )

		self.resist_c_investigation6 = wx.TextCtrl( self.resist_council_11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.resist_c_investigation6, 0, wx.ALL, 5 )

		self.m_staticText226 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText226.Wrap( -1 )

		fgSizer46.Add( self.m_staticText226, 0, wx.ALL, 5 )

		self.resist_c_espionage6 = wx.TextCtrl( self.resist_council_11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.resist_c_espionage6, 0, wx.ALL, 5 )

		self.m_staticText236 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText236.Wrap( -1 )

		fgSizer46.Add( self.m_staticText236, 0, wx.ALL, 5 )

		self.resist_c_command6 = wx.TextCtrl( self.resist_council_11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.resist_c_command6, 0, wx.ALL, 5 )

		self.m_staticText246 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText246.Wrap( -1 )

		fgSizer46.Add( self.m_staticText246, 0, wx.ALL, 5 )

		self.resist_c_administration6 = wx.TextCtrl( self.resist_council_11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.resist_c_administration6, 0, wx.ALL, 5 )

		self.m_staticText256 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText256.Wrap( -1 )

		fgSizer46.Add( self.m_staticText256, 0, wx.ALL, 5 )

		self.resist_c_science6 = wx.TextCtrl( self.resist_council_11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.resist_c_science6, 0, wx.ALL, 5 )

		self.m_staticText266 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText266.Wrap( -1 )

		fgSizer46.Add( self.m_staticText266, 0, wx.ALL, 5 )

		self.resist_c_security6 = wx.TextCtrl( self.resist_council_11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.resist_c_security6, 0, wx.ALL, 5 )

		self.m_staticText276 = wx.StaticText( self.resist_council_11, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText276.Wrap( -1 )

		fgSizer46.Add( self.m_staticText276, 0, wx.ALL, 5 )

		self.resist_c_loyalty6 = wx.TextCtrl( self.resist_council_11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.resist_c_loyalty6, 0, wx.ALL, 5 )


		self.resist_council_11.SetSizer( fgSizer46 )
		self.resist_council_11.Layout()
		fgSizer46.Fit( self.resist_council_11 )
		self.resist_sub_tabs1.AddPage( self.resist_council_11, u"Councilor 1", False )
		self.resist_council_21 = wx.Panel( self.resist_sub_tabs1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer411 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer411.SetFlexibleDirection( wx.BOTH )
		fgSizer411.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname11 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname11.Wrap( -1 )

		fgSizer411.Add( self.resist_c_fname11, 0, wx.ALL, 5 )

		self.resist_c_lname11 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname11.Wrap( -1 )

		fgSizer411.Add( self.resist_c_lname11, 0, wx.ALL, 5 )

		self.m_staticText8411 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8411.Wrap( -1 )

		fgSizer411.Add( self.m_staticText8411, 0, wx.ALL, 5 )

		resist_c_class11Choices = []
		self.resist_c_class11 = wx.Choice( self.resist_council_21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class11Choices, 0 )
		self.resist_c_class11.SetSelection( 0 )
		fgSizer411.Add( self.resist_c_class11, 0, wx.ALL, 5 )

		self.m_staticText2011 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2011.Wrap( -1 )

		fgSizer411.Add( self.m_staticText2011, 0, wx.ALL, 5 )

		self.resist_c_persuasion11 = wx.TextCtrl( self.resist_council_21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer411.Add( self.resist_c_persuasion11, 0, wx.ALL, 5 )

		self.m_staticText2111 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2111.Wrap( -1 )

		fgSizer411.Add( self.m_staticText2111, 0, wx.ALL, 5 )

		self.resist_c_investigation11 = wx.TextCtrl( self.resist_council_21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer411.Add( self.resist_c_investigation11, 0, wx.ALL, 5 )

		self.m_staticText2211 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2211.Wrap( -1 )

		fgSizer411.Add( self.m_staticText2211, 0, wx.ALL, 5 )

		self.resist_c_espionage11 = wx.TextCtrl( self.resist_council_21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer411.Add( self.resist_c_espionage11, 0, wx.ALL, 5 )

		self.m_staticText2311 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2311.Wrap( -1 )

		fgSizer411.Add( self.m_staticText2311, 0, wx.ALL, 5 )

		self.resist_c_command11 = wx.TextCtrl( self.resist_council_21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer411.Add( self.resist_c_command11, 0, wx.ALL, 5 )

		self.m_staticText2411 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2411.Wrap( -1 )

		fgSizer411.Add( self.m_staticText2411, 0, wx.ALL, 5 )

		self.resist_c_administration11 = wx.TextCtrl( self.resist_council_21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer411.Add( self.resist_c_administration11, 0, wx.ALL, 5 )

		self.m_staticText2511 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2511.Wrap( -1 )

		fgSizer411.Add( self.m_staticText2511, 0, wx.ALL, 5 )

		self.resist_c_science11 = wx.TextCtrl( self.resist_council_21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer411.Add( self.resist_c_science11, 0, wx.ALL, 5 )

		self.m_staticText2611 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2611.Wrap( -1 )

		fgSizer411.Add( self.m_staticText2611, 0, wx.ALL, 5 )

		self.resist_c_security11 = wx.TextCtrl( self.resist_council_21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer411.Add( self.resist_c_security11, 0, wx.ALL, 5 )

		self.m_staticText2711 = wx.StaticText( self.resist_council_21, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2711.Wrap( -1 )

		fgSizer411.Add( self.m_staticText2711, 0, wx.ALL, 5 )

		self.resist_c_loyalty11 = wx.TextCtrl( self.resist_council_21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer411.Add( self.resist_c_loyalty11, 0, wx.ALL, 5 )


		self.resist_council_21.SetSizer( fgSizer411 )
		self.resist_council_21.Layout()
		fgSizer411.Fit( self.resist_council_21 )
		self.resist_sub_tabs1.AddPage( self.resist_council_21, u"Councilor 2", False )
		self.resist_council_31 = wx.Panel( self.resist_sub_tabs1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer421 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer421.SetFlexibleDirection( wx.BOTH )
		fgSizer421.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname21 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname21.Wrap( -1 )

		fgSizer421.Add( self.resist_c_fname21, 0, wx.ALL, 5 )

		self.resist_c_lname21 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname21.Wrap( -1 )

		fgSizer421.Add( self.resist_c_lname21, 0, wx.ALL, 5 )

		self.m_staticText8421 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8421.Wrap( -1 )

		fgSizer421.Add( self.m_staticText8421, 0, wx.ALL, 5 )

		resist_c_class21Choices = []
		self.resist_c_class21 = wx.Choice( self.resist_council_31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class21Choices, 0 )
		self.resist_c_class21.SetSelection( 0 )
		fgSizer421.Add( self.resist_c_class21, 0, wx.ALL, 5 )

		self.m_staticText2021 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2021.Wrap( -1 )

		fgSizer421.Add( self.m_staticText2021, 0, wx.ALL, 5 )

		self.resist_c_persuasion21 = wx.TextCtrl( self.resist_council_31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.resist_c_persuasion21, 0, wx.ALL, 5 )

		self.m_staticText2121 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2121.Wrap( -1 )

		fgSizer421.Add( self.m_staticText2121, 0, wx.ALL, 5 )

		self.resist_c_investigation21 = wx.TextCtrl( self.resist_council_31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.resist_c_investigation21, 0, wx.ALL, 5 )

		self.m_staticText2221 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2221.Wrap( -1 )

		fgSizer421.Add( self.m_staticText2221, 0, wx.ALL, 5 )

		self.resist_c_espionage21 = wx.TextCtrl( self.resist_council_31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.resist_c_espionage21, 0, wx.ALL, 5 )

		self.m_staticText2321 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2321.Wrap( -1 )

		fgSizer421.Add( self.m_staticText2321, 0, wx.ALL, 5 )

		self.resist_c_command21 = wx.TextCtrl( self.resist_council_31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.resist_c_command21, 0, wx.ALL, 5 )

		self.m_staticText2421 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2421.Wrap( -1 )

		fgSizer421.Add( self.m_staticText2421, 0, wx.ALL, 5 )

		self.resist_c_administration21 = wx.TextCtrl( self.resist_council_31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.resist_c_administration21, 0, wx.ALL, 5 )

		self.m_staticText2521 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2521.Wrap( -1 )

		fgSizer421.Add( self.m_staticText2521, 0, wx.ALL, 5 )

		self.resist_c_science21 = wx.TextCtrl( self.resist_council_31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.resist_c_science21, 0, wx.ALL, 5 )

		self.m_staticText2621 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2621.Wrap( -1 )

		fgSizer421.Add( self.m_staticText2621, 0, wx.ALL, 5 )

		self.resist_c_security21 = wx.TextCtrl( self.resist_council_31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.resist_c_security21, 0, wx.ALL, 5 )

		self.m_staticText2721 = wx.StaticText( self.resist_council_31, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2721.Wrap( -1 )

		fgSizer421.Add( self.m_staticText2721, 0, wx.ALL, 5 )

		self.resist_c_loyalty21 = wx.TextCtrl( self.resist_council_31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.resist_c_loyalty21, 0, wx.ALL, 5 )


		self.resist_council_31.SetSizer( fgSizer421 )
		self.resist_council_31.Layout()
		fgSizer421.Fit( self.resist_council_31 )
		self.resist_sub_tabs1.AddPage( self.resist_council_31, u"Councilor 3", False )
		self.resist_council_41 = wx.Panel( self.resist_sub_tabs1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer431 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer431.SetFlexibleDirection( wx.BOTH )
		fgSizer431.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname31 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname31.Wrap( -1 )

		fgSizer431.Add( self.resist_c_fname31, 0, wx.ALL, 5 )

		self.resist_c_lname31 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname31.Wrap( -1 )

		fgSizer431.Add( self.resist_c_lname31, 0, wx.ALL, 5 )

		self.m_staticText8431 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8431.Wrap( -1 )

		fgSizer431.Add( self.m_staticText8431, 0, wx.ALL, 5 )

		resist_c_class31Choices = []
		self.resist_c_class31 = wx.Choice( self.resist_council_41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class31Choices, 0 )
		self.resist_c_class31.SetSelection( 0 )
		fgSizer431.Add( self.resist_c_class31, 0, wx.ALL, 5 )

		self.m_staticText2031 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2031.Wrap( -1 )

		fgSizer431.Add( self.m_staticText2031, 0, wx.ALL, 5 )

		self.resist_c_persuasion31 = wx.TextCtrl( self.resist_council_41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer431.Add( self.resist_c_persuasion31, 0, wx.ALL, 5 )

		self.m_staticText2131 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2131.Wrap( -1 )

		fgSizer431.Add( self.m_staticText2131, 0, wx.ALL, 5 )

		self.resist_c_investigation31 = wx.TextCtrl( self.resist_council_41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer431.Add( self.resist_c_investigation31, 0, wx.ALL, 5 )

		self.m_staticText2231 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2231.Wrap( -1 )

		fgSizer431.Add( self.m_staticText2231, 0, wx.ALL, 5 )

		self.resist_c_espionage31 = wx.TextCtrl( self.resist_council_41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer431.Add( self.resist_c_espionage31, 0, wx.ALL, 5 )

		self.m_staticText2331 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2331.Wrap( -1 )

		fgSizer431.Add( self.m_staticText2331, 0, wx.ALL, 5 )

		self.resist_c_command31 = wx.TextCtrl( self.resist_council_41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer431.Add( self.resist_c_command31, 0, wx.ALL, 5 )

		self.m_staticText2431 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2431.Wrap( -1 )

		fgSizer431.Add( self.m_staticText2431, 0, wx.ALL, 5 )

		self.resist_c_administration31 = wx.TextCtrl( self.resist_council_41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer431.Add( self.resist_c_administration31, 0, wx.ALL, 5 )

		self.m_staticText2531 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2531.Wrap( -1 )

		fgSizer431.Add( self.m_staticText2531, 0, wx.ALL, 5 )

		self.resist_c_science31 = wx.TextCtrl( self.resist_council_41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer431.Add( self.resist_c_science31, 0, wx.ALL, 5 )

		self.m_staticText2631 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2631.Wrap( -1 )

		fgSizer431.Add( self.m_staticText2631, 0, wx.ALL, 5 )

		self.resist_c_security31 = wx.TextCtrl( self.resist_council_41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer431.Add( self.resist_c_security31, 0, wx.ALL, 5 )

		self.m_staticText2731 = wx.StaticText( self.resist_council_41, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2731.Wrap( -1 )

		fgSizer431.Add( self.m_staticText2731, 0, wx.ALL, 5 )

		self.resist_c_loyalty31 = wx.TextCtrl( self.resist_council_41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer431.Add( self.resist_c_loyalty31, 0, wx.ALL, 5 )


		self.resist_council_41.SetSizer( fgSizer431 )
		self.resist_council_41.Layout()
		fgSizer431.Fit( self.resist_council_41 )
		self.resist_sub_tabs1.AddPage( self.resist_council_41, u"Councilor 4", False )
		self.resist_council_51 = wx.Panel( self.resist_sub_tabs1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer441 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer441.SetFlexibleDirection( wx.BOTH )
		fgSizer441.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname41 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname41.Wrap( -1 )

		fgSizer441.Add( self.resist_c_fname41, 0, wx.ALL, 5 )

		self.resist_c_lname41 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname41.Wrap( -1 )

		fgSizer441.Add( self.resist_c_lname41, 0, wx.ALL, 5 )

		self.m_staticText8441 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8441.Wrap( -1 )

		fgSizer441.Add( self.m_staticText8441, 0, wx.ALL, 5 )

		resist_c_class41Choices = []
		self.resist_c_class41 = wx.Choice( self.resist_council_51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class41Choices, 0 )
		self.resist_c_class41.SetSelection( 0 )
		fgSizer441.Add( self.resist_c_class41, 0, wx.ALL, 5 )

		self.m_staticText2041 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2041.Wrap( -1 )

		fgSizer441.Add( self.m_staticText2041, 0, wx.ALL, 5 )

		self.resist_c_persuasion41 = wx.TextCtrl( self.resist_council_51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer441.Add( self.resist_c_persuasion41, 0, wx.ALL, 5 )

		self.m_staticText2141 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2141.Wrap( -1 )

		fgSizer441.Add( self.m_staticText2141, 0, wx.ALL, 5 )

		self.resist_c_investigation41 = wx.TextCtrl( self.resist_council_51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer441.Add( self.resist_c_investigation41, 0, wx.ALL, 5 )

		self.m_staticText2241 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2241.Wrap( -1 )

		fgSizer441.Add( self.m_staticText2241, 0, wx.ALL, 5 )

		self.resist_c_espionage41 = wx.TextCtrl( self.resist_council_51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer441.Add( self.resist_c_espionage41, 0, wx.ALL, 5 )

		self.m_staticText2341 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2341.Wrap( -1 )

		fgSizer441.Add( self.m_staticText2341, 0, wx.ALL, 5 )

		self.resist_c_command41 = wx.TextCtrl( self.resist_council_51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer441.Add( self.resist_c_command41, 0, wx.ALL, 5 )

		self.m_staticText2441 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2441.Wrap( -1 )

		fgSizer441.Add( self.m_staticText2441, 0, wx.ALL, 5 )

		self.resist_c_administration41 = wx.TextCtrl( self.resist_council_51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer441.Add( self.resist_c_administration41, 0, wx.ALL, 5 )

		self.m_staticText2541 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2541.Wrap( -1 )

		fgSizer441.Add( self.m_staticText2541, 0, wx.ALL, 5 )

		self.resist_c_science41 = wx.TextCtrl( self.resist_council_51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer441.Add( self.resist_c_science41, 0, wx.ALL, 5 )

		self.m_staticText2641 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2641.Wrap( -1 )

		fgSizer441.Add( self.m_staticText2641, 0, wx.ALL, 5 )

		self.resist_c_security41 = wx.TextCtrl( self.resist_council_51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer441.Add( self.resist_c_security41, 0, wx.ALL, 5 )

		self.m_staticText2741 = wx.StaticText( self.resist_council_51, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2741.Wrap( -1 )

		fgSizer441.Add( self.m_staticText2741, 0, wx.ALL, 5 )

		self.resist_c_loyalty41 = wx.TextCtrl( self.resist_council_51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer441.Add( self.resist_c_loyalty41, 0, wx.ALL, 5 )


		self.resist_council_51.SetSizer( fgSizer441 )
		self.resist_council_51.Layout()
		fgSizer441.Fit( self.resist_council_51 )
		self.resist_sub_tabs1.AddPage( self.resist_council_51, u"Councilor 5", False )
		self.resist_council_61 = wx.Panel( self.resist_sub_tabs1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer451 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer451.SetFlexibleDirection( wx.BOTH )
		fgSizer451.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname51 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname51.Wrap( -1 )

		fgSizer451.Add( self.resist_c_fname51, 0, wx.ALL, 5 )

		self.resist_c_lname51 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname51.Wrap( -1 )

		fgSizer451.Add( self.resist_c_lname51, 0, wx.ALL, 5 )

		self.m_staticText8451 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8451.Wrap( -1 )

		fgSizer451.Add( self.m_staticText8451, 0, wx.ALL, 5 )

		resist_c_class51Choices = []
		self.resist_c_class51 = wx.Choice( self.resist_council_61, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class51Choices, 0 )
		self.resist_c_class51.SetSelection( 0 )
		fgSizer451.Add( self.resist_c_class51, 0, wx.ALL, 5 )

		self.m_staticText2051 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2051.Wrap( -1 )

		fgSizer451.Add( self.m_staticText2051, 0, wx.ALL, 5 )

		self.resist_c_persuasion51 = wx.TextCtrl( self.resist_council_61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer451.Add( self.resist_c_persuasion51, 0, wx.ALL, 5 )

		self.m_staticText2151 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2151.Wrap( -1 )

		fgSizer451.Add( self.m_staticText2151, 0, wx.ALL, 5 )

		self.resist_c_investigation51 = wx.TextCtrl( self.resist_council_61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer451.Add( self.resist_c_investigation51, 0, wx.ALL, 5 )

		self.m_staticText2251 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2251.Wrap( -1 )

		fgSizer451.Add( self.m_staticText2251, 0, wx.ALL, 5 )

		self.resist_c_espionage51 = wx.TextCtrl( self.resist_council_61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer451.Add( self.resist_c_espionage51, 0, wx.ALL, 5 )

		self.m_staticText2351 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2351.Wrap( -1 )

		fgSizer451.Add( self.m_staticText2351, 0, wx.ALL, 5 )

		self.resist_c_command51 = wx.TextCtrl( self.resist_council_61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer451.Add( self.resist_c_command51, 0, wx.ALL, 5 )

		self.m_staticText2451 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2451.Wrap( -1 )

		fgSizer451.Add( self.m_staticText2451, 0, wx.ALL, 5 )

		self.resist_c_administration51 = wx.TextCtrl( self.resist_council_61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer451.Add( self.resist_c_administration51, 0, wx.ALL, 5 )

		self.m_staticText2551 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2551.Wrap( -1 )

		fgSizer451.Add( self.m_staticText2551, 0, wx.ALL, 5 )

		self.resist_c_science51 = wx.TextCtrl( self.resist_council_61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer451.Add( self.resist_c_science51, 0, wx.ALL, 5 )

		self.m_staticText2651 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2651.Wrap( -1 )

		fgSizer451.Add( self.m_staticText2651, 0, wx.ALL, 5 )

		self.resist_c_security51 = wx.TextCtrl( self.resist_council_61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer451.Add( self.resist_c_security51, 0, wx.ALL, 5 )

		self.m_staticText2751 = wx.StaticText( self.resist_council_61, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2751.Wrap( -1 )

		fgSizer451.Add( self.m_staticText2751, 0, wx.ALL, 5 )

		self.resist_c_loyalty51 = wx.TextCtrl( self.resist_council_61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer451.Add( self.resist_c_loyalty51, 0, wx.ALL, 5 )


		self.resist_council_61.SetSizer( fgSizer451 )
		self.resist_council_61.Layout()
		fgSizer451.Fit( self.resist_council_61 )
		self.resist_sub_tabs1.AddPage( self.resist_council_61, u"Councilor 6", False )

		bSizer31.Add( self.resist_sub_tabs1, 0, wx.EXPAND |wx.ALL, 5 )


		self.imperium_panel.SetSizer( bSizer31 )
		self.imperium_panel.Layout()
		bSizer31.Fit( self.imperium_panel )
		self.app_tabs.AddPage( self.imperium_panel, u"Humanity First", False )
		self.initiave_panel = wx.Panel( self.app_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		gSizer12 = wx.GridSizer( 0, 3, 0, 0 )

		self.player_flag2 = wx.CheckBox( self.initiave_panel, wx.ID_ANY, u"Player Faction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.player_flag2, 0, wx.ALL, 5 )

		self.m_staticText58112 = wx.StaticText( self.initiave_panel, wx.ID_ANY, u"Alien Hate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58112.Wrap( -1 )

		gSizer12.Add( self.m_staticText58112, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_spinCtrl22 = wx.SpinCtrl( self.initiave_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer12.Add( self.m_spinCtrl22, 0, wx.ALL, 5 )


		bSizer32.Add( gSizer12, 1, wx.EXPAND, 5 )

		self.resist_sub_tabs2 = wx.Notebook( self.initiave_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_resource_panel2 = wx.Panel( self.resist_sub_tabs2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer22 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText29 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Money", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer22.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.resist_money2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_money2, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Influence", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.resist_influence2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_influence2, 0, wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Ops", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		fgSizer22.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.resist_ops2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_ops2, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Boost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer22.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.resist_boost2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_boost2, 0, wx.ALL, 5 )

		self.m_staticText62 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Water", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		fgSizer22.Add( self.m_staticText62, 0, wx.ALL, 5 )

		self.resist_water2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_water2, 0, wx.ALL, 5 )

		self.m_staticText72 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Volatiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )

		fgSizer22.Add( self.m_staticText72, 0, wx.ALL, 5 )

		self.resist_volatiles2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_volatiles2, 0, wx.ALL, 5 )

		self.m_staticText82 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Base Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		fgSizer22.Add( self.m_staticText82, 0, wx.ALL, 5 )

		self.resist_basemetals2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_basemetals2, 0, wx.ALL, 5 )

		self.m_staticText92 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Noble Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )

		fgSizer22.Add( self.m_staticText92, 0, wx.ALL, 5 )

		self.resist_noblemetals2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_noblemetals2, 0, wx.ALL, 5 )

		self.m_staticText102 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Fissiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText102.Wrap( -1 )

		fgSizer22.Add( self.m_staticText102, 0, wx.ALL, 5 )

		self.resist_fissiles2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_fissiles2, 0, wx.ALL, 5 )

		self.m_staticText112 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Exotics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText112.Wrap( -1 )

		fgSizer22.Add( self.m_staticText112, 0, wx.ALL, 5 )

		self.resist_exotics2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_exotics2, 0, wx.ALL, 5 )

		self.m_staticText122 = wx.StaticText( self.resist_resource_panel2, wx.ID_ANY, u"Antimatter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText122.Wrap( -1 )

		fgSizer22.Add( self.m_staticText122, 0, wx.ALL, 5 )

		self.resist_antimatter2 = wx.TextCtrl( self.resist_resource_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.resist_antimatter2, 0, wx.ALL, 5 )


		self.resist_resource_panel2.SetSizer( fgSizer22 )
		self.resist_resource_panel2.Layout()
		fgSizer22.Fit( self.resist_resource_panel2 )
		self.resist_sub_tabs2.AddPage( self.resist_resource_panel2, u"Resources", True )
		self.resist_projects2 = wx.Panel( self.resist_sub_tabs2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer32 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer32.SetFlexibleDirection( wx.BOTH )
		fgSizer32.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText152 = wx.StaticText( self.resist_projects2, wx.ID_ANY, u"Active Project", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText152.Wrap( -1 )

		fgSizer32.Add( self.m_staticText152, 0, wx.ALL, 5 )

		self.m_staticText172 = wx.StaticText( self.resist_projects2, wx.ID_ANY, u"Current Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172.Wrap( -1 )

		fgSizer32.Add( self.m_staticText172, 0, wx.ALL, 5 )

		self.resist_project12 = wx.StaticText( self.resist_projects2, wx.ID_ANY, u"Project 1 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project12.Wrap( -1 )

		fgSizer32.Add( self.resist_project12, 0, wx.ALL, 5 )

		self.resist_project1_progress2 = wx.TextCtrl( self.resist_projects2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer32.Add( self.resist_project1_progress2, 0, wx.ALL, 5 )

		self.resist_project22 = wx.StaticText( self.resist_projects2, wx.ID_ANY, u"Project 2 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project22.Wrap( -1 )

		fgSizer32.Add( self.resist_project22, 0, wx.ALL, 5 )

		self.resist_project2_progress2 = wx.TextCtrl( self.resist_projects2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer32.Add( self.resist_project2_progress2, 0, wx.ALL, 5 )

		self.resist_project32 = wx.StaticText( self.resist_projects2, wx.ID_ANY, u"Project 3 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project32.Wrap( -1 )

		fgSizer32.Add( self.resist_project32, 0, wx.ALL, 5 )

		self.resist_project3_progress2 = wx.TextCtrl( self.resist_projects2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer32.Add( self.resist_project3_progress2, 0, wx.ALL, 5 )


		self.resist_projects2.SetSizer( fgSizer32 )
		self.resist_projects2.Layout()
		fgSizer32.Fit( self.resist_projects2 )
		self.resist_sub_tabs2.AddPage( self.resist_projects2, u"Project Research", False )
		self.resist_council_12 = wx.Panel( self.resist_sub_tabs2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer47 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer47.SetFlexibleDirection( wx.BOTH )
		fgSizer47.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname7 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname7.Wrap( -1 )

		fgSizer47.Add( self.resist_c_fname7, 0, wx.ALL, 5 )

		self.resist_c_lname7 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname7.Wrap( -1 )

		fgSizer47.Add( self.resist_c_lname7, 0, wx.ALL, 5 )

		self.m_staticText847 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText847.Wrap( -1 )

		fgSizer47.Add( self.m_staticText847, 0, wx.ALL, 5 )

		resist_c_class7Choices = []
		self.resist_c_class7 = wx.Choice( self.resist_council_12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class7Choices, 0 )
		self.resist_c_class7.SetSelection( 0 )
		fgSizer47.Add( self.resist_c_class7, 0, wx.ALL, 5 )

		self.m_staticText207 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText207.Wrap( -1 )

		fgSizer47.Add( self.m_staticText207, 0, wx.ALL, 5 )

		self.resist_c_persuasion7 = wx.TextCtrl( self.resist_council_12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.resist_c_persuasion7, 0, wx.ALL, 5 )

		self.m_staticText217 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText217.Wrap( -1 )

		fgSizer47.Add( self.m_staticText217, 0, wx.ALL, 5 )

		self.resist_c_investigation7 = wx.TextCtrl( self.resist_council_12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.resist_c_investigation7, 0, wx.ALL, 5 )

		self.m_staticText227 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText227.Wrap( -1 )

		fgSizer47.Add( self.m_staticText227, 0, wx.ALL, 5 )

		self.resist_c_espionage7 = wx.TextCtrl( self.resist_council_12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.resist_c_espionage7, 0, wx.ALL, 5 )

		self.m_staticText237 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText237.Wrap( -1 )

		fgSizer47.Add( self.m_staticText237, 0, wx.ALL, 5 )

		self.resist_c_command7 = wx.TextCtrl( self.resist_council_12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.resist_c_command7, 0, wx.ALL, 5 )

		self.m_staticText247 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText247.Wrap( -1 )

		fgSizer47.Add( self.m_staticText247, 0, wx.ALL, 5 )

		self.resist_c_administration7 = wx.TextCtrl( self.resist_council_12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.resist_c_administration7, 0, wx.ALL, 5 )

		self.m_staticText257 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText257.Wrap( -1 )

		fgSizer47.Add( self.m_staticText257, 0, wx.ALL, 5 )

		self.resist_c_science7 = wx.TextCtrl( self.resist_council_12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.resist_c_science7, 0, wx.ALL, 5 )

		self.m_staticText267 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText267.Wrap( -1 )

		fgSizer47.Add( self.m_staticText267, 0, wx.ALL, 5 )

		self.resist_c_security7 = wx.TextCtrl( self.resist_council_12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.resist_c_security7, 0, wx.ALL, 5 )

		self.m_staticText277 = wx.StaticText( self.resist_council_12, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText277.Wrap( -1 )

		fgSizer47.Add( self.m_staticText277, 0, wx.ALL, 5 )

		self.resist_c_loyalty7 = wx.TextCtrl( self.resist_council_12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.resist_c_loyalty7, 0, wx.ALL, 5 )


		self.resist_council_12.SetSizer( fgSizer47 )
		self.resist_council_12.Layout()
		fgSizer47.Fit( self.resist_council_12 )
		self.resist_sub_tabs2.AddPage( self.resist_council_12, u"Councilor 1", False )
		self.resist_council_22 = wx.Panel( self.resist_sub_tabs2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer412 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer412.SetFlexibleDirection( wx.BOTH )
		fgSizer412.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname12 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname12.Wrap( -1 )

		fgSizer412.Add( self.resist_c_fname12, 0, wx.ALL, 5 )

		self.resist_c_lname12 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname12.Wrap( -1 )

		fgSizer412.Add( self.resist_c_lname12, 0, wx.ALL, 5 )

		self.m_staticText8412 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8412.Wrap( -1 )

		fgSizer412.Add( self.m_staticText8412, 0, wx.ALL, 5 )

		resist_c_class12Choices = []
		self.resist_c_class12 = wx.Choice( self.resist_council_22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class12Choices, 0 )
		self.resist_c_class12.SetSelection( 0 )
		fgSizer412.Add( self.resist_c_class12, 0, wx.ALL, 5 )

		self.m_staticText2012 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2012.Wrap( -1 )

		fgSizer412.Add( self.m_staticText2012, 0, wx.ALL, 5 )

		self.resist_c_persuasion12 = wx.TextCtrl( self.resist_council_22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer412.Add( self.resist_c_persuasion12, 0, wx.ALL, 5 )

		self.m_staticText2112 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2112.Wrap( -1 )

		fgSizer412.Add( self.m_staticText2112, 0, wx.ALL, 5 )

		self.resist_c_investigation12 = wx.TextCtrl( self.resist_council_22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer412.Add( self.resist_c_investigation12, 0, wx.ALL, 5 )

		self.m_staticText2212 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2212.Wrap( -1 )

		fgSizer412.Add( self.m_staticText2212, 0, wx.ALL, 5 )

		self.resist_c_espionage12 = wx.TextCtrl( self.resist_council_22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer412.Add( self.resist_c_espionage12, 0, wx.ALL, 5 )

		self.m_staticText2312 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2312.Wrap( -1 )

		fgSizer412.Add( self.m_staticText2312, 0, wx.ALL, 5 )

		self.resist_c_command12 = wx.TextCtrl( self.resist_council_22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer412.Add( self.resist_c_command12, 0, wx.ALL, 5 )

		self.m_staticText2412 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2412.Wrap( -1 )

		fgSizer412.Add( self.m_staticText2412, 0, wx.ALL, 5 )

		self.resist_c_administration12 = wx.TextCtrl( self.resist_council_22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer412.Add( self.resist_c_administration12, 0, wx.ALL, 5 )

		self.m_staticText2512 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2512.Wrap( -1 )

		fgSizer412.Add( self.m_staticText2512, 0, wx.ALL, 5 )

		self.resist_c_science12 = wx.TextCtrl( self.resist_council_22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer412.Add( self.resist_c_science12, 0, wx.ALL, 5 )

		self.m_staticText2612 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2612.Wrap( -1 )

		fgSizer412.Add( self.m_staticText2612, 0, wx.ALL, 5 )

		self.resist_c_security12 = wx.TextCtrl( self.resist_council_22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer412.Add( self.resist_c_security12, 0, wx.ALL, 5 )

		self.m_staticText2712 = wx.StaticText( self.resist_council_22, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2712.Wrap( -1 )

		fgSizer412.Add( self.m_staticText2712, 0, wx.ALL, 5 )

		self.resist_c_loyalty12 = wx.TextCtrl( self.resist_council_22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer412.Add( self.resist_c_loyalty12, 0, wx.ALL, 5 )


		self.resist_council_22.SetSizer( fgSizer412 )
		self.resist_council_22.Layout()
		fgSizer412.Fit( self.resist_council_22 )
		self.resist_sub_tabs2.AddPage( self.resist_council_22, u"Councilor 2", False )
		self.resist_council_32 = wx.Panel( self.resist_sub_tabs2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer422 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer422.SetFlexibleDirection( wx.BOTH )
		fgSizer422.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname22 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname22.Wrap( -1 )

		fgSizer422.Add( self.resist_c_fname22, 0, wx.ALL, 5 )

		self.resist_c_lname22 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname22.Wrap( -1 )

		fgSizer422.Add( self.resist_c_lname22, 0, wx.ALL, 5 )

		self.m_staticText8422 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8422.Wrap( -1 )

		fgSizer422.Add( self.m_staticText8422, 0, wx.ALL, 5 )

		resist_c_class22Choices = []
		self.resist_c_class22 = wx.Choice( self.resist_council_32, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class22Choices, 0 )
		self.resist_c_class22.SetSelection( 0 )
		fgSizer422.Add( self.resist_c_class22, 0, wx.ALL, 5 )

		self.m_staticText2022 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2022.Wrap( -1 )

		fgSizer422.Add( self.m_staticText2022, 0, wx.ALL, 5 )

		self.resist_c_persuasion22 = wx.TextCtrl( self.resist_council_32, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer422.Add( self.resist_c_persuasion22, 0, wx.ALL, 5 )

		self.m_staticText2122 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2122.Wrap( -1 )

		fgSizer422.Add( self.m_staticText2122, 0, wx.ALL, 5 )

		self.resist_c_investigation22 = wx.TextCtrl( self.resist_council_32, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer422.Add( self.resist_c_investigation22, 0, wx.ALL, 5 )

		self.m_staticText2222 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2222.Wrap( -1 )

		fgSizer422.Add( self.m_staticText2222, 0, wx.ALL, 5 )

		self.resist_c_espionage22 = wx.TextCtrl( self.resist_council_32, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer422.Add( self.resist_c_espionage22, 0, wx.ALL, 5 )

		self.m_staticText2322 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2322.Wrap( -1 )

		fgSizer422.Add( self.m_staticText2322, 0, wx.ALL, 5 )

		self.resist_c_command22 = wx.TextCtrl( self.resist_council_32, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer422.Add( self.resist_c_command22, 0, wx.ALL, 5 )

		self.m_staticText2422 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2422.Wrap( -1 )

		fgSizer422.Add( self.m_staticText2422, 0, wx.ALL, 5 )

		self.resist_c_administration22 = wx.TextCtrl( self.resist_council_32, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer422.Add( self.resist_c_administration22, 0, wx.ALL, 5 )

		self.m_staticText2522 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2522.Wrap( -1 )

		fgSizer422.Add( self.m_staticText2522, 0, wx.ALL, 5 )

		self.resist_c_science22 = wx.TextCtrl( self.resist_council_32, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer422.Add( self.resist_c_science22, 0, wx.ALL, 5 )

		self.m_staticText2622 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2622.Wrap( -1 )

		fgSizer422.Add( self.m_staticText2622, 0, wx.ALL, 5 )

		self.resist_c_security22 = wx.TextCtrl( self.resist_council_32, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer422.Add( self.resist_c_security22, 0, wx.ALL, 5 )

		self.m_staticText2722 = wx.StaticText( self.resist_council_32, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2722.Wrap( -1 )

		fgSizer422.Add( self.m_staticText2722, 0, wx.ALL, 5 )

		self.resist_c_loyalty22 = wx.TextCtrl( self.resist_council_32, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer422.Add( self.resist_c_loyalty22, 0, wx.ALL, 5 )


		self.resist_council_32.SetSizer( fgSizer422 )
		self.resist_council_32.Layout()
		fgSizer422.Fit( self.resist_council_32 )
		self.resist_sub_tabs2.AddPage( self.resist_council_32, u"Councilor 3", False )
		self.resist_council_42 = wx.Panel( self.resist_sub_tabs2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer432 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer432.SetFlexibleDirection( wx.BOTH )
		fgSizer432.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname32 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname32.Wrap( -1 )

		fgSizer432.Add( self.resist_c_fname32, 0, wx.ALL, 5 )

		self.resist_c_lname32 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname32.Wrap( -1 )

		fgSizer432.Add( self.resist_c_lname32, 0, wx.ALL, 5 )

		self.m_staticText8432 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8432.Wrap( -1 )

		fgSizer432.Add( self.m_staticText8432, 0, wx.ALL, 5 )

		resist_c_class32Choices = []
		self.resist_c_class32 = wx.Choice( self.resist_council_42, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class32Choices, 0 )
		self.resist_c_class32.SetSelection( 0 )
		fgSizer432.Add( self.resist_c_class32, 0, wx.ALL, 5 )

		self.m_staticText2032 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2032.Wrap( -1 )

		fgSizer432.Add( self.m_staticText2032, 0, wx.ALL, 5 )

		self.resist_c_persuasion32 = wx.TextCtrl( self.resist_council_42, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer432.Add( self.resist_c_persuasion32, 0, wx.ALL, 5 )

		self.m_staticText2132 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2132.Wrap( -1 )

		fgSizer432.Add( self.m_staticText2132, 0, wx.ALL, 5 )

		self.resist_c_investigation32 = wx.TextCtrl( self.resist_council_42, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer432.Add( self.resist_c_investigation32, 0, wx.ALL, 5 )

		self.m_staticText2232 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2232.Wrap( -1 )

		fgSizer432.Add( self.m_staticText2232, 0, wx.ALL, 5 )

		self.resist_c_espionage32 = wx.TextCtrl( self.resist_council_42, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer432.Add( self.resist_c_espionage32, 0, wx.ALL, 5 )

		self.m_staticText2332 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2332.Wrap( -1 )

		fgSizer432.Add( self.m_staticText2332, 0, wx.ALL, 5 )

		self.resist_c_command32 = wx.TextCtrl( self.resist_council_42, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer432.Add( self.resist_c_command32, 0, wx.ALL, 5 )

		self.m_staticText2432 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2432.Wrap( -1 )

		fgSizer432.Add( self.m_staticText2432, 0, wx.ALL, 5 )

		self.resist_c_administration32 = wx.TextCtrl( self.resist_council_42, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer432.Add( self.resist_c_administration32, 0, wx.ALL, 5 )

		self.m_staticText2532 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2532.Wrap( -1 )

		fgSizer432.Add( self.m_staticText2532, 0, wx.ALL, 5 )

		self.resist_c_science32 = wx.TextCtrl( self.resist_council_42, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer432.Add( self.resist_c_science32, 0, wx.ALL, 5 )

		self.m_staticText2632 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2632.Wrap( -1 )

		fgSizer432.Add( self.m_staticText2632, 0, wx.ALL, 5 )

		self.resist_c_security32 = wx.TextCtrl( self.resist_council_42, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer432.Add( self.resist_c_security32, 0, wx.ALL, 5 )

		self.m_staticText2732 = wx.StaticText( self.resist_council_42, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2732.Wrap( -1 )

		fgSizer432.Add( self.m_staticText2732, 0, wx.ALL, 5 )

		self.resist_c_loyalty32 = wx.TextCtrl( self.resist_council_42, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer432.Add( self.resist_c_loyalty32, 0, wx.ALL, 5 )


		self.resist_council_42.SetSizer( fgSizer432 )
		self.resist_council_42.Layout()
		fgSizer432.Fit( self.resist_council_42 )
		self.resist_sub_tabs2.AddPage( self.resist_council_42, u"Councilor 4", False )
		self.resist_council_52 = wx.Panel( self.resist_sub_tabs2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer442 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer442.SetFlexibleDirection( wx.BOTH )
		fgSizer442.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname42 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname42.Wrap( -1 )

		fgSizer442.Add( self.resist_c_fname42, 0, wx.ALL, 5 )

		self.resist_c_lname42 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname42.Wrap( -1 )

		fgSizer442.Add( self.resist_c_lname42, 0, wx.ALL, 5 )

		self.m_staticText8442 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8442.Wrap( -1 )

		fgSizer442.Add( self.m_staticText8442, 0, wx.ALL, 5 )

		resist_c_class42Choices = []
		self.resist_c_class42 = wx.Choice( self.resist_council_52, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class42Choices, 0 )
		self.resist_c_class42.SetSelection( 0 )
		fgSizer442.Add( self.resist_c_class42, 0, wx.ALL, 5 )

		self.m_staticText2042 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2042.Wrap( -1 )

		fgSizer442.Add( self.m_staticText2042, 0, wx.ALL, 5 )

		self.resist_c_persuasion42 = wx.TextCtrl( self.resist_council_52, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer442.Add( self.resist_c_persuasion42, 0, wx.ALL, 5 )

		self.m_staticText2142 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2142.Wrap( -1 )

		fgSizer442.Add( self.m_staticText2142, 0, wx.ALL, 5 )

		self.resist_c_investigation42 = wx.TextCtrl( self.resist_council_52, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer442.Add( self.resist_c_investigation42, 0, wx.ALL, 5 )

		self.m_staticText2242 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2242.Wrap( -1 )

		fgSizer442.Add( self.m_staticText2242, 0, wx.ALL, 5 )

		self.resist_c_espionage42 = wx.TextCtrl( self.resist_council_52, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer442.Add( self.resist_c_espionage42, 0, wx.ALL, 5 )

		self.m_staticText2342 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2342.Wrap( -1 )

		fgSizer442.Add( self.m_staticText2342, 0, wx.ALL, 5 )

		self.resist_c_command42 = wx.TextCtrl( self.resist_council_52, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer442.Add( self.resist_c_command42, 0, wx.ALL, 5 )

		self.m_staticText2442 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2442.Wrap( -1 )

		fgSizer442.Add( self.m_staticText2442, 0, wx.ALL, 5 )

		self.resist_c_administration42 = wx.TextCtrl( self.resist_council_52, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer442.Add( self.resist_c_administration42, 0, wx.ALL, 5 )

		self.m_staticText2542 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2542.Wrap( -1 )

		fgSizer442.Add( self.m_staticText2542, 0, wx.ALL, 5 )

		self.resist_c_science42 = wx.TextCtrl( self.resist_council_52, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer442.Add( self.resist_c_science42, 0, wx.ALL, 5 )

		self.m_staticText2642 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2642.Wrap( -1 )

		fgSizer442.Add( self.m_staticText2642, 0, wx.ALL, 5 )

		self.resist_c_security42 = wx.TextCtrl( self.resist_council_52, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer442.Add( self.resist_c_security42, 0, wx.ALL, 5 )

		self.m_staticText2742 = wx.StaticText( self.resist_council_52, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2742.Wrap( -1 )

		fgSizer442.Add( self.m_staticText2742, 0, wx.ALL, 5 )

		self.resist_c_loyalty42 = wx.TextCtrl( self.resist_council_52, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer442.Add( self.resist_c_loyalty42, 0, wx.ALL, 5 )


		self.resist_council_52.SetSizer( fgSizer442 )
		self.resist_council_52.Layout()
		fgSizer442.Fit( self.resist_council_52 )
		self.resist_sub_tabs2.AddPage( self.resist_council_52, u"Councilor 5", False )
		self.resist_council_62 = wx.Panel( self.resist_sub_tabs2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer452 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer452.SetFlexibleDirection( wx.BOTH )
		fgSizer452.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname52 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname52.Wrap( -1 )

		fgSizer452.Add( self.resist_c_fname52, 0, wx.ALL, 5 )

		self.resist_c_lname52 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname52.Wrap( -1 )

		fgSizer452.Add( self.resist_c_lname52, 0, wx.ALL, 5 )

		self.m_staticText8452 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8452.Wrap( -1 )

		fgSizer452.Add( self.m_staticText8452, 0, wx.ALL, 5 )

		resist_c_class52Choices = []
		self.resist_c_class52 = wx.Choice( self.resist_council_62, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class52Choices, 0 )
		self.resist_c_class52.SetSelection( 0 )
		fgSizer452.Add( self.resist_c_class52, 0, wx.ALL, 5 )

		self.m_staticText2052 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2052.Wrap( -1 )

		fgSizer452.Add( self.m_staticText2052, 0, wx.ALL, 5 )

		self.resist_c_persuasion52 = wx.TextCtrl( self.resist_council_62, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer452.Add( self.resist_c_persuasion52, 0, wx.ALL, 5 )

		self.m_staticText2152 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2152.Wrap( -1 )

		fgSizer452.Add( self.m_staticText2152, 0, wx.ALL, 5 )

		self.resist_c_investigation52 = wx.TextCtrl( self.resist_council_62, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer452.Add( self.resist_c_investigation52, 0, wx.ALL, 5 )

		self.m_staticText2252 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2252.Wrap( -1 )

		fgSizer452.Add( self.m_staticText2252, 0, wx.ALL, 5 )

		self.resist_c_espionage52 = wx.TextCtrl( self.resist_council_62, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer452.Add( self.resist_c_espionage52, 0, wx.ALL, 5 )

		self.m_staticText2352 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2352.Wrap( -1 )

		fgSizer452.Add( self.m_staticText2352, 0, wx.ALL, 5 )

		self.resist_c_command52 = wx.TextCtrl( self.resist_council_62, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer452.Add( self.resist_c_command52, 0, wx.ALL, 5 )

		self.m_staticText2452 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2452.Wrap( -1 )

		fgSizer452.Add( self.m_staticText2452, 0, wx.ALL, 5 )

		self.resist_c_administration52 = wx.TextCtrl( self.resist_council_62, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer452.Add( self.resist_c_administration52, 0, wx.ALL, 5 )

		self.m_staticText2552 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2552.Wrap( -1 )

		fgSizer452.Add( self.m_staticText2552, 0, wx.ALL, 5 )

		self.resist_c_science52 = wx.TextCtrl( self.resist_council_62, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer452.Add( self.resist_c_science52, 0, wx.ALL, 5 )

		self.m_staticText2652 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2652.Wrap( -1 )

		fgSizer452.Add( self.m_staticText2652, 0, wx.ALL, 5 )

		self.resist_c_security52 = wx.TextCtrl( self.resist_council_62, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer452.Add( self.resist_c_security52, 0, wx.ALL, 5 )

		self.m_staticText2752 = wx.StaticText( self.resist_council_62, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2752.Wrap( -1 )

		fgSizer452.Add( self.m_staticText2752, 0, wx.ALL, 5 )

		self.resist_c_loyalty52 = wx.TextCtrl( self.resist_council_62, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer452.Add( self.resist_c_loyalty52, 0, wx.ALL, 5 )


		self.resist_council_62.SetSizer( fgSizer452 )
		self.resist_council_62.Layout()
		fgSizer452.Fit( self.resist_council_62 )
		self.resist_sub_tabs2.AddPage( self.resist_council_62, u"Councilor 6", False )

		bSizer32.Add( self.resist_sub_tabs2, 0, wx.EXPAND |wx.ALL, 5 )


		self.initiave_panel.SetSizer( bSizer32 )
		self.initiave_panel.Layout()
		bSizer32.Fit( self.initiave_panel )
		self.app_tabs.AddPage( self.initiave_panel, u"The Initiative", False )
		self.heratic_panel = wx.Panel( self.app_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		gSizer121 = wx.GridSizer( 0, 3, 0, 0 )

		self.player_flag3 = wx.CheckBox( self.heratic_panel, wx.ID_ANY, u"Player Faction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer121.Add( self.player_flag3, 0, wx.ALL, 5 )


		bSizer33.Add( gSizer121, 1, wx.EXPAND, 5 )

		self.resist_sub_tabs3 = wx.Notebook( self.heratic_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_resource_panel3 = wx.Panel( self.resist_sub_tabs3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer23 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText210 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Money", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText210.Wrap( -1 )

		fgSizer23.Add( self.m_staticText210, 0, wx.ALL, 5 )

		self.resist_money3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_money3, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Influence", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		fgSizer23.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.resist_influence3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_influence3, 0, wx.ALL, 5 )

		self.m_staticText43 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Ops", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		fgSizer23.Add( self.m_staticText43, 0, wx.ALL, 5 )

		self.resist_ops3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_ops3, 0, wx.ALL, 5 )

		self.m_staticText53 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Boost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		fgSizer23.Add( self.m_staticText53, 0, wx.ALL, 5 )

		self.resist_boost3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_boost3, 0, wx.ALL, 5 )

		self.m_staticText63 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Water", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		fgSizer23.Add( self.m_staticText63, 0, wx.ALL, 5 )

		self.resist_water3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_water3, 0, wx.ALL, 5 )

		self.m_staticText73 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Volatiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )

		fgSizer23.Add( self.m_staticText73, 0, wx.ALL, 5 )

		self.resist_volatiles3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_volatiles3, 0, wx.ALL, 5 )

		self.m_staticText83 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Base Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer23.Add( self.m_staticText83, 0, wx.ALL, 5 )

		self.resist_basemetals3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_basemetals3, 0, wx.ALL, 5 )

		self.m_staticText93 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Noble Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )

		fgSizer23.Add( self.m_staticText93, 0, wx.ALL, 5 )

		self.resist_noblemetals3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_noblemetals3, 0, wx.ALL, 5 )

		self.m_staticText103 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Fissiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText103.Wrap( -1 )

		fgSizer23.Add( self.m_staticText103, 0, wx.ALL, 5 )

		self.resist_fissiles3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_fissiles3, 0, wx.ALL, 5 )

		self.m_staticText113 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Exotics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText113.Wrap( -1 )

		fgSizer23.Add( self.m_staticText113, 0, wx.ALL, 5 )

		self.resist_exotics3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_exotics3, 0, wx.ALL, 5 )

		self.m_staticText123 = wx.StaticText( self.resist_resource_panel3, wx.ID_ANY, u"Antimatter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText123.Wrap( -1 )

		fgSizer23.Add( self.m_staticText123, 0, wx.ALL, 5 )

		self.resist_antimatter3 = wx.TextCtrl( self.resist_resource_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.resist_antimatter3, 0, wx.ALL, 5 )


		self.resist_resource_panel3.SetSizer( fgSizer23 )
		self.resist_resource_panel3.Layout()
		fgSizer23.Fit( self.resist_resource_panel3 )
		self.resist_sub_tabs3.AddPage( self.resist_resource_panel3, u"Resources", True )
		self.resist_projects3 = wx.Panel( self.resist_sub_tabs3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer33 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText153 = wx.StaticText( self.resist_projects3, wx.ID_ANY, u"Active Project", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText153.Wrap( -1 )

		fgSizer33.Add( self.m_staticText153, 0, wx.ALL, 5 )

		self.m_staticText173 = wx.StaticText( self.resist_projects3, wx.ID_ANY, u"Current Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText173.Wrap( -1 )

		fgSizer33.Add( self.m_staticText173, 0, wx.ALL, 5 )

		self.resist_project13 = wx.StaticText( self.resist_projects3, wx.ID_ANY, u"Project 1 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project13.Wrap( -1 )

		fgSizer33.Add( self.resist_project13, 0, wx.ALL, 5 )

		self.resist_project1_progress3 = wx.TextCtrl( self.resist_projects3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.resist_project1_progress3, 0, wx.ALL, 5 )

		self.resist_project23 = wx.StaticText( self.resist_projects3, wx.ID_ANY, u"Project 2 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project23.Wrap( -1 )

		fgSizer33.Add( self.resist_project23, 0, wx.ALL, 5 )

		self.resist_project2_progress3 = wx.TextCtrl( self.resist_projects3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.resist_project2_progress3, 0, wx.ALL, 5 )

		self.resist_project33 = wx.StaticText( self.resist_projects3, wx.ID_ANY, u"Project 3 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project33.Wrap( -1 )

		fgSizer33.Add( self.resist_project33, 0, wx.ALL, 5 )

		self.resist_project3_progress3 = wx.TextCtrl( self.resist_projects3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.resist_project3_progress3, 0, wx.ALL, 5 )


		self.resist_projects3.SetSizer( fgSizer33 )
		self.resist_projects3.Layout()
		fgSizer33.Fit( self.resist_projects3 )
		self.resist_sub_tabs3.AddPage( self.resist_projects3, u"Project Research", False )
		self.resist_council_13 = wx.Panel( self.resist_sub_tabs3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer48 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer48.SetFlexibleDirection( wx.BOTH )
		fgSizer48.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname8 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname8.Wrap( -1 )

		fgSizer48.Add( self.resist_c_fname8, 0, wx.ALL, 5 )

		self.resist_c_lname8 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname8.Wrap( -1 )

		fgSizer48.Add( self.resist_c_lname8, 0, wx.ALL, 5 )

		self.m_staticText848 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText848.Wrap( -1 )

		fgSizer48.Add( self.m_staticText848, 0, wx.ALL, 5 )

		resist_c_class8Choices = []
		self.resist_c_class8 = wx.Choice( self.resist_council_13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class8Choices, 0 )
		self.resist_c_class8.SetSelection( 0 )
		fgSizer48.Add( self.resist_c_class8, 0, wx.ALL, 5 )

		self.m_staticText208 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText208.Wrap( -1 )

		fgSizer48.Add( self.m_staticText208, 0, wx.ALL, 5 )

		self.resist_c_persuasion8 = wx.TextCtrl( self.resist_council_13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer48.Add( self.resist_c_persuasion8, 0, wx.ALL, 5 )

		self.m_staticText218 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText218.Wrap( -1 )

		fgSizer48.Add( self.m_staticText218, 0, wx.ALL, 5 )

		self.resist_c_investigation8 = wx.TextCtrl( self.resist_council_13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer48.Add( self.resist_c_investigation8, 0, wx.ALL, 5 )

		self.m_staticText228 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText228.Wrap( -1 )

		fgSizer48.Add( self.m_staticText228, 0, wx.ALL, 5 )

		self.resist_c_espionage8 = wx.TextCtrl( self.resist_council_13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer48.Add( self.resist_c_espionage8, 0, wx.ALL, 5 )

		self.m_staticText238 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText238.Wrap( -1 )

		fgSizer48.Add( self.m_staticText238, 0, wx.ALL, 5 )

		self.resist_c_command8 = wx.TextCtrl( self.resist_council_13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer48.Add( self.resist_c_command8, 0, wx.ALL, 5 )

		self.m_staticText248 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText248.Wrap( -1 )

		fgSizer48.Add( self.m_staticText248, 0, wx.ALL, 5 )

		self.resist_c_administration8 = wx.TextCtrl( self.resist_council_13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer48.Add( self.resist_c_administration8, 0, wx.ALL, 5 )

		self.m_staticText258 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText258.Wrap( -1 )

		fgSizer48.Add( self.m_staticText258, 0, wx.ALL, 5 )

		self.resist_c_science8 = wx.TextCtrl( self.resist_council_13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer48.Add( self.resist_c_science8, 0, wx.ALL, 5 )

		self.m_staticText268 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText268.Wrap( -1 )

		fgSizer48.Add( self.m_staticText268, 0, wx.ALL, 5 )

		self.resist_c_security8 = wx.TextCtrl( self.resist_council_13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer48.Add( self.resist_c_security8, 0, wx.ALL, 5 )

		self.m_staticText278 = wx.StaticText( self.resist_council_13, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText278.Wrap( -1 )

		fgSizer48.Add( self.m_staticText278, 0, wx.ALL, 5 )

		self.resist_c_loyalty8 = wx.TextCtrl( self.resist_council_13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer48.Add( self.resist_c_loyalty8, 0, wx.ALL, 5 )


		self.resist_council_13.SetSizer( fgSizer48 )
		self.resist_council_13.Layout()
		fgSizer48.Fit( self.resist_council_13 )
		self.resist_sub_tabs3.AddPage( self.resist_council_13, u"Councilor 1", False )
		self.resist_council_23 = wx.Panel( self.resist_sub_tabs3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer413 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer413.SetFlexibleDirection( wx.BOTH )
		fgSizer413.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname13 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname13.Wrap( -1 )

		fgSizer413.Add( self.resist_c_fname13, 0, wx.ALL, 5 )

		self.resist_c_lname13 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname13.Wrap( -1 )

		fgSizer413.Add( self.resist_c_lname13, 0, wx.ALL, 5 )

		self.m_staticText8413 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8413.Wrap( -1 )

		fgSizer413.Add( self.m_staticText8413, 0, wx.ALL, 5 )

		resist_c_class13Choices = []
		self.resist_c_class13 = wx.Choice( self.resist_council_23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class13Choices, 0 )
		self.resist_c_class13.SetSelection( 0 )
		fgSizer413.Add( self.resist_c_class13, 0, wx.ALL, 5 )

		self.m_staticText2013 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2013.Wrap( -1 )

		fgSizer413.Add( self.m_staticText2013, 0, wx.ALL, 5 )

		self.resist_c_persuasion13 = wx.TextCtrl( self.resist_council_23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer413.Add( self.resist_c_persuasion13, 0, wx.ALL, 5 )

		self.m_staticText2113 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2113.Wrap( -1 )

		fgSizer413.Add( self.m_staticText2113, 0, wx.ALL, 5 )

		self.resist_c_investigation13 = wx.TextCtrl( self.resist_council_23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer413.Add( self.resist_c_investigation13, 0, wx.ALL, 5 )

		self.m_staticText2213 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2213.Wrap( -1 )

		fgSizer413.Add( self.m_staticText2213, 0, wx.ALL, 5 )

		self.resist_c_espionage13 = wx.TextCtrl( self.resist_council_23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer413.Add( self.resist_c_espionage13, 0, wx.ALL, 5 )

		self.m_staticText2313 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2313.Wrap( -1 )

		fgSizer413.Add( self.m_staticText2313, 0, wx.ALL, 5 )

		self.resist_c_command13 = wx.TextCtrl( self.resist_council_23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer413.Add( self.resist_c_command13, 0, wx.ALL, 5 )

		self.m_staticText2413 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2413.Wrap( -1 )

		fgSizer413.Add( self.m_staticText2413, 0, wx.ALL, 5 )

		self.resist_c_administration13 = wx.TextCtrl( self.resist_council_23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer413.Add( self.resist_c_administration13, 0, wx.ALL, 5 )

		self.m_staticText2513 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2513.Wrap( -1 )

		fgSizer413.Add( self.m_staticText2513, 0, wx.ALL, 5 )

		self.resist_c_science13 = wx.TextCtrl( self.resist_council_23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer413.Add( self.resist_c_science13, 0, wx.ALL, 5 )

		self.m_staticText2613 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2613.Wrap( -1 )

		fgSizer413.Add( self.m_staticText2613, 0, wx.ALL, 5 )

		self.resist_c_security13 = wx.TextCtrl( self.resist_council_23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer413.Add( self.resist_c_security13, 0, wx.ALL, 5 )

		self.m_staticText2713 = wx.StaticText( self.resist_council_23, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2713.Wrap( -1 )

		fgSizer413.Add( self.m_staticText2713, 0, wx.ALL, 5 )

		self.resist_c_loyalty13 = wx.TextCtrl( self.resist_council_23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer413.Add( self.resist_c_loyalty13, 0, wx.ALL, 5 )


		self.resist_council_23.SetSizer( fgSizer413 )
		self.resist_council_23.Layout()
		fgSizer413.Fit( self.resist_council_23 )
		self.resist_sub_tabs3.AddPage( self.resist_council_23, u"Councilor 2", False )
		self.resist_council_33 = wx.Panel( self.resist_sub_tabs3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer423 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer423.SetFlexibleDirection( wx.BOTH )
		fgSizer423.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname23 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname23.Wrap( -1 )

		fgSizer423.Add( self.resist_c_fname23, 0, wx.ALL, 5 )

		self.resist_c_lname23 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname23.Wrap( -1 )

		fgSizer423.Add( self.resist_c_lname23, 0, wx.ALL, 5 )

		self.m_staticText8423 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8423.Wrap( -1 )

		fgSizer423.Add( self.m_staticText8423, 0, wx.ALL, 5 )

		resist_c_class23Choices = []
		self.resist_c_class23 = wx.Choice( self.resist_council_33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class23Choices, 0 )
		self.resist_c_class23.SetSelection( 0 )
		fgSizer423.Add( self.resist_c_class23, 0, wx.ALL, 5 )

		self.m_staticText2023 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2023.Wrap( -1 )

		fgSizer423.Add( self.m_staticText2023, 0, wx.ALL, 5 )

		self.resist_c_persuasion23 = wx.TextCtrl( self.resist_council_33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer423.Add( self.resist_c_persuasion23, 0, wx.ALL, 5 )

		self.m_staticText2123 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2123.Wrap( -1 )

		fgSizer423.Add( self.m_staticText2123, 0, wx.ALL, 5 )

		self.resist_c_investigation23 = wx.TextCtrl( self.resist_council_33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer423.Add( self.resist_c_investigation23, 0, wx.ALL, 5 )

		self.m_staticText2223 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2223.Wrap( -1 )

		fgSizer423.Add( self.m_staticText2223, 0, wx.ALL, 5 )

		self.resist_c_espionage23 = wx.TextCtrl( self.resist_council_33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer423.Add( self.resist_c_espionage23, 0, wx.ALL, 5 )

		self.m_staticText2323 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2323.Wrap( -1 )

		fgSizer423.Add( self.m_staticText2323, 0, wx.ALL, 5 )

		self.resist_c_command23 = wx.TextCtrl( self.resist_council_33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer423.Add( self.resist_c_command23, 0, wx.ALL, 5 )

		self.m_staticText2423 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2423.Wrap( -1 )

		fgSizer423.Add( self.m_staticText2423, 0, wx.ALL, 5 )

		self.resist_c_administration23 = wx.TextCtrl( self.resist_council_33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer423.Add( self.resist_c_administration23, 0, wx.ALL, 5 )

		self.m_staticText2523 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2523.Wrap( -1 )

		fgSizer423.Add( self.m_staticText2523, 0, wx.ALL, 5 )

		self.resist_c_science23 = wx.TextCtrl( self.resist_council_33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer423.Add( self.resist_c_science23, 0, wx.ALL, 5 )

		self.m_staticText2623 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2623.Wrap( -1 )

		fgSizer423.Add( self.m_staticText2623, 0, wx.ALL, 5 )

		self.resist_c_security23 = wx.TextCtrl( self.resist_council_33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer423.Add( self.resist_c_security23, 0, wx.ALL, 5 )

		self.m_staticText2723 = wx.StaticText( self.resist_council_33, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2723.Wrap( -1 )

		fgSizer423.Add( self.m_staticText2723, 0, wx.ALL, 5 )

		self.resist_c_loyalty23 = wx.TextCtrl( self.resist_council_33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer423.Add( self.resist_c_loyalty23, 0, wx.ALL, 5 )


		self.resist_council_33.SetSizer( fgSizer423 )
		self.resist_council_33.Layout()
		fgSizer423.Fit( self.resist_council_33 )
		self.resist_sub_tabs3.AddPage( self.resist_council_33, u"Councilor 3", False )
		self.resist_council_43 = wx.Panel( self.resist_sub_tabs3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer433 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer433.SetFlexibleDirection( wx.BOTH )
		fgSizer433.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname33 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname33.Wrap( -1 )

		fgSizer433.Add( self.resist_c_fname33, 0, wx.ALL, 5 )

		self.resist_c_lname33 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname33.Wrap( -1 )

		fgSizer433.Add( self.resist_c_lname33, 0, wx.ALL, 5 )

		self.m_staticText8433 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8433.Wrap( -1 )

		fgSizer433.Add( self.m_staticText8433, 0, wx.ALL, 5 )

		resist_c_class33Choices = []
		self.resist_c_class33 = wx.Choice( self.resist_council_43, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class33Choices, 0 )
		self.resist_c_class33.SetSelection( 0 )
		fgSizer433.Add( self.resist_c_class33, 0, wx.ALL, 5 )

		self.m_staticText2033 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2033.Wrap( -1 )

		fgSizer433.Add( self.m_staticText2033, 0, wx.ALL, 5 )

		self.resist_c_persuasion33 = wx.TextCtrl( self.resist_council_43, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer433.Add( self.resist_c_persuasion33, 0, wx.ALL, 5 )

		self.m_staticText2133 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2133.Wrap( -1 )

		fgSizer433.Add( self.m_staticText2133, 0, wx.ALL, 5 )

		self.resist_c_investigation33 = wx.TextCtrl( self.resist_council_43, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer433.Add( self.resist_c_investigation33, 0, wx.ALL, 5 )

		self.m_staticText2233 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2233.Wrap( -1 )

		fgSizer433.Add( self.m_staticText2233, 0, wx.ALL, 5 )

		self.resist_c_espionage33 = wx.TextCtrl( self.resist_council_43, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer433.Add( self.resist_c_espionage33, 0, wx.ALL, 5 )

		self.m_staticText2333 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2333.Wrap( -1 )

		fgSizer433.Add( self.m_staticText2333, 0, wx.ALL, 5 )

		self.resist_c_command33 = wx.TextCtrl( self.resist_council_43, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer433.Add( self.resist_c_command33, 0, wx.ALL, 5 )

		self.m_staticText2433 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2433.Wrap( -1 )

		fgSizer433.Add( self.m_staticText2433, 0, wx.ALL, 5 )

		self.resist_c_administration33 = wx.TextCtrl( self.resist_council_43, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer433.Add( self.resist_c_administration33, 0, wx.ALL, 5 )

		self.m_staticText2533 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2533.Wrap( -1 )

		fgSizer433.Add( self.m_staticText2533, 0, wx.ALL, 5 )

		self.resist_c_science33 = wx.TextCtrl( self.resist_council_43, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer433.Add( self.resist_c_science33, 0, wx.ALL, 5 )

		self.m_staticText2633 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2633.Wrap( -1 )

		fgSizer433.Add( self.m_staticText2633, 0, wx.ALL, 5 )

		self.resist_c_security33 = wx.TextCtrl( self.resist_council_43, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer433.Add( self.resist_c_security33, 0, wx.ALL, 5 )

		self.m_staticText2733 = wx.StaticText( self.resist_council_43, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2733.Wrap( -1 )

		fgSizer433.Add( self.m_staticText2733, 0, wx.ALL, 5 )

		self.resist_c_loyalty33 = wx.TextCtrl( self.resist_council_43, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer433.Add( self.resist_c_loyalty33, 0, wx.ALL, 5 )


		self.resist_council_43.SetSizer( fgSizer433 )
		self.resist_council_43.Layout()
		fgSizer433.Fit( self.resist_council_43 )
		self.resist_sub_tabs3.AddPage( self.resist_council_43, u"Councilor 4", False )
		self.resist_council_53 = wx.Panel( self.resist_sub_tabs3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer443 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer443.SetFlexibleDirection( wx.BOTH )
		fgSizer443.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname43 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname43.Wrap( -1 )

		fgSizer443.Add( self.resist_c_fname43, 0, wx.ALL, 5 )

		self.resist_c_lname43 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname43.Wrap( -1 )

		fgSizer443.Add( self.resist_c_lname43, 0, wx.ALL, 5 )

		self.m_staticText8443 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8443.Wrap( -1 )

		fgSizer443.Add( self.m_staticText8443, 0, wx.ALL, 5 )

		resist_c_class43Choices = []
		self.resist_c_class43 = wx.Choice( self.resist_council_53, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class43Choices, 0 )
		self.resist_c_class43.SetSelection( 0 )
		fgSizer443.Add( self.resist_c_class43, 0, wx.ALL, 5 )

		self.m_staticText2043 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2043.Wrap( -1 )

		fgSizer443.Add( self.m_staticText2043, 0, wx.ALL, 5 )

		self.resist_c_persuasion43 = wx.TextCtrl( self.resist_council_53, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer443.Add( self.resist_c_persuasion43, 0, wx.ALL, 5 )

		self.m_staticText2143 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2143.Wrap( -1 )

		fgSizer443.Add( self.m_staticText2143, 0, wx.ALL, 5 )

		self.resist_c_investigation43 = wx.TextCtrl( self.resist_council_53, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer443.Add( self.resist_c_investigation43, 0, wx.ALL, 5 )

		self.m_staticText2243 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2243.Wrap( -1 )

		fgSizer443.Add( self.m_staticText2243, 0, wx.ALL, 5 )

		self.resist_c_espionage43 = wx.TextCtrl( self.resist_council_53, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer443.Add( self.resist_c_espionage43, 0, wx.ALL, 5 )

		self.m_staticText2343 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2343.Wrap( -1 )

		fgSizer443.Add( self.m_staticText2343, 0, wx.ALL, 5 )

		self.resist_c_command43 = wx.TextCtrl( self.resist_council_53, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer443.Add( self.resist_c_command43, 0, wx.ALL, 5 )

		self.m_staticText2443 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2443.Wrap( -1 )

		fgSizer443.Add( self.m_staticText2443, 0, wx.ALL, 5 )

		self.resist_c_administration43 = wx.TextCtrl( self.resist_council_53, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer443.Add( self.resist_c_administration43, 0, wx.ALL, 5 )

		self.m_staticText2543 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2543.Wrap( -1 )

		fgSizer443.Add( self.m_staticText2543, 0, wx.ALL, 5 )

		self.resist_c_science43 = wx.TextCtrl( self.resist_council_53, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer443.Add( self.resist_c_science43, 0, wx.ALL, 5 )

		self.m_staticText2643 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2643.Wrap( -1 )

		fgSizer443.Add( self.m_staticText2643, 0, wx.ALL, 5 )

		self.resist_c_security43 = wx.TextCtrl( self.resist_council_53, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer443.Add( self.resist_c_security43, 0, wx.ALL, 5 )

		self.m_staticText2743 = wx.StaticText( self.resist_council_53, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2743.Wrap( -1 )

		fgSizer443.Add( self.m_staticText2743, 0, wx.ALL, 5 )

		self.resist_c_loyalty43 = wx.TextCtrl( self.resist_council_53, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer443.Add( self.resist_c_loyalty43, 0, wx.ALL, 5 )


		self.resist_council_53.SetSizer( fgSizer443 )
		self.resist_council_53.Layout()
		fgSizer443.Fit( self.resist_council_53 )
		self.resist_sub_tabs3.AddPage( self.resist_council_53, u"Councilor 5", False )
		self.resist_council_63 = wx.Panel( self.resist_sub_tabs3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer453 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer453.SetFlexibleDirection( wx.BOTH )
		fgSizer453.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname53 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname53.Wrap( -1 )

		fgSizer453.Add( self.resist_c_fname53, 0, wx.ALL, 5 )

		self.resist_c_lname53 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname53.Wrap( -1 )

		fgSizer453.Add( self.resist_c_lname53, 0, wx.ALL, 5 )

		self.m_staticText8453 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8453.Wrap( -1 )

		fgSizer453.Add( self.m_staticText8453, 0, wx.ALL, 5 )

		resist_c_class53Choices = []
		self.resist_c_class53 = wx.Choice( self.resist_council_63, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class53Choices, 0 )
		self.resist_c_class53.SetSelection( 0 )
		fgSizer453.Add( self.resist_c_class53, 0, wx.ALL, 5 )

		self.m_staticText2053 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2053.Wrap( -1 )

		fgSizer453.Add( self.m_staticText2053, 0, wx.ALL, 5 )

		self.resist_c_persuasion53 = wx.TextCtrl( self.resist_council_63, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer453.Add( self.resist_c_persuasion53, 0, wx.ALL, 5 )

		self.m_staticText2153 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2153.Wrap( -1 )

		fgSizer453.Add( self.m_staticText2153, 0, wx.ALL, 5 )

		self.resist_c_investigation53 = wx.TextCtrl( self.resist_council_63, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer453.Add( self.resist_c_investigation53, 0, wx.ALL, 5 )

		self.m_staticText2253 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2253.Wrap( -1 )

		fgSizer453.Add( self.m_staticText2253, 0, wx.ALL, 5 )

		self.resist_c_espionage53 = wx.TextCtrl( self.resist_council_63, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer453.Add( self.resist_c_espionage53, 0, wx.ALL, 5 )

		self.m_staticText2353 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2353.Wrap( -1 )

		fgSizer453.Add( self.m_staticText2353, 0, wx.ALL, 5 )

		self.resist_c_command53 = wx.TextCtrl( self.resist_council_63, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer453.Add( self.resist_c_command53, 0, wx.ALL, 5 )

		self.m_staticText2453 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2453.Wrap( -1 )

		fgSizer453.Add( self.m_staticText2453, 0, wx.ALL, 5 )

		self.resist_c_administration53 = wx.TextCtrl( self.resist_council_63, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer453.Add( self.resist_c_administration53, 0, wx.ALL, 5 )

		self.m_staticText2553 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2553.Wrap( -1 )

		fgSizer453.Add( self.m_staticText2553, 0, wx.ALL, 5 )

		self.resist_c_science53 = wx.TextCtrl( self.resist_council_63, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer453.Add( self.resist_c_science53, 0, wx.ALL, 5 )

		self.m_staticText2653 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2653.Wrap( -1 )

		fgSizer453.Add( self.m_staticText2653, 0, wx.ALL, 5 )

		self.resist_c_security53 = wx.TextCtrl( self.resist_council_63, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer453.Add( self.resist_c_security53, 0, wx.ALL, 5 )

		self.m_staticText2753 = wx.StaticText( self.resist_council_63, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2753.Wrap( -1 )

		fgSizer453.Add( self.m_staticText2753, 0, wx.ALL, 5 )

		self.resist_c_loyalty53 = wx.TextCtrl( self.resist_council_63, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer453.Add( self.resist_c_loyalty53, 0, wx.ALL, 5 )


		self.resist_council_63.SetSizer( fgSizer453 )
		self.resist_council_63.Layout()
		fgSizer453.Fit( self.resist_council_63 )
		self.resist_sub_tabs3.AddPage( self.resist_council_63, u"Councilor 6", False )

		bSizer33.Add( self.resist_sub_tabs3, 0, wx.EXPAND |wx.ALL, 5 )


		self.heratic_panel.SetSizer( bSizer33 )
		self.heratic_panel.Layout()
		bSizer33.Fit( self.heratic_panel )
		self.app_tabs.AddPage( self.heratic_panel, u"The Servants", False )
		self.protectorate_panel = wx.Panel( self.app_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		gSizer122 = wx.GridSizer( 0, 3, 0, 0 )

		self.player_flag4 = wx.CheckBox( self.protectorate_panel, wx.ID_ANY, u"Player Faction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer122.Add( self.player_flag4, 0, wx.ALL, 5 )

		self.m_staticText581122 = wx.StaticText( self.protectorate_panel, wx.ID_ANY, u"Alien Hate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText581122.Wrap( -1 )

		gSizer122.Add( self.m_staticText581122, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_spinCtrl24 = wx.SpinCtrl( self.protectorate_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer122.Add( self.m_spinCtrl24, 0, wx.ALL, 5 )


		bSizer34.Add( gSizer122, 1, wx.EXPAND, 5 )

		self.resist_sub_tabs4 = wx.Notebook( self.protectorate_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_resource_panel4 = wx.Panel( self.resist_sub_tabs4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer24 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText219 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Money", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText219.Wrap( -1 )

		fgSizer24.Add( self.m_staticText219, 0, wx.ALL, 5 )

		self.resist_money4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_money4, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Influence", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		fgSizer24.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.resist_influence4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_influence4, 0, wx.ALL, 5 )

		self.m_staticText44 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Ops", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		fgSizer24.Add( self.m_staticText44, 0, wx.ALL, 5 )

		self.resist_ops4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_ops4, 0, wx.ALL, 5 )

		self.m_staticText54 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Boost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		fgSizer24.Add( self.m_staticText54, 0, wx.ALL, 5 )

		self.resist_boost4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_boost4, 0, wx.ALL, 5 )

		self.m_staticText64 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Water", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )

		fgSizer24.Add( self.m_staticText64, 0, wx.ALL, 5 )

		self.resist_water4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_water4, 0, wx.ALL, 5 )

		self.m_staticText74 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Volatiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		fgSizer24.Add( self.m_staticText74, 0, wx.ALL, 5 )

		self.resist_volatiles4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_volatiles4, 0, wx.ALL, 5 )

		self.m_staticText85 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Base Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		fgSizer24.Add( self.m_staticText85, 0, wx.ALL, 5 )

		self.resist_basemetals4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_basemetals4, 0, wx.ALL, 5 )

		self.m_staticText94 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Noble Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( -1 )

		fgSizer24.Add( self.m_staticText94, 0, wx.ALL, 5 )

		self.resist_noblemetals4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_noblemetals4, 0, wx.ALL, 5 )

		self.m_staticText104 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Fissiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText104.Wrap( -1 )

		fgSizer24.Add( self.m_staticText104, 0, wx.ALL, 5 )

		self.resist_fissiles4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_fissiles4, 0, wx.ALL, 5 )

		self.m_staticText114 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Exotics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText114.Wrap( -1 )

		fgSizer24.Add( self.m_staticText114, 0, wx.ALL, 5 )

		self.resist_exotics4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_exotics4, 0, wx.ALL, 5 )

		self.m_staticText124 = wx.StaticText( self.resist_resource_panel4, wx.ID_ANY, u"Antimatter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText124.Wrap( -1 )

		fgSizer24.Add( self.m_staticText124, 0, wx.ALL, 5 )

		self.resist_antimatter4 = wx.TextCtrl( self.resist_resource_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.resist_antimatter4, 0, wx.ALL, 5 )


		self.resist_resource_panel4.SetSizer( fgSizer24 )
		self.resist_resource_panel4.Layout()
		fgSizer24.Fit( self.resist_resource_panel4 )
		self.resist_sub_tabs4.AddPage( self.resist_resource_panel4, u"Resources", True )
		self.resist_projects4 = wx.Panel( self.resist_sub_tabs4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer34 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText154 = wx.StaticText( self.resist_projects4, wx.ID_ANY, u"Active Project", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText154.Wrap( -1 )

		fgSizer34.Add( self.m_staticText154, 0, wx.ALL, 5 )

		self.m_staticText174 = wx.StaticText( self.resist_projects4, wx.ID_ANY, u"Current Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText174.Wrap( -1 )

		fgSizer34.Add( self.m_staticText174, 0, wx.ALL, 5 )

		self.resist_project14 = wx.StaticText( self.resist_projects4, wx.ID_ANY, u"Project 1 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project14.Wrap( -1 )

		fgSizer34.Add( self.resist_project14, 0, wx.ALL, 5 )

		self.resist_project1_progress4 = wx.TextCtrl( self.resist_projects4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer34.Add( self.resist_project1_progress4, 0, wx.ALL, 5 )

		self.resist_project24 = wx.StaticText( self.resist_projects4, wx.ID_ANY, u"Project 2 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project24.Wrap( -1 )

		fgSizer34.Add( self.resist_project24, 0, wx.ALL, 5 )

		self.resist_project2_progress4 = wx.TextCtrl( self.resist_projects4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer34.Add( self.resist_project2_progress4, 0, wx.ALL, 5 )

		self.resist_project34 = wx.StaticText( self.resist_projects4, wx.ID_ANY, u"Project 3 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project34.Wrap( -1 )

		fgSizer34.Add( self.resist_project34, 0, wx.ALL, 5 )

		self.resist_project3_progress4 = wx.TextCtrl( self.resist_projects4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer34.Add( self.resist_project3_progress4, 0, wx.ALL, 5 )


		self.resist_projects4.SetSizer( fgSizer34 )
		self.resist_projects4.Layout()
		fgSizer34.Fit( self.resist_projects4 )
		self.resist_sub_tabs4.AddPage( self.resist_projects4, u"Project Research", False )
		self.resist_council_14 = wx.Panel( self.resist_sub_tabs4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer49 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer49.SetFlexibleDirection( wx.BOTH )
		fgSizer49.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname9 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname9.Wrap( -1 )

		fgSizer49.Add( self.resist_c_fname9, 0, wx.ALL, 5 )

		self.resist_c_lname9 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname9.Wrap( -1 )

		fgSizer49.Add( self.resist_c_lname9, 0, wx.ALL, 5 )

		self.m_staticText849 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText849.Wrap( -1 )

		fgSizer49.Add( self.m_staticText849, 0, wx.ALL, 5 )

		resist_c_class9Choices = []
		self.resist_c_class9 = wx.Choice( self.resist_council_14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class9Choices, 0 )
		self.resist_c_class9.SetSelection( 0 )
		fgSizer49.Add( self.resist_c_class9, 0, wx.ALL, 5 )

		self.m_staticText209 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText209.Wrap( -1 )

		fgSizer49.Add( self.m_staticText209, 0, wx.ALL, 5 )

		self.resist_c_persuasion9 = wx.TextCtrl( self.resist_council_14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.resist_c_persuasion9, 0, wx.ALL, 5 )

		self.m_staticText2110 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2110.Wrap( -1 )

		fgSizer49.Add( self.m_staticText2110, 0, wx.ALL, 5 )

		self.resist_c_investigation9 = wx.TextCtrl( self.resist_council_14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.resist_c_investigation9, 0, wx.ALL, 5 )

		self.m_staticText229 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText229.Wrap( -1 )

		fgSizer49.Add( self.m_staticText229, 0, wx.ALL, 5 )

		self.resist_c_espionage9 = wx.TextCtrl( self.resist_council_14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.resist_c_espionage9, 0, wx.ALL, 5 )

		self.m_staticText239 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText239.Wrap( -1 )

		fgSizer49.Add( self.m_staticText239, 0, wx.ALL, 5 )

		self.resist_c_command9 = wx.TextCtrl( self.resist_council_14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.resist_c_command9, 0, wx.ALL, 5 )

		self.m_staticText249 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText249.Wrap( -1 )

		fgSizer49.Add( self.m_staticText249, 0, wx.ALL, 5 )

		self.resist_c_administration9 = wx.TextCtrl( self.resist_council_14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.resist_c_administration9, 0, wx.ALL, 5 )

		self.m_staticText259 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText259.Wrap( -1 )

		fgSizer49.Add( self.m_staticText259, 0, wx.ALL, 5 )

		self.resist_c_science9 = wx.TextCtrl( self.resist_council_14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.resist_c_science9, 0, wx.ALL, 5 )

		self.m_staticText269 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText269.Wrap( -1 )

		fgSizer49.Add( self.m_staticText269, 0, wx.ALL, 5 )

		self.resist_c_security9 = wx.TextCtrl( self.resist_council_14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.resist_c_security9, 0, wx.ALL, 5 )

		self.m_staticText279 = wx.StaticText( self.resist_council_14, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText279.Wrap( -1 )

		fgSizer49.Add( self.m_staticText279, 0, wx.ALL, 5 )

		self.resist_c_loyalty9 = wx.TextCtrl( self.resist_council_14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.resist_c_loyalty9, 0, wx.ALL, 5 )


		self.resist_council_14.SetSizer( fgSizer49 )
		self.resist_council_14.Layout()
		fgSizer49.Fit( self.resist_council_14 )
		self.resist_sub_tabs4.AddPage( self.resist_council_14, u"Councilor 1", False )
		self.resist_council_24 = wx.Panel( self.resist_sub_tabs4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer414 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer414.SetFlexibleDirection( wx.BOTH )
		fgSizer414.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname14 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname14.Wrap( -1 )

		fgSizer414.Add( self.resist_c_fname14, 0, wx.ALL, 5 )

		self.resist_c_lname14 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname14.Wrap( -1 )

		fgSizer414.Add( self.resist_c_lname14, 0, wx.ALL, 5 )

		self.m_staticText8414 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8414.Wrap( -1 )

		fgSizer414.Add( self.m_staticText8414, 0, wx.ALL, 5 )

		resist_c_class14Choices = []
		self.resist_c_class14 = wx.Choice( self.resist_council_24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class14Choices, 0 )
		self.resist_c_class14.SetSelection( 0 )
		fgSizer414.Add( self.resist_c_class14, 0, wx.ALL, 5 )

		self.m_staticText2014 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2014.Wrap( -1 )

		fgSizer414.Add( self.m_staticText2014, 0, wx.ALL, 5 )

		self.resist_c_persuasion14 = wx.TextCtrl( self.resist_council_24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer414.Add( self.resist_c_persuasion14, 0, wx.ALL, 5 )

		self.m_staticText2114 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2114.Wrap( -1 )

		fgSizer414.Add( self.m_staticText2114, 0, wx.ALL, 5 )

		self.resist_c_investigation14 = wx.TextCtrl( self.resist_council_24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer414.Add( self.resist_c_investigation14, 0, wx.ALL, 5 )

		self.m_staticText2214 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2214.Wrap( -1 )

		fgSizer414.Add( self.m_staticText2214, 0, wx.ALL, 5 )

		self.resist_c_espionage14 = wx.TextCtrl( self.resist_council_24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer414.Add( self.resist_c_espionage14, 0, wx.ALL, 5 )

		self.m_staticText2314 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2314.Wrap( -1 )

		fgSizer414.Add( self.m_staticText2314, 0, wx.ALL, 5 )

		self.resist_c_command14 = wx.TextCtrl( self.resist_council_24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer414.Add( self.resist_c_command14, 0, wx.ALL, 5 )

		self.m_staticText2414 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2414.Wrap( -1 )

		fgSizer414.Add( self.m_staticText2414, 0, wx.ALL, 5 )

		self.resist_c_administration14 = wx.TextCtrl( self.resist_council_24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer414.Add( self.resist_c_administration14, 0, wx.ALL, 5 )

		self.m_staticText2514 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2514.Wrap( -1 )

		fgSizer414.Add( self.m_staticText2514, 0, wx.ALL, 5 )

		self.resist_c_science14 = wx.TextCtrl( self.resist_council_24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer414.Add( self.resist_c_science14, 0, wx.ALL, 5 )

		self.m_staticText2614 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2614.Wrap( -1 )

		fgSizer414.Add( self.m_staticText2614, 0, wx.ALL, 5 )

		self.resist_c_security14 = wx.TextCtrl( self.resist_council_24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer414.Add( self.resist_c_security14, 0, wx.ALL, 5 )

		self.m_staticText2714 = wx.StaticText( self.resist_council_24, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2714.Wrap( -1 )

		fgSizer414.Add( self.m_staticText2714, 0, wx.ALL, 5 )

		self.resist_c_loyalty14 = wx.TextCtrl( self.resist_council_24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer414.Add( self.resist_c_loyalty14, 0, wx.ALL, 5 )


		self.resist_council_24.SetSizer( fgSizer414 )
		self.resist_council_24.Layout()
		fgSizer414.Fit( self.resist_council_24 )
		self.resist_sub_tabs4.AddPage( self.resist_council_24, u"Councilor 2", False )
		self.resist_council_34 = wx.Panel( self.resist_sub_tabs4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer424 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer424.SetFlexibleDirection( wx.BOTH )
		fgSizer424.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname24 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname24.Wrap( -1 )

		fgSizer424.Add( self.resist_c_fname24, 0, wx.ALL, 5 )

		self.resist_c_lname24 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname24.Wrap( -1 )

		fgSizer424.Add( self.resist_c_lname24, 0, wx.ALL, 5 )

		self.m_staticText8424 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8424.Wrap( -1 )

		fgSizer424.Add( self.m_staticText8424, 0, wx.ALL, 5 )

		resist_c_class24Choices = []
		self.resist_c_class24 = wx.Choice( self.resist_council_34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class24Choices, 0 )
		self.resist_c_class24.SetSelection( 0 )
		fgSizer424.Add( self.resist_c_class24, 0, wx.ALL, 5 )

		self.m_staticText2024 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2024.Wrap( -1 )

		fgSizer424.Add( self.m_staticText2024, 0, wx.ALL, 5 )

		self.resist_c_persuasion24 = wx.TextCtrl( self.resist_council_34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer424.Add( self.resist_c_persuasion24, 0, wx.ALL, 5 )

		self.m_staticText2124 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2124.Wrap( -1 )

		fgSizer424.Add( self.m_staticText2124, 0, wx.ALL, 5 )

		self.resist_c_investigation24 = wx.TextCtrl( self.resist_council_34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer424.Add( self.resist_c_investigation24, 0, wx.ALL, 5 )

		self.m_staticText2224 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2224.Wrap( -1 )

		fgSizer424.Add( self.m_staticText2224, 0, wx.ALL, 5 )

		self.resist_c_espionage24 = wx.TextCtrl( self.resist_council_34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer424.Add( self.resist_c_espionage24, 0, wx.ALL, 5 )

		self.m_staticText2324 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2324.Wrap( -1 )

		fgSizer424.Add( self.m_staticText2324, 0, wx.ALL, 5 )

		self.resist_c_command24 = wx.TextCtrl( self.resist_council_34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer424.Add( self.resist_c_command24, 0, wx.ALL, 5 )

		self.m_staticText2424 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2424.Wrap( -1 )

		fgSizer424.Add( self.m_staticText2424, 0, wx.ALL, 5 )

		self.resist_c_administration24 = wx.TextCtrl( self.resist_council_34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer424.Add( self.resist_c_administration24, 0, wx.ALL, 5 )

		self.m_staticText2524 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2524.Wrap( -1 )

		fgSizer424.Add( self.m_staticText2524, 0, wx.ALL, 5 )

		self.resist_c_science24 = wx.TextCtrl( self.resist_council_34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer424.Add( self.resist_c_science24, 0, wx.ALL, 5 )

		self.m_staticText2624 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2624.Wrap( -1 )

		fgSizer424.Add( self.m_staticText2624, 0, wx.ALL, 5 )

		self.resist_c_security24 = wx.TextCtrl( self.resist_council_34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer424.Add( self.resist_c_security24, 0, wx.ALL, 5 )

		self.m_staticText2724 = wx.StaticText( self.resist_council_34, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2724.Wrap( -1 )

		fgSizer424.Add( self.m_staticText2724, 0, wx.ALL, 5 )

		self.resist_c_loyalty24 = wx.TextCtrl( self.resist_council_34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer424.Add( self.resist_c_loyalty24, 0, wx.ALL, 5 )


		self.resist_council_34.SetSizer( fgSizer424 )
		self.resist_council_34.Layout()
		fgSizer424.Fit( self.resist_council_34 )
		self.resist_sub_tabs4.AddPage( self.resist_council_34, u"Councilor 3", False )
		self.resist_council_44 = wx.Panel( self.resist_sub_tabs4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer434 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer434.SetFlexibleDirection( wx.BOTH )
		fgSizer434.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname34 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname34.Wrap( -1 )

		fgSizer434.Add( self.resist_c_fname34, 0, wx.ALL, 5 )

		self.resist_c_lname34 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname34.Wrap( -1 )

		fgSizer434.Add( self.resist_c_lname34, 0, wx.ALL, 5 )

		self.m_staticText8434 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8434.Wrap( -1 )

		fgSizer434.Add( self.m_staticText8434, 0, wx.ALL, 5 )

		resist_c_class34Choices = []
		self.resist_c_class34 = wx.Choice( self.resist_council_44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class34Choices, 0 )
		self.resist_c_class34.SetSelection( 0 )
		fgSizer434.Add( self.resist_c_class34, 0, wx.ALL, 5 )

		self.m_staticText2034 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2034.Wrap( -1 )

		fgSizer434.Add( self.m_staticText2034, 0, wx.ALL, 5 )

		self.resist_c_persuasion34 = wx.TextCtrl( self.resist_council_44, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer434.Add( self.resist_c_persuasion34, 0, wx.ALL, 5 )

		self.m_staticText2134 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2134.Wrap( -1 )

		fgSizer434.Add( self.m_staticText2134, 0, wx.ALL, 5 )

		self.resist_c_investigation34 = wx.TextCtrl( self.resist_council_44, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer434.Add( self.resist_c_investigation34, 0, wx.ALL, 5 )

		self.m_staticText2234 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2234.Wrap( -1 )

		fgSizer434.Add( self.m_staticText2234, 0, wx.ALL, 5 )

		self.resist_c_espionage34 = wx.TextCtrl( self.resist_council_44, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer434.Add( self.resist_c_espionage34, 0, wx.ALL, 5 )

		self.m_staticText2334 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2334.Wrap( -1 )

		fgSizer434.Add( self.m_staticText2334, 0, wx.ALL, 5 )

		self.resist_c_command34 = wx.TextCtrl( self.resist_council_44, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer434.Add( self.resist_c_command34, 0, wx.ALL, 5 )

		self.m_staticText2434 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2434.Wrap( -1 )

		fgSizer434.Add( self.m_staticText2434, 0, wx.ALL, 5 )

		self.resist_c_administration34 = wx.TextCtrl( self.resist_council_44, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer434.Add( self.resist_c_administration34, 0, wx.ALL, 5 )

		self.m_staticText2534 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2534.Wrap( -1 )

		fgSizer434.Add( self.m_staticText2534, 0, wx.ALL, 5 )

		self.resist_c_science34 = wx.TextCtrl( self.resist_council_44, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer434.Add( self.resist_c_science34, 0, wx.ALL, 5 )

		self.m_staticText2634 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2634.Wrap( -1 )

		fgSizer434.Add( self.m_staticText2634, 0, wx.ALL, 5 )

		self.resist_c_security34 = wx.TextCtrl( self.resist_council_44, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer434.Add( self.resist_c_security34, 0, wx.ALL, 5 )

		self.m_staticText2734 = wx.StaticText( self.resist_council_44, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2734.Wrap( -1 )

		fgSizer434.Add( self.m_staticText2734, 0, wx.ALL, 5 )

		self.resist_c_loyalty34 = wx.TextCtrl( self.resist_council_44, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer434.Add( self.resist_c_loyalty34, 0, wx.ALL, 5 )


		self.resist_council_44.SetSizer( fgSizer434 )
		self.resist_council_44.Layout()
		fgSizer434.Fit( self.resist_council_44 )
		self.resist_sub_tabs4.AddPage( self.resist_council_44, u"Councilor 4", False )
		self.resist_council_54 = wx.Panel( self.resist_sub_tabs4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer444 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer444.SetFlexibleDirection( wx.BOTH )
		fgSizer444.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname44 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname44.Wrap( -1 )

		fgSizer444.Add( self.resist_c_fname44, 0, wx.ALL, 5 )

		self.resist_c_lname44 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname44.Wrap( -1 )

		fgSizer444.Add( self.resist_c_lname44, 0, wx.ALL, 5 )

		self.m_staticText8444 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8444.Wrap( -1 )

		fgSizer444.Add( self.m_staticText8444, 0, wx.ALL, 5 )

		resist_c_class44Choices = []
		self.resist_c_class44 = wx.Choice( self.resist_council_54, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class44Choices, 0 )
		self.resist_c_class44.SetSelection( 0 )
		fgSizer444.Add( self.resist_c_class44, 0, wx.ALL, 5 )

		self.m_staticText2044 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2044.Wrap( -1 )

		fgSizer444.Add( self.m_staticText2044, 0, wx.ALL, 5 )

		self.resist_c_persuasion44 = wx.TextCtrl( self.resist_council_54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer444.Add( self.resist_c_persuasion44, 0, wx.ALL, 5 )

		self.m_staticText2144 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2144.Wrap( -1 )

		fgSizer444.Add( self.m_staticText2144, 0, wx.ALL, 5 )

		self.resist_c_investigation44 = wx.TextCtrl( self.resist_council_54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer444.Add( self.resist_c_investigation44, 0, wx.ALL, 5 )

		self.m_staticText2244 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2244.Wrap( -1 )

		fgSizer444.Add( self.m_staticText2244, 0, wx.ALL, 5 )

		self.resist_c_espionage44 = wx.TextCtrl( self.resist_council_54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer444.Add( self.resist_c_espionage44, 0, wx.ALL, 5 )

		self.m_staticText2344 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2344.Wrap( -1 )

		fgSizer444.Add( self.m_staticText2344, 0, wx.ALL, 5 )

		self.resist_c_command44 = wx.TextCtrl( self.resist_council_54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer444.Add( self.resist_c_command44, 0, wx.ALL, 5 )

		self.m_staticText2444 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2444.Wrap( -1 )

		fgSizer444.Add( self.m_staticText2444, 0, wx.ALL, 5 )

		self.resist_c_administration44 = wx.TextCtrl( self.resist_council_54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer444.Add( self.resist_c_administration44, 0, wx.ALL, 5 )

		self.m_staticText2544 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2544.Wrap( -1 )

		fgSizer444.Add( self.m_staticText2544, 0, wx.ALL, 5 )

		self.resist_c_science44 = wx.TextCtrl( self.resist_council_54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer444.Add( self.resist_c_science44, 0, wx.ALL, 5 )

		self.m_staticText2644 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2644.Wrap( -1 )

		fgSizer444.Add( self.m_staticText2644, 0, wx.ALL, 5 )

		self.resist_c_security44 = wx.TextCtrl( self.resist_council_54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer444.Add( self.resist_c_security44, 0, wx.ALL, 5 )

		self.m_staticText2744 = wx.StaticText( self.resist_council_54, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2744.Wrap( -1 )

		fgSizer444.Add( self.m_staticText2744, 0, wx.ALL, 5 )

		self.resist_c_loyalty44 = wx.TextCtrl( self.resist_council_54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer444.Add( self.resist_c_loyalty44, 0, wx.ALL, 5 )


		self.resist_council_54.SetSizer( fgSizer444 )
		self.resist_council_54.Layout()
		fgSizer444.Fit( self.resist_council_54 )
		self.resist_sub_tabs4.AddPage( self.resist_council_54, u"Councilor 5", False )
		self.resist_council_64 = wx.Panel( self.resist_sub_tabs4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer454 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer454.SetFlexibleDirection( wx.BOTH )
		fgSizer454.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname54 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname54.Wrap( -1 )

		fgSizer454.Add( self.resist_c_fname54, 0, wx.ALL, 5 )

		self.resist_c_lname54 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname54.Wrap( -1 )

		fgSizer454.Add( self.resist_c_lname54, 0, wx.ALL, 5 )

		self.m_staticText8454 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8454.Wrap( -1 )

		fgSizer454.Add( self.m_staticText8454, 0, wx.ALL, 5 )

		resist_c_class54Choices = []
		self.resist_c_class54 = wx.Choice( self.resist_council_64, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class54Choices, 0 )
		self.resist_c_class54.SetSelection( 0 )
		fgSizer454.Add( self.resist_c_class54, 0, wx.ALL, 5 )

		self.m_staticText2054 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2054.Wrap( -1 )

		fgSizer454.Add( self.m_staticText2054, 0, wx.ALL, 5 )

		self.resist_c_persuasion54 = wx.TextCtrl( self.resist_council_64, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer454.Add( self.resist_c_persuasion54, 0, wx.ALL, 5 )

		self.m_staticText2154 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2154.Wrap( -1 )

		fgSizer454.Add( self.m_staticText2154, 0, wx.ALL, 5 )

		self.resist_c_investigation54 = wx.TextCtrl( self.resist_council_64, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer454.Add( self.resist_c_investigation54, 0, wx.ALL, 5 )

		self.m_staticText2254 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2254.Wrap( -1 )

		fgSizer454.Add( self.m_staticText2254, 0, wx.ALL, 5 )

		self.resist_c_espionage54 = wx.TextCtrl( self.resist_council_64, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer454.Add( self.resist_c_espionage54, 0, wx.ALL, 5 )

		self.m_staticText2354 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2354.Wrap( -1 )

		fgSizer454.Add( self.m_staticText2354, 0, wx.ALL, 5 )

		self.resist_c_command54 = wx.TextCtrl( self.resist_council_64, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer454.Add( self.resist_c_command54, 0, wx.ALL, 5 )

		self.m_staticText2454 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2454.Wrap( -1 )

		fgSizer454.Add( self.m_staticText2454, 0, wx.ALL, 5 )

		self.resist_c_administration54 = wx.TextCtrl( self.resist_council_64, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer454.Add( self.resist_c_administration54, 0, wx.ALL, 5 )

		self.m_staticText2554 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2554.Wrap( -1 )

		fgSizer454.Add( self.m_staticText2554, 0, wx.ALL, 5 )

		self.resist_c_science54 = wx.TextCtrl( self.resist_council_64, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer454.Add( self.resist_c_science54, 0, wx.ALL, 5 )

		self.m_staticText2654 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2654.Wrap( -1 )

		fgSizer454.Add( self.m_staticText2654, 0, wx.ALL, 5 )

		self.resist_c_security54 = wx.TextCtrl( self.resist_council_64, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer454.Add( self.resist_c_security54, 0, wx.ALL, 5 )

		self.m_staticText2754 = wx.StaticText( self.resist_council_64, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2754.Wrap( -1 )

		fgSizer454.Add( self.m_staticText2754, 0, wx.ALL, 5 )

		self.resist_c_loyalty54 = wx.TextCtrl( self.resist_council_64, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer454.Add( self.resist_c_loyalty54, 0, wx.ALL, 5 )


		self.resist_council_64.SetSizer( fgSizer454 )
		self.resist_council_64.Layout()
		fgSizer454.Fit( self.resist_council_64 )
		self.resist_sub_tabs4.AddPage( self.resist_council_64, u"Councilor 6", False )

		bSizer34.Add( self.resist_sub_tabs4, 0, wx.EXPAND |wx.ALL, 5 )


		self.protectorate_panel.SetSizer( bSizer34 )
		self.protectorate_panel.Layout()
		bSizer34.Fit( self.protectorate_panel )
		self.app_tabs.AddPage( self.protectorate_panel, u"The Protectorate", False )
		self.academy_panel = wx.Panel( self.app_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		gSizer1221 = wx.GridSizer( 0, 3, 0, 0 )

		self.player_flag5 = wx.CheckBox( self.academy_panel, wx.ID_ANY, u"Player Faction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1221.Add( self.player_flag5, 0, wx.ALL, 5 )

		self.m_staticText5811221 = wx.StaticText( self.academy_panel, wx.ID_ANY, u"Alien Hate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5811221.Wrap( -1 )

		gSizer1221.Add( self.m_staticText5811221, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_spinCtrl25 = wx.SpinCtrl( self.academy_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer1221.Add( self.m_spinCtrl25, 0, wx.ALL, 5 )


		bSizer35.Add( gSizer1221, 1, wx.EXPAND, 5 )

		self.resist_sub_tabs5 = wx.Notebook( self.academy_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_resource_panel5 = wx.Panel( self.resist_sub_tabs5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer25 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText220 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Money", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText220.Wrap( -1 )

		fgSizer25.Add( self.m_staticText220, 0, wx.ALL, 5 )

		self.resist_money5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_money5, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Influence", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		fgSizer25.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.resist_influence5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_influence5, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Ops", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		fgSizer25.Add( self.m_staticText45, 0, wx.ALL, 5 )

		self.resist_ops5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_ops5, 0, wx.ALL, 5 )

		self.m_staticText55 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Boost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		fgSizer25.Add( self.m_staticText55, 0, wx.ALL, 5 )

		self.resist_boost5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_boost5, 0, wx.ALL, 5 )

		self.m_staticText65 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Water", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		fgSizer25.Add( self.m_staticText65, 0, wx.ALL, 5 )

		self.resist_water5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_water5, 0, wx.ALL, 5 )

		self.m_staticText75 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Volatiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		fgSizer25.Add( self.m_staticText75, 0, wx.ALL, 5 )

		self.resist_volatiles5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_volatiles5, 0, wx.ALL, 5 )

		self.m_staticText86 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Base Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )

		fgSizer25.Add( self.m_staticText86, 0, wx.ALL, 5 )

		self.resist_basemetals5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_basemetals5, 0, wx.ALL, 5 )

		self.m_staticText95 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Noble Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )

		fgSizer25.Add( self.m_staticText95, 0, wx.ALL, 5 )

		self.resist_noblemetals5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_noblemetals5, 0, wx.ALL, 5 )

		self.m_staticText105 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Fissiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText105.Wrap( -1 )

		fgSizer25.Add( self.m_staticText105, 0, wx.ALL, 5 )

		self.resist_fissiles5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_fissiles5, 0, wx.ALL, 5 )

		self.m_staticText115 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Exotics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText115.Wrap( -1 )

		fgSizer25.Add( self.m_staticText115, 0, wx.ALL, 5 )

		self.resist_exotics5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_exotics5, 0, wx.ALL, 5 )

		self.m_staticText125 = wx.StaticText( self.resist_resource_panel5, wx.ID_ANY, u"Antimatter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText125.Wrap( -1 )

		fgSizer25.Add( self.m_staticText125, 0, wx.ALL, 5 )

		self.resist_antimatter5 = wx.TextCtrl( self.resist_resource_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.resist_antimatter5, 0, wx.ALL, 5 )


		self.resist_resource_panel5.SetSizer( fgSizer25 )
		self.resist_resource_panel5.Layout()
		fgSizer25.Fit( self.resist_resource_panel5 )
		self.resist_sub_tabs5.AddPage( self.resist_resource_panel5, u"Resources", True )
		self.resist_projects5 = wx.Panel( self.resist_sub_tabs5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer35 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText155 = wx.StaticText( self.resist_projects5, wx.ID_ANY, u"Active Project", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText155.Wrap( -1 )

		fgSizer35.Add( self.m_staticText155, 0, wx.ALL, 5 )

		self.m_staticText175 = wx.StaticText( self.resist_projects5, wx.ID_ANY, u"Current Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText175.Wrap( -1 )

		fgSizer35.Add( self.m_staticText175, 0, wx.ALL, 5 )

		self.resist_project15 = wx.StaticText( self.resist_projects5, wx.ID_ANY, u"Project 1 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project15.Wrap( -1 )

		fgSizer35.Add( self.resist_project15, 0, wx.ALL, 5 )

		self.resist_project1_progress5 = wx.TextCtrl( self.resist_projects5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.resist_project1_progress5, 0, wx.ALL, 5 )

		self.resist_project25 = wx.StaticText( self.resist_projects5, wx.ID_ANY, u"Project 2 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project25.Wrap( -1 )

		fgSizer35.Add( self.resist_project25, 0, wx.ALL, 5 )

		self.resist_project2_progress5 = wx.TextCtrl( self.resist_projects5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.resist_project2_progress5, 0, wx.ALL, 5 )

		self.resist_project35 = wx.StaticText( self.resist_projects5, wx.ID_ANY, u"Project 3 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project35.Wrap( -1 )

		fgSizer35.Add( self.resist_project35, 0, wx.ALL, 5 )

		self.resist_project3_progress5 = wx.TextCtrl( self.resist_projects5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.resist_project3_progress5, 0, wx.ALL, 5 )


		self.resist_projects5.SetSizer( fgSizer35 )
		self.resist_projects5.Layout()
		fgSizer35.Fit( self.resist_projects5 )
		self.resist_sub_tabs5.AddPage( self.resist_projects5, u"Project Research", False )
		self.resist_council_15 = wx.Panel( self.resist_sub_tabs5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer410 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer410.SetFlexibleDirection( wx.BOTH )
		fgSizer410.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname10 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname10.Wrap( -1 )

		fgSizer410.Add( self.resist_c_fname10, 0, wx.ALL, 5 )

		self.resist_c_lname10 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname10.Wrap( -1 )

		fgSizer410.Add( self.resist_c_lname10, 0, wx.ALL, 5 )

		self.m_staticText8410 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8410.Wrap( -1 )

		fgSizer410.Add( self.m_staticText8410, 0, wx.ALL, 5 )

		resist_c_class10Choices = []
		self.resist_c_class10 = wx.Choice( self.resist_council_15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class10Choices, 0 )
		self.resist_c_class10.SetSelection( 0 )
		fgSizer410.Add( self.resist_c_class10, 0, wx.ALL, 5 )

		self.m_staticText2010 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2010.Wrap( -1 )

		fgSizer410.Add( self.m_staticText2010, 0, wx.ALL, 5 )

		self.resist_c_persuasion10 = wx.TextCtrl( self.resist_council_15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer410.Add( self.resist_c_persuasion10, 0, wx.ALL, 5 )

		self.m_staticText2115 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2115.Wrap( -1 )

		fgSizer410.Add( self.m_staticText2115, 0, wx.ALL, 5 )

		self.resist_c_investigation10 = wx.TextCtrl( self.resist_council_15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer410.Add( self.resist_c_investigation10, 0, wx.ALL, 5 )

		self.m_staticText2210 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2210.Wrap( -1 )

		fgSizer410.Add( self.m_staticText2210, 0, wx.ALL, 5 )

		self.resist_c_espionage10 = wx.TextCtrl( self.resist_council_15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer410.Add( self.resist_c_espionage10, 0, wx.ALL, 5 )

		self.m_staticText2310 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2310.Wrap( -1 )

		fgSizer410.Add( self.m_staticText2310, 0, wx.ALL, 5 )

		self.resist_c_command10 = wx.TextCtrl( self.resist_council_15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer410.Add( self.resist_c_command10, 0, wx.ALL, 5 )

		self.m_staticText2410 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2410.Wrap( -1 )

		fgSizer410.Add( self.m_staticText2410, 0, wx.ALL, 5 )

		self.resist_c_administration10 = wx.TextCtrl( self.resist_council_15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer410.Add( self.resist_c_administration10, 0, wx.ALL, 5 )

		self.m_staticText2510 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2510.Wrap( -1 )

		fgSizer410.Add( self.m_staticText2510, 0, wx.ALL, 5 )

		self.resist_c_science10 = wx.TextCtrl( self.resist_council_15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer410.Add( self.resist_c_science10, 0, wx.ALL, 5 )

		self.m_staticText2610 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2610.Wrap( -1 )

		fgSizer410.Add( self.m_staticText2610, 0, wx.ALL, 5 )

		self.resist_c_security10 = wx.TextCtrl( self.resist_council_15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer410.Add( self.resist_c_security10, 0, wx.ALL, 5 )

		self.m_staticText2710 = wx.StaticText( self.resist_council_15, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2710.Wrap( -1 )

		fgSizer410.Add( self.m_staticText2710, 0, wx.ALL, 5 )

		self.resist_c_loyalty10 = wx.TextCtrl( self.resist_council_15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer410.Add( self.resist_c_loyalty10, 0, wx.ALL, 5 )


		self.resist_council_15.SetSizer( fgSizer410 )
		self.resist_council_15.Layout()
		fgSizer410.Fit( self.resist_council_15 )
		self.resist_sub_tabs5.AddPage( self.resist_council_15, u"Councilor 1", False )
		self.resist_council_25 = wx.Panel( self.resist_sub_tabs5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer415 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer415.SetFlexibleDirection( wx.BOTH )
		fgSizer415.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname15 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname15.Wrap( -1 )

		fgSizer415.Add( self.resist_c_fname15, 0, wx.ALL, 5 )

		self.resist_c_lname15 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname15.Wrap( -1 )

		fgSizer415.Add( self.resist_c_lname15, 0, wx.ALL, 5 )

		self.m_staticText8415 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8415.Wrap( -1 )

		fgSizer415.Add( self.m_staticText8415, 0, wx.ALL, 5 )

		resist_c_class15Choices = []
		self.resist_c_class15 = wx.Choice( self.resist_council_25, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class15Choices, 0 )
		self.resist_c_class15.SetSelection( 0 )
		fgSizer415.Add( self.resist_c_class15, 0, wx.ALL, 5 )

		self.m_staticText2015 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2015.Wrap( -1 )

		fgSizer415.Add( self.m_staticText2015, 0, wx.ALL, 5 )

		self.resist_c_persuasion15 = wx.TextCtrl( self.resist_council_25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer415.Add( self.resist_c_persuasion15, 0, wx.ALL, 5 )

		self.m_staticText2116 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2116.Wrap( -1 )

		fgSizer415.Add( self.m_staticText2116, 0, wx.ALL, 5 )

		self.resist_c_investigation15 = wx.TextCtrl( self.resist_council_25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer415.Add( self.resist_c_investigation15, 0, wx.ALL, 5 )

		self.m_staticText2215 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2215.Wrap( -1 )

		fgSizer415.Add( self.m_staticText2215, 0, wx.ALL, 5 )

		self.resist_c_espionage15 = wx.TextCtrl( self.resist_council_25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer415.Add( self.resist_c_espionage15, 0, wx.ALL, 5 )

		self.m_staticText2315 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2315.Wrap( -1 )

		fgSizer415.Add( self.m_staticText2315, 0, wx.ALL, 5 )

		self.resist_c_command15 = wx.TextCtrl( self.resist_council_25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer415.Add( self.resist_c_command15, 0, wx.ALL, 5 )

		self.m_staticText2415 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2415.Wrap( -1 )

		fgSizer415.Add( self.m_staticText2415, 0, wx.ALL, 5 )

		self.resist_c_administration15 = wx.TextCtrl( self.resist_council_25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer415.Add( self.resist_c_administration15, 0, wx.ALL, 5 )

		self.m_staticText2515 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2515.Wrap( -1 )

		fgSizer415.Add( self.m_staticText2515, 0, wx.ALL, 5 )

		self.resist_c_science15 = wx.TextCtrl( self.resist_council_25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer415.Add( self.resist_c_science15, 0, wx.ALL, 5 )

		self.m_staticText2615 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2615.Wrap( -1 )

		fgSizer415.Add( self.m_staticText2615, 0, wx.ALL, 5 )

		self.resist_c_security15 = wx.TextCtrl( self.resist_council_25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer415.Add( self.resist_c_security15, 0, wx.ALL, 5 )

		self.m_staticText2715 = wx.StaticText( self.resist_council_25, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2715.Wrap( -1 )

		fgSizer415.Add( self.m_staticText2715, 0, wx.ALL, 5 )

		self.resist_c_loyalty15 = wx.TextCtrl( self.resist_council_25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer415.Add( self.resist_c_loyalty15, 0, wx.ALL, 5 )


		self.resist_council_25.SetSizer( fgSizer415 )
		self.resist_council_25.Layout()
		fgSizer415.Fit( self.resist_council_25 )
		self.resist_sub_tabs5.AddPage( self.resist_council_25, u"Councilor 2", False )
		self.resist_council_35 = wx.Panel( self.resist_sub_tabs5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer425 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer425.SetFlexibleDirection( wx.BOTH )
		fgSizer425.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname25 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname25.Wrap( -1 )

		fgSizer425.Add( self.resist_c_fname25, 0, wx.ALL, 5 )

		self.resist_c_lname25 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname25.Wrap( -1 )

		fgSizer425.Add( self.resist_c_lname25, 0, wx.ALL, 5 )

		self.m_staticText8425 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8425.Wrap( -1 )

		fgSizer425.Add( self.m_staticText8425, 0, wx.ALL, 5 )

		resist_c_class25Choices = []
		self.resist_c_class25 = wx.Choice( self.resist_council_35, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class25Choices, 0 )
		self.resist_c_class25.SetSelection( 0 )
		fgSizer425.Add( self.resist_c_class25, 0, wx.ALL, 5 )

		self.m_staticText2025 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2025.Wrap( -1 )

		fgSizer425.Add( self.m_staticText2025, 0, wx.ALL, 5 )

		self.resist_c_persuasion25 = wx.TextCtrl( self.resist_council_35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer425.Add( self.resist_c_persuasion25, 0, wx.ALL, 5 )

		self.m_staticText2125 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2125.Wrap( -1 )

		fgSizer425.Add( self.m_staticText2125, 0, wx.ALL, 5 )

		self.resist_c_investigation25 = wx.TextCtrl( self.resist_council_35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer425.Add( self.resist_c_investigation25, 0, wx.ALL, 5 )

		self.m_staticText2225 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2225.Wrap( -1 )

		fgSizer425.Add( self.m_staticText2225, 0, wx.ALL, 5 )

		self.resist_c_espionage25 = wx.TextCtrl( self.resist_council_35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer425.Add( self.resist_c_espionage25, 0, wx.ALL, 5 )

		self.m_staticText2325 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2325.Wrap( -1 )

		fgSizer425.Add( self.m_staticText2325, 0, wx.ALL, 5 )

		self.resist_c_command25 = wx.TextCtrl( self.resist_council_35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer425.Add( self.resist_c_command25, 0, wx.ALL, 5 )

		self.m_staticText2425 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2425.Wrap( -1 )

		fgSizer425.Add( self.m_staticText2425, 0, wx.ALL, 5 )

		self.resist_c_administration25 = wx.TextCtrl( self.resist_council_35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer425.Add( self.resist_c_administration25, 0, wx.ALL, 5 )

		self.m_staticText2525 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2525.Wrap( -1 )

		fgSizer425.Add( self.m_staticText2525, 0, wx.ALL, 5 )

		self.resist_c_science25 = wx.TextCtrl( self.resist_council_35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer425.Add( self.resist_c_science25, 0, wx.ALL, 5 )

		self.m_staticText2625 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2625.Wrap( -1 )

		fgSizer425.Add( self.m_staticText2625, 0, wx.ALL, 5 )

		self.resist_c_security25 = wx.TextCtrl( self.resist_council_35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer425.Add( self.resist_c_security25, 0, wx.ALL, 5 )

		self.m_staticText2725 = wx.StaticText( self.resist_council_35, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2725.Wrap( -1 )

		fgSizer425.Add( self.m_staticText2725, 0, wx.ALL, 5 )

		self.resist_c_loyalty25 = wx.TextCtrl( self.resist_council_35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer425.Add( self.resist_c_loyalty25, 0, wx.ALL, 5 )


		self.resist_council_35.SetSizer( fgSizer425 )
		self.resist_council_35.Layout()
		fgSizer425.Fit( self.resist_council_35 )
		self.resist_sub_tabs5.AddPage( self.resist_council_35, u"Councilor 3", False )
		self.resist_council_45 = wx.Panel( self.resist_sub_tabs5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer435 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer435.SetFlexibleDirection( wx.BOTH )
		fgSizer435.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname35 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname35.Wrap( -1 )

		fgSizer435.Add( self.resist_c_fname35, 0, wx.ALL, 5 )

		self.resist_c_lname35 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname35.Wrap( -1 )

		fgSizer435.Add( self.resist_c_lname35, 0, wx.ALL, 5 )

		self.m_staticText8435 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8435.Wrap( -1 )

		fgSizer435.Add( self.m_staticText8435, 0, wx.ALL, 5 )

		resist_c_class35Choices = []
		self.resist_c_class35 = wx.Choice( self.resist_council_45, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class35Choices, 0 )
		self.resist_c_class35.SetSelection( 0 )
		fgSizer435.Add( self.resist_c_class35, 0, wx.ALL, 5 )

		self.m_staticText2035 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2035.Wrap( -1 )

		fgSizer435.Add( self.m_staticText2035, 0, wx.ALL, 5 )

		self.resist_c_persuasion35 = wx.TextCtrl( self.resist_council_45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer435.Add( self.resist_c_persuasion35, 0, wx.ALL, 5 )

		self.m_staticText2135 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2135.Wrap( -1 )

		fgSizer435.Add( self.m_staticText2135, 0, wx.ALL, 5 )

		self.resist_c_investigation35 = wx.TextCtrl( self.resist_council_45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer435.Add( self.resist_c_investigation35, 0, wx.ALL, 5 )

		self.m_staticText2235 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2235.Wrap( -1 )

		fgSizer435.Add( self.m_staticText2235, 0, wx.ALL, 5 )

		self.resist_c_espionage35 = wx.TextCtrl( self.resist_council_45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer435.Add( self.resist_c_espionage35, 0, wx.ALL, 5 )

		self.m_staticText2335 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2335.Wrap( -1 )

		fgSizer435.Add( self.m_staticText2335, 0, wx.ALL, 5 )

		self.resist_c_command35 = wx.TextCtrl( self.resist_council_45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer435.Add( self.resist_c_command35, 0, wx.ALL, 5 )

		self.m_staticText2435 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2435.Wrap( -1 )

		fgSizer435.Add( self.m_staticText2435, 0, wx.ALL, 5 )

		self.resist_c_administration35 = wx.TextCtrl( self.resist_council_45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer435.Add( self.resist_c_administration35, 0, wx.ALL, 5 )

		self.m_staticText2535 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2535.Wrap( -1 )

		fgSizer435.Add( self.m_staticText2535, 0, wx.ALL, 5 )

		self.resist_c_science35 = wx.TextCtrl( self.resist_council_45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer435.Add( self.resist_c_science35, 0, wx.ALL, 5 )

		self.m_staticText2635 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2635.Wrap( -1 )

		fgSizer435.Add( self.m_staticText2635, 0, wx.ALL, 5 )

		self.resist_c_security35 = wx.TextCtrl( self.resist_council_45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer435.Add( self.resist_c_security35, 0, wx.ALL, 5 )

		self.m_staticText2735 = wx.StaticText( self.resist_council_45, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2735.Wrap( -1 )

		fgSizer435.Add( self.m_staticText2735, 0, wx.ALL, 5 )

		self.resist_c_loyalty35 = wx.TextCtrl( self.resist_council_45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer435.Add( self.resist_c_loyalty35, 0, wx.ALL, 5 )


		self.resist_council_45.SetSizer( fgSizer435 )
		self.resist_council_45.Layout()
		fgSizer435.Fit( self.resist_council_45 )
		self.resist_sub_tabs5.AddPage( self.resist_council_45, u"Councilor 4", False )
		self.resist_council_55 = wx.Panel( self.resist_sub_tabs5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer445 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer445.SetFlexibleDirection( wx.BOTH )
		fgSizer445.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname45 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname45.Wrap( -1 )

		fgSizer445.Add( self.resist_c_fname45, 0, wx.ALL, 5 )

		self.resist_c_lname45 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname45.Wrap( -1 )

		fgSizer445.Add( self.resist_c_lname45, 0, wx.ALL, 5 )

		self.m_staticText8445 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8445.Wrap( -1 )

		fgSizer445.Add( self.m_staticText8445, 0, wx.ALL, 5 )

		resist_c_class45Choices = []
		self.resist_c_class45 = wx.Choice( self.resist_council_55, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class45Choices, 0 )
		self.resist_c_class45.SetSelection( 0 )
		fgSizer445.Add( self.resist_c_class45, 0, wx.ALL, 5 )

		self.m_staticText2045 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2045.Wrap( -1 )

		fgSizer445.Add( self.m_staticText2045, 0, wx.ALL, 5 )

		self.resist_c_persuasion45 = wx.TextCtrl( self.resist_council_55, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer445.Add( self.resist_c_persuasion45, 0, wx.ALL, 5 )

		self.m_staticText2145 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2145.Wrap( -1 )

		fgSizer445.Add( self.m_staticText2145, 0, wx.ALL, 5 )

		self.resist_c_investigation45 = wx.TextCtrl( self.resist_council_55, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer445.Add( self.resist_c_investigation45, 0, wx.ALL, 5 )

		self.m_staticText2245 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2245.Wrap( -1 )

		fgSizer445.Add( self.m_staticText2245, 0, wx.ALL, 5 )

		self.resist_c_espionage45 = wx.TextCtrl( self.resist_council_55, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer445.Add( self.resist_c_espionage45, 0, wx.ALL, 5 )

		self.m_staticText2345 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2345.Wrap( -1 )

		fgSizer445.Add( self.m_staticText2345, 0, wx.ALL, 5 )

		self.resist_c_command45 = wx.TextCtrl( self.resist_council_55, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer445.Add( self.resist_c_command45, 0, wx.ALL, 5 )

		self.m_staticText2445 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2445.Wrap( -1 )

		fgSizer445.Add( self.m_staticText2445, 0, wx.ALL, 5 )

		self.resist_c_administration45 = wx.TextCtrl( self.resist_council_55, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer445.Add( self.resist_c_administration45, 0, wx.ALL, 5 )

		self.m_staticText2545 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2545.Wrap( -1 )

		fgSizer445.Add( self.m_staticText2545, 0, wx.ALL, 5 )

		self.resist_c_science45 = wx.TextCtrl( self.resist_council_55, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer445.Add( self.resist_c_science45, 0, wx.ALL, 5 )

		self.m_staticText2645 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2645.Wrap( -1 )

		fgSizer445.Add( self.m_staticText2645, 0, wx.ALL, 5 )

		self.resist_c_security45 = wx.TextCtrl( self.resist_council_55, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer445.Add( self.resist_c_security45, 0, wx.ALL, 5 )

		self.m_staticText2745 = wx.StaticText( self.resist_council_55, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2745.Wrap( -1 )

		fgSizer445.Add( self.m_staticText2745, 0, wx.ALL, 5 )

		self.resist_c_loyalty45 = wx.TextCtrl( self.resist_council_55, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer445.Add( self.resist_c_loyalty45, 0, wx.ALL, 5 )


		self.resist_council_55.SetSizer( fgSizer445 )
		self.resist_council_55.Layout()
		fgSizer445.Fit( self.resist_council_55 )
		self.resist_sub_tabs5.AddPage( self.resist_council_55, u"Councilor 5", False )
		self.resist_council_65 = wx.Panel( self.resist_sub_tabs5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer455 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer455.SetFlexibleDirection( wx.BOTH )
		fgSizer455.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname55 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname55.Wrap( -1 )

		fgSizer455.Add( self.resist_c_fname55, 0, wx.ALL, 5 )

		self.resist_c_lname55 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname55.Wrap( -1 )

		fgSizer455.Add( self.resist_c_lname55, 0, wx.ALL, 5 )

		self.m_staticText8455 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8455.Wrap( -1 )

		fgSizer455.Add( self.m_staticText8455, 0, wx.ALL, 5 )

		resist_c_class55Choices = []
		self.resist_c_class55 = wx.Choice( self.resist_council_65, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class55Choices, 0 )
		self.resist_c_class55.SetSelection( 0 )
		fgSizer455.Add( self.resist_c_class55, 0, wx.ALL, 5 )

		self.m_staticText2055 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2055.Wrap( -1 )

		fgSizer455.Add( self.m_staticText2055, 0, wx.ALL, 5 )

		self.resist_c_persuasion55 = wx.TextCtrl( self.resist_council_65, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer455.Add( self.resist_c_persuasion55, 0, wx.ALL, 5 )

		self.m_staticText2155 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2155.Wrap( -1 )

		fgSizer455.Add( self.m_staticText2155, 0, wx.ALL, 5 )

		self.resist_c_investigation55 = wx.TextCtrl( self.resist_council_65, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer455.Add( self.resist_c_investigation55, 0, wx.ALL, 5 )

		self.m_staticText2255 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2255.Wrap( -1 )

		fgSizer455.Add( self.m_staticText2255, 0, wx.ALL, 5 )

		self.resist_c_espionage55 = wx.TextCtrl( self.resist_council_65, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer455.Add( self.resist_c_espionage55, 0, wx.ALL, 5 )

		self.m_staticText2355 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2355.Wrap( -1 )

		fgSizer455.Add( self.m_staticText2355, 0, wx.ALL, 5 )

		self.resist_c_command55 = wx.TextCtrl( self.resist_council_65, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer455.Add( self.resist_c_command55, 0, wx.ALL, 5 )

		self.m_staticText2455 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2455.Wrap( -1 )

		fgSizer455.Add( self.m_staticText2455, 0, wx.ALL, 5 )

		self.resist_c_administration55 = wx.TextCtrl( self.resist_council_65, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer455.Add( self.resist_c_administration55, 0, wx.ALL, 5 )

		self.m_staticText2555 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2555.Wrap( -1 )

		fgSizer455.Add( self.m_staticText2555, 0, wx.ALL, 5 )

		self.resist_c_science55 = wx.TextCtrl( self.resist_council_65, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer455.Add( self.resist_c_science55, 0, wx.ALL, 5 )

		self.m_staticText2655 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2655.Wrap( -1 )

		fgSizer455.Add( self.m_staticText2655, 0, wx.ALL, 5 )

		self.resist_c_security55 = wx.TextCtrl( self.resist_council_65, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer455.Add( self.resist_c_security55, 0, wx.ALL, 5 )

		self.m_staticText2755 = wx.StaticText( self.resist_council_65, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2755.Wrap( -1 )

		fgSizer455.Add( self.m_staticText2755, 0, wx.ALL, 5 )

		self.resist_c_loyalty55 = wx.TextCtrl( self.resist_council_65, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer455.Add( self.resist_c_loyalty55, 0, wx.ALL, 5 )


		self.resist_council_65.SetSizer( fgSizer455 )
		self.resist_council_65.Layout()
		fgSizer455.Fit( self.resist_council_65 )
		self.resist_sub_tabs5.AddPage( self.resist_council_65, u"Councilor 6", False )

		bSizer35.Add( self.resist_sub_tabs5, 0, wx.EXPAND |wx.ALL, 5 )


		self.academy_panel.SetSizer( bSizer35 )
		self.academy_panel.Layout()
		bSizer35.Fit( self.academy_panel )
		self.app_tabs.AddPage( self.academy_panel, u"The Academy", False )
		self.exodus_panel = wx.Panel( self.app_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		gSizer1222 = wx.GridSizer( 0, 3, 0, 0 )

		self.player_flag6 = wx.CheckBox( self.exodus_panel, wx.ID_ANY, u"Player Faction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1222.Add( self.player_flag6, 0, wx.ALL, 5 )

		self.m_staticText5811222 = wx.StaticText( self.exodus_panel, wx.ID_ANY, u"Alien Hate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5811222.Wrap( -1 )

		gSizer1222.Add( self.m_staticText5811222, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_spinCtrl26 = wx.SpinCtrl( self.exodus_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		gSizer1222.Add( self.m_spinCtrl26, 0, wx.ALL, 5 )


		bSizer36.Add( gSizer1222, 1, wx.EXPAND, 5 )

		self.resist_sub_tabs6 = wx.Notebook( self.exodus_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_resource_panel6 = wx.Panel( self.resist_sub_tabs6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer26 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer26.SetFlexibleDirection( wx.BOTH )
		fgSizer26.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText230 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Money", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText230.Wrap( -1 )

		fgSizer26.Add( self.m_staticText230, 0, wx.ALL, 5 )

		self.resist_money6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_money6, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Influence", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		fgSizer26.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.resist_influence6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_influence6, 0, wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Ops", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		fgSizer26.Add( self.m_staticText46, 0, wx.ALL, 5 )

		self.resist_ops6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_ops6, 0, wx.ALL, 5 )

		self.m_staticText56 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Boost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		fgSizer26.Add( self.m_staticText56, 0, wx.ALL, 5 )

		self.resist_boost6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_boost6, 0, wx.ALL, 5 )

		self.m_staticText66 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Water", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )

		fgSizer26.Add( self.m_staticText66, 0, wx.ALL, 5 )

		self.resist_water6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_water6, 0, wx.ALL, 5 )

		self.m_staticText76 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Volatiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )

		fgSizer26.Add( self.m_staticText76, 0, wx.ALL, 5 )

		self.resist_volatiles6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_volatiles6, 0, wx.ALL, 5 )

		self.m_staticText87 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Base Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )

		fgSizer26.Add( self.m_staticText87, 0, wx.ALL, 5 )

		self.resist_basemetals6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_basemetals6, 0, wx.ALL, 5 )

		self.m_staticText96 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Noble Metals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText96.Wrap( -1 )

		fgSizer26.Add( self.m_staticText96, 0, wx.ALL, 5 )

		self.resist_noblemetals6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_noblemetals6, 0, wx.ALL, 5 )

		self.m_staticText106 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Fissiles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText106.Wrap( -1 )

		fgSizer26.Add( self.m_staticText106, 0, wx.ALL, 5 )

		self.resist_fissiles6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_fissiles6, 0, wx.ALL, 5 )

		self.m_staticText116 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Exotics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText116.Wrap( -1 )

		fgSizer26.Add( self.m_staticText116, 0, wx.ALL, 5 )

		self.resist_exotics6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_exotics6, 0, wx.ALL, 5 )

		self.m_staticText126 = wx.StaticText( self.resist_resource_panel6, wx.ID_ANY, u"Antimatter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText126.Wrap( -1 )

		fgSizer26.Add( self.m_staticText126, 0, wx.ALL, 5 )

		self.resist_antimatter6 = wx.TextCtrl( self.resist_resource_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.resist_antimatter6, 0, wx.ALL, 5 )


		self.resist_resource_panel6.SetSizer( fgSizer26 )
		self.resist_resource_panel6.Layout()
		fgSizer26.Fit( self.resist_resource_panel6 )
		self.resist_sub_tabs6.AddPage( self.resist_resource_panel6, u"Resources", True )
		self.resist_projects6 = wx.Panel( self.resist_sub_tabs6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer36 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText156 = wx.StaticText( self.resist_projects6, wx.ID_ANY, u"Active Project", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText156.Wrap( -1 )

		fgSizer36.Add( self.m_staticText156, 0, wx.ALL, 5 )

		self.m_staticText176 = wx.StaticText( self.resist_projects6, wx.ID_ANY, u"Current Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText176.Wrap( -1 )

		fgSizer36.Add( self.m_staticText176, 0, wx.ALL, 5 )

		self.resist_project16 = wx.StaticText( self.resist_projects6, wx.ID_ANY, u"Project 1 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project16.Wrap( -1 )

		fgSizer36.Add( self.resist_project16, 0, wx.ALL, 5 )

		self.resist_project1_progress6 = wx.TextCtrl( self.resist_projects6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.resist_project1_progress6, 0, wx.ALL, 5 )

		self.resist_project26 = wx.StaticText( self.resist_projects6, wx.ID_ANY, u"Project 2 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project26.Wrap( -1 )

		fgSizer36.Add( self.resist_project26, 0, wx.ALL, 5 )

		self.resist_project2_progress6 = wx.TextCtrl( self.resist_projects6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.resist_project2_progress6, 0, wx.ALL, 5 )

		self.resist_project36 = wx.StaticText( self.resist_projects6, wx.ID_ANY, u"Project 3 Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_project36.Wrap( -1 )

		fgSizer36.Add( self.resist_project36, 0, wx.ALL, 5 )

		self.resist_project3_progress6 = wx.TextCtrl( self.resist_projects6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.resist_project3_progress6, 0, wx.ALL, 5 )


		self.resist_projects6.SetSizer( fgSizer36 )
		self.resist_projects6.Layout()
		fgSizer36.Fit( self.resist_projects6 )
		self.resist_sub_tabs6.AddPage( self.resist_projects6, u"Project Research", False )
		self.resist_council_16 = wx.Panel( self.resist_sub_tabs6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer416 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer416.SetFlexibleDirection( wx.BOTH )
		fgSizer416.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname16 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname16.Wrap( -1 )

		fgSizer416.Add( self.resist_c_fname16, 0, wx.ALL, 5 )

		self.resist_c_lname16 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname16.Wrap( -1 )

		fgSizer416.Add( self.resist_c_lname16, 0, wx.ALL, 5 )

		self.m_staticText8416 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8416.Wrap( -1 )

		fgSizer416.Add( self.m_staticText8416, 0, wx.ALL, 5 )

		resist_c_class16Choices = []
		self.resist_c_class16 = wx.Choice( self.resist_council_16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class16Choices, 0 )
		self.resist_c_class16.SetSelection( 0 )
		fgSizer416.Add( self.resist_c_class16, 0, wx.ALL, 5 )

		self.m_staticText2016 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2016.Wrap( -1 )

		fgSizer416.Add( self.m_staticText2016, 0, wx.ALL, 5 )

		self.resist_c_persuasion16 = wx.TextCtrl( self.resist_council_16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer416.Add( self.resist_c_persuasion16, 0, wx.ALL, 5 )

		self.m_staticText2117 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2117.Wrap( -1 )

		fgSizer416.Add( self.m_staticText2117, 0, wx.ALL, 5 )

		self.resist_c_investigation16 = wx.TextCtrl( self.resist_council_16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer416.Add( self.resist_c_investigation16, 0, wx.ALL, 5 )

		self.m_staticText2216 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2216.Wrap( -1 )

		fgSizer416.Add( self.m_staticText2216, 0, wx.ALL, 5 )

		self.resist_c_espionage16 = wx.TextCtrl( self.resist_council_16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer416.Add( self.resist_c_espionage16, 0, wx.ALL, 5 )

		self.m_staticText2316 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2316.Wrap( -1 )

		fgSizer416.Add( self.m_staticText2316, 0, wx.ALL, 5 )

		self.resist_c_command16 = wx.TextCtrl( self.resist_council_16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer416.Add( self.resist_c_command16, 0, wx.ALL, 5 )

		self.m_staticText2416 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2416.Wrap( -1 )

		fgSizer416.Add( self.m_staticText2416, 0, wx.ALL, 5 )

		self.resist_c_administration16 = wx.TextCtrl( self.resist_council_16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer416.Add( self.resist_c_administration16, 0, wx.ALL, 5 )

		self.m_staticText2516 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2516.Wrap( -1 )

		fgSizer416.Add( self.m_staticText2516, 0, wx.ALL, 5 )

		self.resist_c_science16 = wx.TextCtrl( self.resist_council_16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer416.Add( self.resist_c_science16, 0, wx.ALL, 5 )

		self.m_staticText2616 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2616.Wrap( -1 )

		fgSizer416.Add( self.m_staticText2616, 0, wx.ALL, 5 )

		self.resist_c_security16 = wx.TextCtrl( self.resist_council_16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer416.Add( self.resist_c_security16, 0, wx.ALL, 5 )

		self.m_staticText2716 = wx.StaticText( self.resist_council_16, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2716.Wrap( -1 )

		fgSizer416.Add( self.m_staticText2716, 0, wx.ALL, 5 )

		self.resist_c_loyalty16 = wx.TextCtrl( self.resist_council_16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer416.Add( self.resist_c_loyalty16, 0, wx.ALL, 5 )


		self.resist_council_16.SetSizer( fgSizer416 )
		self.resist_council_16.Layout()
		fgSizer416.Fit( self.resist_council_16 )
		self.resist_sub_tabs6.AddPage( self.resist_council_16, u"Councilor 1", False )
		self.resist_council_26 = wx.Panel( self.resist_sub_tabs6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer417 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer417.SetFlexibleDirection( wx.BOTH )
		fgSizer417.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname17 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname17.Wrap( -1 )

		fgSizer417.Add( self.resist_c_fname17, 0, wx.ALL, 5 )

		self.resist_c_lname17 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname17.Wrap( -1 )

		fgSizer417.Add( self.resist_c_lname17, 0, wx.ALL, 5 )

		self.m_staticText8417 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8417.Wrap( -1 )

		fgSizer417.Add( self.m_staticText8417, 0, wx.ALL, 5 )

		resist_c_class17Choices = []
		self.resist_c_class17 = wx.Choice( self.resist_council_26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class17Choices, 0 )
		self.resist_c_class17.SetSelection( 0 )
		fgSizer417.Add( self.resist_c_class17, 0, wx.ALL, 5 )

		self.m_staticText2017 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2017.Wrap( -1 )

		fgSizer417.Add( self.m_staticText2017, 0, wx.ALL, 5 )

		self.resist_c_persuasion17 = wx.TextCtrl( self.resist_council_26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer417.Add( self.resist_c_persuasion17, 0, wx.ALL, 5 )

		self.m_staticText2118 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2118.Wrap( -1 )

		fgSizer417.Add( self.m_staticText2118, 0, wx.ALL, 5 )

		self.resist_c_investigation17 = wx.TextCtrl( self.resist_council_26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer417.Add( self.resist_c_investigation17, 0, wx.ALL, 5 )

		self.m_staticText2217 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2217.Wrap( -1 )

		fgSizer417.Add( self.m_staticText2217, 0, wx.ALL, 5 )

		self.resist_c_espionage17 = wx.TextCtrl( self.resist_council_26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer417.Add( self.resist_c_espionage17, 0, wx.ALL, 5 )

		self.m_staticText2317 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2317.Wrap( -1 )

		fgSizer417.Add( self.m_staticText2317, 0, wx.ALL, 5 )

		self.resist_c_command17 = wx.TextCtrl( self.resist_council_26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer417.Add( self.resist_c_command17, 0, wx.ALL, 5 )

		self.m_staticText2417 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2417.Wrap( -1 )

		fgSizer417.Add( self.m_staticText2417, 0, wx.ALL, 5 )

		self.resist_c_administration17 = wx.TextCtrl( self.resist_council_26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer417.Add( self.resist_c_administration17, 0, wx.ALL, 5 )

		self.m_staticText2517 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2517.Wrap( -1 )

		fgSizer417.Add( self.m_staticText2517, 0, wx.ALL, 5 )

		self.resist_c_science17 = wx.TextCtrl( self.resist_council_26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer417.Add( self.resist_c_science17, 0, wx.ALL, 5 )

		self.m_staticText2617 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2617.Wrap( -1 )

		fgSizer417.Add( self.m_staticText2617, 0, wx.ALL, 5 )

		self.resist_c_security17 = wx.TextCtrl( self.resist_council_26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer417.Add( self.resist_c_security17, 0, wx.ALL, 5 )

		self.m_staticText2717 = wx.StaticText( self.resist_council_26, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2717.Wrap( -1 )

		fgSizer417.Add( self.m_staticText2717, 0, wx.ALL, 5 )

		self.resist_c_loyalty17 = wx.TextCtrl( self.resist_council_26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer417.Add( self.resist_c_loyalty17, 0, wx.ALL, 5 )


		self.resist_council_26.SetSizer( fgSizer417 )
		self.resist_council_26.Layout()
		fgSizer417.Fit( self.resist_council_26 )
		self.resist_sub_tabs6.AddPage( self.resist_council_26, u"Councilor 2", False )
		self.resist_council_36 = wx.Panel( self.resist_sub_tabs6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer426 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer426.SetFlexibleDirection( wx.BOTH )
		fgSizer426.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname26 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname26.Wrap( -1 )

		fgSizer426.Add( self.resist_c_fname26, 0, wx.ALL, 5 )

		self.resist_c_lname26 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname26.Wrap( -1 )

		fgSizer426.Add( self.resist_c_lname26, 0, wx.ALL, 5 )

		self.m_staticText8426 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8426.Wrap( -1 )

		fgSizer426.Add( self.m_staticText8426, 0, wx.ALL, 5 )

		resist_c_class26Choices = []
		self.resist_c_class26 = wx.Choice( self.resist_council_36, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class26Choices, 0 )
		self.resist_c_class26.SetSelection( 0 )
		fgSizer426.Add( self.resist_c_class26, 0, wx.ALL, 5 )

		self.m_staticText2026 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2026.Wrap( -1 )

		fgSizer426.Add( self.m_staticText2026, 0, wx.ALL, 5 )

		self.resist_c_persuasion26 = wx.TextCtrl( self.resist_council_36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer426.Add( self.resist_c_persuasion26, 0, wx.ALL, 5 )

		self.m_staticText2126 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2126.Wrap( -1 )

		fgSizer426.Add( self.m_staticText2126, 0, wx.ALL, 5 )

		self.resist_c_investigation26 = wx.TextCtrl( self.resist_council_36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer426.Add( self.resist_c_investigation26, 0, wx.ALL, 5 )

		self.m_staticText2226 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2226.Wrap( -1 )

		fgSizer426.Add( self.m_staticText2226, 0, wx.ALL, 5 )

		self.resist_c_espionage26 = wx.TextCtrl( self.resist_council_36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer426.Add( self.resist_c_espionage26, 0, wx.ALL, 5 )

		self.m_staticText2326 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2326.Wrap( -1 )

		fgSizer426.Add( self.m_staticText2326, 0, wx.ALL, 5 )

		self.resist_c_command26 = wx.TextCtrl( self.resist_council_36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer426.Add( self.resist_c_command26, 0, wx.ALL, 5 )

		self.m_staticText2426 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2426.Wrap( -1 )

		fgSizer426.Add( self.m_staticText2426, 0, wx.ALL, 5 )

		self.resist_c_administration26 = wx.TextCtrl( self.resist_council_36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer426.Add( self.resist_c_administration26, 0, wx.ALL, 5 )

		self.m_staticText2526 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2526.Wrap( -1 )

		fgSizer426.Add( self.m_staticText2526, 0, wx.ALL, 5 )

		self.resist_c_science26 = wx.TextCtrl( self.resist_council_36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer426.Add( self.resist_c_science26, 0, wx.ALL, 5 )

		self.m_staticText2626 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2626.Wrap( -1 )

		fgSizer426.Add( self.m_staticText2626, 0, wx.ALL, 5 )

		self.resist_c_security26 = wx.TextCtrl( self.resist_council_36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer426.Add( self.resist_c_security26, 0, wx.ALL, 5 )

		self.m_staticText2726 = wx.StaticText( self.resist_council_36, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2726.Wrap( -1 )

		fgSizer426.Add( self.m_staticText2726, 0, wx.ALL, 5 )

		self.resist_c_loyalty26 = wx.TextCtrl( self.resist_council_36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer426.Add( self.resist_c_loyalty26, 0, wx.ALL, 5 )


		self.resist_council_36.SetSizer( fgSizer426 )
		self.resist_council_36.Layout()
		fgSizer426.Fit( self.resist_council_36 )
		self.resist_sub_tabs6.AddPage( self.resist_council_36, u"Councilor 3", False )
		self.resist_council_46 = wx.Panel( self.resist_sub_tabs6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer436 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer436.SetFlexibleDirection( wx.BOTH )
		fgSizer436.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname36 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname36.Wrap( -1 )

		fgSizer436.Add( self.resist_c_fname36, 0, wx.ALL, 5 )

		self.resist_c_lname36 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname36.Wrap( -1 )

		fgSizer436.Add( self.resist_c_lname36, 0, wx.ALL, 5 )

		self.m_staticText8436 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8436.Wrap( -1 )

		fgSizer436.Add( self.m_staticText8436, 0, wx.ALL, 5 )

		resist_c_class36Choices = []
		self.resist_c_class36 = wx.Choice( self.resist_council_46, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class36Choices, 0 )
		self.resist_c_class36.SetSelection( 0 )
		fgSizer436.Add( self.resist_c_class36, 0, wx.ALL, 5 )

		self.m_staticText2036 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2036.Wrap( -1 )

		fgSizer436.Add( self.m_staticText2036, 0, wx.ALL, 5 )

		self.resist_c_persuasion36 = wx.TextCtrl( self.resist_council_46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer436.Add( self.resist_c_persuasion36, 0, wx.ALL, 5 )

		self.m_staticText2136 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2136.Wrap( -1 )

		fgSizer436.Add( self.m_staticText2136, 0, wx.ALL, 5 )

		self.resist_c_investigation36 = wx.TextCtrl( self.resist_council_46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer436.Add( self.resist_c_investigation36, 0, wx.ALL, 5 )

		self.m_staticText2236 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2236.Wrap( -1 )

		fgSizer436.Add( self.m_staticText2236, 0, wx.ALL, 5 )

		self.resist_c_espionage36 = wx.TextCtrl( self.resist_council_46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer436.Add( self.resist_c_espionage36, 0, wx.ALL, 5 )

		self.m_staticText2336 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2336.Wrap( -1 )

		fgSizer436.Add( self.m_staticText2336, 0, wx.ALL, 5 )

		self.resist_c_command36 = wx.TextCtrl( self.resist_council_46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer436.Add( self.resist_c_command36, 0, wx.ALL, 5 )

		self.m_staticText2436 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2436.Wrap( -1 )

		fgSizer436.Add( self.m_staticText2436, 0, wx.ALL, 5 )

		self.resist_c_administration36 = wx.TextCtrl( self.resist_council_46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer436.Add( self.resist_c_administration36, 0, wx.ALL, 5 )

		self.m_staticText2536 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2536.Wrap( -1 )

		fgSizer436.Add( self.m_staticText2536, 0, wx.ALL, 5 )

		self.resist_c_science36 = wx.TextCtrl( self.resist_council_46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer436.Add( self.resist_c_science36, 0, wx.ALL, 5 )

		self.m_staticText2636 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2636.Wrap( -1 )

		fgSizer436.Add( self.m_staticText2636, 0, wx.ALL, 5 )

		self.resist_c_security36 = wx.TextCtrl( self.resist_council_46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer436.Add( self.resist_c_security36, 0, wx.ALL, 5 )

		self.m_staticText2736 = wx.StaticText( self.resist_council_46, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2736.Wrap( -1 )

		fgSizer436.Add( self.m_staticText2736, 0, wx.ALL, 5 )

		self.resist_c_loyalty36 = wx.TextCtrl( self.resist_council_46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer436.Add( self.resist_c_loyalty36, 0, wx.ALL, 5 )


		self.resist_council_46.SetSizer( fgSizer436 )
		self.resist_council_46.Layout()
		fgSizer436.Fit( self.resist_council_46 )
		self.resist_sub_tabs6.AddPage( self.resist_council_46, u"Councilor 4", False )
		self.resist_council_56 = wx.Panel( self.resist_sub_tabs6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer446 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer446.SetFlexibleDirection( wx.BOTH )
		fgSizer446.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname46 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname46.Wrap( -1 )

		fgSizer446.Add( self.resist_c_fname46, 0, wx.ALL, 5 )

		self.resist_c_lname46 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname46.Wrap( -1 )

		fgSizer446.Add( self.resist_c_lname46, 0, wx.ALL, 5 )

		self.m_staticText8446 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8446.Wrap( -1 )

		fgSizer446.Add( self.m_staticText8446, 0, wx.ALL, 5 )

		resist_c_class46Choices = []
		self.resist_c_class46 = wx.Choice( self.resist_council_56, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class46Choices, 0 )
		self.resist_c_class46.SetSelection( 0 )
		fgSizer446.Add( self.resist_c_class46, 0, wx.ALL, 5 )

		self.m_staticText2046 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2046.Wrap( -1 )

		fgSizer446.Add( self.m_staticText2046, 0, wx.ALL, 5 )

		self.resist_c_persuasion46 = wx.TextCtrl( self.resist_council_56, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer446.Add( self.resist_c_persuasion46, 0, wx.ALL, 5 )

		self.m_staticText2146 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2146.Wrap( -1 )

		fgSizer446.Add( self.m_staticText2146, 0, wx.ALL, 5 )

		self.resist_c_investigation46 = wx.TextCtrl( self.resist_council_56, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer446.Add( self.resist_c_investigation46, 0, wx.ALL, 5 )

		self.m_staticText2246 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2246.Wrap( -1 )

		fgSizer446.Add( self.m_staticText2246, 0, wx.ALL, 5 )

		self.resist_c_espionage46 = wx.TextCtrl( self.resist_council_56, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer446.Add( self.resist_c_espionage46, 0, wx.ALL, 5 )

		self.m_staticText2346 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2346.Wrap( -1 )

		fgSizer446.Add( self.m_staticText2346, 0, wx.ALL, 5 )

		self.resist_c_command46 = wx.TextCtrl( self.resist_council_56, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer446.Add( self.resist_c_command46, 0, wx.ALL, 5 )

		self.m_staticText2446 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2446.Wrap( -1 )

		fgSizer446.Add( self.m_staticText2446, 0, wx.ALL, 5 )

		self.resist_c_administration46 = wx.TextCtrl( self.resist_council_56, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer446.Add( self.resist_c_administration46, 0, wx.ALL, 5 )

		self.m_staticText2546 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2546.Wrap( -1 )

		fgSizer446.Add( self.m_staticText2546, 0, wx.ALL, 5 )

		self.resist_c_science46 = wx.TextCtrl( self.resist_council_56, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer446.Add( self.resist_c_science46, 0, wx.ALL, 5 )

		self.m_staticText2646 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2646.Wrap( -1 )

		fgSizer446.Add( self.m_staticText2646, 0, wx.ALL, 5 )

		self.resist_c_security46 = wx.TextCtrl( self.resist_council_56, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer446.Add( self.resist_c_security46, 0, wx.ALL, 5 )

		self.m_staticText2746 = wx.StaticText( self.resist_council_56, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2746.Wrap( -1 )

		fgSizer446.Add( self.m_staticText2746, 0, wx.ALL, 5 )

		self.resist_c_loyalty46 = wx.TextCtrl( self.resist_council_56, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer446.Add( self.resist_c_loyalty46, 0, wx.ALL, 5 )


		self.resist_council_56.SetSizer( fgSizer446 )
		self.resist_council_56.Layout()
		fgSizer446.Fit( self.resist_council_56 )
		self.resist_sub_tabs6.AddPage( self.resist_council_56, u"Councilor 5", False )
		self.resist_council_66 = wx.Panel( self.resist_sub_tabs6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer456 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer456.SetFlexibleDirection( wx.BOTH )
		fgSizer456.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.resist_c_fname56 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_fname56.Wrap( -1 )

		fgSizer456.Add( self.resist_c_fname56, 0, wx.ALL, 5 )

		self.resist_c_lname56 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resist_c_lname56.Wrap( -1 )

		fgSizer456.Add( self.resist_c_lname56, 0, wx.ALL, 5 )

		self.m_staticText8456 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8456.Wrap( -1 )

		fgSizer456.Add( self.m_staticText8456, 0, wx.ALL, 5 )

		resist_c_class56Choices = []
		self.resist_c_class56 = wx.Choice( self.resist_council_66, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, resist_c_class56Choices, 0 )
		self.resist_c_class56.SetSelection( 0 )
		fgSizer456.Add( self.resist_c_class56, 0, wx.ALL, 5 )

		self.m_staticText2056 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2056.Wrap( -1 )

		fgSizer456.Add( self.m_staticText2056, 0, wx.ALL, 5 )

		self.resist_c_persuasion56 = wx.TextCtrl( self.resist_council_66, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer456.Add( self.resist_c_persuasion56, 0, wx.ALL, 5 )

		self.m_staticText2156 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2156.Wrap( -1 )

		fgSizer456.Add( self.m_staticText2156, 0, wx.ALL, 5 )

		self.resist_c_investigation56 = wx.TextCtrl( self.resist_council_66, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer456.Add( self.resist_c_investigation56, 0, wx.ALL, 5 )

		self.m_staticText2256 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Espionage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2256.Wrap( -1 )

		fgSizer456.Add( self.m_staticText2256, 0, wx.ALL, 5 )

		self.resist_c_espionage56 = wx.TextCtrl( self.resist_council_66, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer456.Add( self.resist_c_espionage56, 0, wx.ALL, 5 )

		self.m_staticText2356 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2356.Wrap( -1 )

		fgSizer456.Add( self.m_staticText2356, 0, wx.ALL, 5 )

		self.resist_c_command56 = wx.TextCtrl( self.resist_council_66, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer456.Add( self.resist_c_command56, 0, wx.ALL, 5 )

		self.m_staticText2456 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Administration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2456.Wrap( -1 )

		fgSizer456.Add( self.m_staticText2456, 0, wx.ALL, 5 )

		self.resist_c_administration56 = wx.TextCtrl( self.resist_council_66, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer456.Add( self.resist_c_administration56, 0, wx.ALL, 5 )

		self.m_staticText2556 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2556.Wrap( -1 )

		fgSizer456.Add( self.m_staticText2556, 0, wx.ALL, 5 )

		self.resist_c_science56 = wx.TextCtrl( self.resist_council_66, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer456.Add( self.resist_c_science56, 0, wx.ALL, 5 )

		self.m_staticText2656 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2656.Wrap( -1 )

		fgSizer456.Add( self.m_staticText2656, 0, wx.ALL, 5 )

		self.resist_c_security56 = wx.TextCtrl( self.resist_council_66, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer456.Add( self.resist_c_security56, 0, wx.ALL, 5 )

		self.m_staticText2756 = wx.StaticText( self.resist_council_66, wx.ID_ANY, u"Loyalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2756.Wrap( -1 )

		fgSizer456.Add( self.m_staticText2756, 0, wx.ALL, 5 )

		self.resist_c_loyalty56 = wx.TextCtrl( self.resist_council_66, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer456.Add( self.resist_c_loyalty56, 0, wx.ALL, 5 )


		self.resist_council_66.SetSizer( fgSizer456 )
		self.resist_council_66.Layout()
		fgSizer456.Fit( self.resist_council_66 )
		self.resist_sub_tabs6.AddPage( self.resist_council_66, u"Councilor 6", False )

		bSizer36.Add( self.resist_sub_tabs6, 0, wx.ALL|wx.EXPAND, 5 )


		self.exodus_panel.SetSizer( bSizer36 )
		self.exodus_panel.Layout()
		bSizer36.Fit( self.exodus_panel )
		self.app_tabs.AddPage( self.exodus_panel, u"Project Exodus", False )

		fgSizer61.Add( self.app_tabs, 1, wx.EXPAND |wx.ALL, 5 )

		additional_c_traits = wx.FlexGridSizer( 2, 4, 0, 0 )
		additional_c_traits.SetFlexibleDirection( wx.BOTH )
		additional_c_traits.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText581 = wx.StaticText( self, wx.ID_ANY, u"Active Traits", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText581.Wrap( -1 )

		additional_c_traits.Add( self.m_staticText581, 0, wx.ALL, 5 )

		self.m_staticText583 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText583.Wrap( -1 )

		additional_c_traits.Add( self.m_staticText583, 0, wx.ALL, 5 )

		self.m_staticText582 = wx.StaticText( self, wx.ID_ANY, u"Avilable Traits", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText582.Wrap( -1 )

		additional_c_traits.Add( self.m_staticText582, 0, wx.ALL, 5 )

		self.m_staticText580 = wx.StaticText( self, wx.ID_ANY, u"Age", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText580.Wrap( -1 )

		additional_c_traits.Add( self.m_staticText580, 0, wx.ALL, 5 )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,145 ), m_listBox1Choices, 0 )
		additional_c_traits.Add( self.m_listBox1, 0, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button2, 0, wx.ALL, 5 )


		additional_c_traits.Add( bSizer11, 1, wx.EXPAND, 5 )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,145 ), m_listBox2Choices, 0 )
		additional_c_traits.Add( self.m_listBox2, 0, wx.ALL, 5 )

		self.c_age = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 18, 200, 0 )
		additional_c_traits.Add( self.c_age, 0, wx.ALL, 5 )


		fgSizer61.Add( additional_c_traits, 0, 0, 5 )

		fgSizer59 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer59.SetFlexibleDirection( wx.BOTH )
		fgSizer59.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText589 = wx.StaticText( self, wx.ID_ANY, u"Completed Projects", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText589.Wrap( -1 )

		fgSizer59.Add( self.m_staticText589, 0, wx.ALL, 5 )

		self.m_staticText590 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText590.Wrap( -1 )

		fgSizer59.Add( self.m_staticText590, 0, wx.ALL, 5 )

		self.m_staticText591 = wx.StaticText( self, wx.ID_ANY, u"Available Projects", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText591.Wrap( -1 )

		fgSizer59.Add( self.m_staticText591, 0, wx.ALL, 5 )

		self.m_staticText588 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText588.Wrap( -1 )

		fgSizer59.Add( self.m_staticText588, 0, wx.ALL, 5 )

		self.m_staticText592 = wx.StaticText( self, wx.ID_ANY, u"Missed Projects", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText592.Wrap( -1 )

		fgSizer59.Add( self.m_staticText592, 0, wx.ALL, 5 )

		c_projectsChoices = []
		self.c_projects = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,100 ), c_projectsChoices, 0 )
		fgSizer59.Add( self.c_projects, 0, wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button4, 0, wx.ALL, 5 )


		fgSizer59.Add( bSizer10, 1, wx.EXPAND, 5 )

		a_projectsChoices = []
		self.a_projects = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,100 ), a_projectsChoices, 0 )
		fgSizer59.Add( self.a_projects, 0, wx.ALL, 5 )

		bSizer111 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_button6, 0, wx.ALL, 5 )


		fgSizer59.Add( bSizer111, 1, wx.EXPAND, 5 )

		m_projectsChoices = []
		self.m_projects = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,100 ), m_projectsChoices, 0 )
		fgSizer59.Add( self.m_projects, 0, wx.ALL, 5 )


		fgSizer61.Add( fgSizer59, 0, 0, 5 )


		bSizer.Add( fgSizer61, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.open_file, id = self.open.GetId() )
		self.Bind( wx.EVT_MENU, self.save_file, id = self.save.GetId() )
		self.Bind( wx.EVT_MENU, self.save_as, id = self.saveas.GetId() )
		self.Bind( wx.EVT_MENU, self.on_quit, id = self.quit.GetId() )
		self.Bind( wx.EVT_MENU, self.open_github, id = self.github.GetId() )
		self.Bind( wx.EVT_MENU, self.about_box, id = self.about.GetId() )
		self.app_tabs.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.tab_changed )
		self.research_slot1.Bind( wx.EVT_CHOICE, self.change_research_1 )
		self.research1_progress.Bind( wx.EVT_TEXT, self.update_research_1 )
		self.research_slot2.Bind( wx.EVT_CHOICE, self.change_research_2 )
		self.research2_progress.Bind( wx.EVT_TEXT, self.update_research_2 )
		self.research_slot3.Bind( wx.EVT_CHOICE, self.change_research_3 )
		self.research3_progress.Bind( wx.EVT_TEXT, self.update_research_3 )
		self.rouge_nuke_count.Bind( wx.EVT_SPINCTRL, self.change_loose_nukes )
		self.player_flag.Bind( wx.EVT_CHECKBOX, self.player_checkbox )
		self.m_spinCtrl2.Bind( wx.EVT_SPINCTRL, self.change_hate )
		self.resist_sub_tabs.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.sub_tab_changed )
		self.resist_money.Bind( wx.EVT_TEXT, self.update_money )
		self.resist_influence.Bind( wx.EVT_TEXT, self.update_influence )
		self.resist_ops.Bind( wx.EVT_TEXT, self.update_ops )
		self.resist_boost.Bind( wx.EVT_TEXT, self.update_boost )
		self.resist_water.Bind( wx.EVT_TEXT, self.update_water )
		self.resist_volatiles.Bind( wx.EVT_TEXT, self.update_volatiles )
		self.resist_basemetals.Bind( wx.EVT_TEXT, self.update_metals )
		self.resist_noblemetals.Bind( wx.EVT_TEXT, self.update_noblemetals )
		self.resist_fissiles.Bind( wx.EVT_TEXT, self.update_fissiles )
		self.resist_exotics.Bind( wx.EVT_TEXT, self.update_exotics )
		self.resist_antimatter.Bind( wx.EVT_TEXT, self.update_antimatter )
		self.resist_project1_progress.Bind( wx.EVT_TEXT, self.update_project_1 )
		self.resist_project2_progress.Bind( wx.EVT_TEXT, self.update_project_2 )
		self.resist_project3_progress.Bind( wx.EVT_TEXT, self.update_project_3 )
		self.resist_c_class.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class1.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion1.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation1.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage1.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command1.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration1.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science1.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security1.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty1.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class2.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion2.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation2.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage2.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command2.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration2.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science2.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security2.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty2.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class3.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion3.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation3.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage3.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command3.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration3.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science3.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security3.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty3.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class4.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion4.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation4.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage4.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command4.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration4.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science4.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security4.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty4.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class5.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion5.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation5.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage5.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command5.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration5.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science5.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security5.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty5.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.player_flag1.Bind( wx.EVT_CHECKBOX, self.player_checkbox )
		self.m_spinCtrl21.Bind( wx.EVT_SPINCTRL, self.change_hate )
		self.resist_sub_tabs1.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.sub_tab_changed )
		self.resist_money1.Bind( wx.EVT_TEXT, self.update_money )
		self.resist_influence1.Bind( wx.EVT_TEXT, self.update_influence )
		self.resist_ops1.Bind( wx.EVT_TEXT, self.update_ops )
		self.resist_boost1.Bind( wx.EVT_TEXT, self.update_boost )
		self.resist_water1.Bind( wx.EVT_TEXT, self.update_water )
		self.resist_volatiles1.Bind( wx.EVT_TEXT, self.update_volatiles )
		self.resist_basemetals1.Bind( wx.EVT_TEXT, self.update_metals )
		self.resist_noblemetals1.Bind( wx.EVT_TEXT, self.update_noblemetals )
		self.resist_fissiles1.Bind( wx.EVT_TEXT, self.update_fissiles )
		self.resist_exotics1.Bind( wx.EVT_TEXT, self.update_exotics )
		self.resist_antimatter1.Bind( wx.EVT_TEXT, self.update_antimatter )
		self.resist_project1_progress1.Bind( wx.EVT_TEXT, self.update_project_1 )
		self.resist_project2_progress1.Bind( wx.EVT_TEXT, self.update_project_2 )
		self.resist_project3_progress1.Bind( wx.EVT_TEXT, self.update_project_3 )
		self.resist_c_class6.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion6.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation6.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage6.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command6.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration6.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science6.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security6.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty6.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class11.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion11.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation11.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage11.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command11.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration11.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science11.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security11.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty11.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class21.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion21.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation21.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage21.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command21.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration21.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science21.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security21.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty21.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class31.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion31.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation31.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage31.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command31.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration31.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science31.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security31.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty31.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class41.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion41.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation41.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage41.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command41.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration41.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science41.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security41.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty41.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class51.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion51.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation51.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage51.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command51.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration51.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science51.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security51.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty51.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.player_flag2.Bind( wx.EVT_CHECKBOX, self.player_checkbox )
		self.m_spinCtrl22.Bind( wx.EVT_SPINCTRL, self.change_hate )
		self.resist_sub_tabs2.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.sub_tab_changed )
		self.resist_money2.Bind( wx.EVT_TEXT, self.update_money )
		self.resist_influence2.Bind( wx.EVT_TEXT, self.update_influence )
		self.resist_ops2.Bind( wx.EVT_TEXT, self.update_ops )
		self.resist_boost2.Bind( wx.EVT_TEXT, self.update_boost )
		self.resist_water2.Bind( wx.EVT_TEXT, self.update_water )
		self.resist_volatiles2.Bind( wx.EVT_TEXT, self.update_volatiles )
		self.resist_basemetals2.Bind( wx.EVT_TEXT, self.update_metals )
		self.resist_noblemetals2.Bind( wx.EVT_TEXT, self.update_noblemetals )
		self.resist_fissiles2.Bind( wx.EVT_TEXT, self.update_fissiles )
		self.resist_exotics2.Bind( wx.EVT_TEXT, self.update_exotics )
		self.resist_antimatter2.Bind( wx.EVT_TEXT, self.update_antimatter )
		self.resist_project1_progress2.Bind( wx.EVT_TEXT, self.update_project_1 )
		self.resist_project2_progress2.Bind( wx.EVT_TEXT, self.update_project_2 )
		self.resist_project3_progress2.Bind( wx.EVT_TEXT, self.update_project_3 )
		self.resist_c_class7.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion7.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation7.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage7.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command7.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration7.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science7.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security7.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty7.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class12.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion12.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation12.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage12.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command12.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration12.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science12.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security12.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty12.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class22.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion22.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation22.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage22.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command22.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration22.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science22.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security22.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty22.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class32.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion32.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation32.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage32.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command32.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration32.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science32.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security32.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty32.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class42.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion42.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation42.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage42.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command42.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration42.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science42.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security42.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty42.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class52.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion52.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation52.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage52.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command52.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration52.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science52.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security52.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty52.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.player_flag3.Bind( wx.EVT_CHECKBOX, self.player_checkbox )
		self.resist_sub_tabs3.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.sub_tab_changed )
		self.resist_money3.Bind( wx.EVT_TEXT, self.update_money )
		self.resist_influence3.Bind( wx.EVT_TEXT, self.update_influence )
		self.resist_ops3.Bind( wx.EVT_TEXT, self.update_ops )
		self.resist_boost3.Bind( wx.EVT_TEXT, self.update_boost )
		self.resist_water3.Bind( wx.EVT_TEXT, self.update_water )
		self.resist_volatiles3.Bind( wx.EVT_TEXT, self.update_volatiles )
		self.resist_basemetals3.Bind( wx.EVT_TEXT, self.update_metals )
		self.resist_noblemetals3.Bind( wx.EVT_TEXT, self.update_noblemetals )
		self.resist_fissiles3.Bind( wx.EVT_TEXT, self.update_fissiles )
		self.resist_exotics3.Bind( wx.EVT_TEXT, self.update_exotics )
		self.resist_antimatter3.Bind( wx.EVT_TEXT, self.update_antimatter )
		self.resist_project1_progress3.Bind( wx.EVT_TEXT, self.update_project_1 )
		self.resist_project2_progress3.Bind( wx.EVT_TEXT, self.update_project_2 )
		self.resist_project3_progress3.Bind( wx.EVT_TEXT, self.update_project_3 )
		self.resist_c_class8.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion8.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation8.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage8.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command8.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration8.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science8.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security8.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty8.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class13.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion13.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation13.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage13.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command13.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration13.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science13.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security13.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty13.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class23.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion23.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation23.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage23.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command23.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration23.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science23.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security23.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty23.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class33.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion33.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation33.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage33.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command33.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration33.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science33.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security33.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty33.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class43.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion43.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation43.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage43.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command43.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration43.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science43.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security43.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty43.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class53.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion53.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation53.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage53.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command53.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration53.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science53.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security53.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty53.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.player_flag4.Bind( wx.EVT_CHECKBOX, self.player_checkbox )
		self.resist_sub_tabs4.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.sub_tab_changed )
		self.resist_money4.Bind( wx.EVT_TEXT, self.update_money )
		self.resist_influence4.Bind( wx.EVT_TEXT, self.update_influence )
		self.resist_ops4.Bind( wx.EVT_TEXT, self.update_ops )
		self.resist_boost4.Bind( wx.EVT_TEXT, self.update_boost )
		self.resist_water4.Bind( wx.EVT_TEXT, self.update_water )
		self.resist_volatiles4.Bind( wx.EVT_TEXT, self.update_volatiles )
		self.resist_basemetals4.Bind( wx.EVT_TEXT, self.update_metals )
		self.resist_noblemetals4.Bind( wx.EVT_TEXT, self.update_noblemetals )
		self.resist_fissiles4.Bind( wx.EVT_TEXT, self.update_fissiles )
		self.resist_exotics4.Bind( wx.EVT_TEXT, self.update_exotics )
		self.resist_antimatter4.Bind( wx.EVT_TEXT, self.update_antimatter )
		self.resist_project1_progress4.Bind( wx.EVT_TEXT, self.update_project_1 )
		self.resist_project2_progress4.Bind( wx.EVT_TEXT, self.update_project_2 )
		self.resist_project3_progress4.Bind( wx.EVT_TEXT, self.update_project_3 )
		self.resist_c_class9.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion9.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation9.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage9.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command9.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration9.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science9.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security9.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty9.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class14.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion14.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation14.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage14.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command14.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration14.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science14.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security14.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty14.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class24.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion24.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation24.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage24.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command24.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration24.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science24.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security24.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty24.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class34.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion34.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation34.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage34.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command34.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration34.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science34.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security34.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty34.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class44.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion44.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation44.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage44.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command44.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration44.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science44.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security44.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty44.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class54.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion54.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation54.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage54.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command54.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration54.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science54.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security54.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty54.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.player_flag5.Bind( wx.EVT_CHECKBOX, self.player_checkbox )
		self.m_spinCtrl25.Bind( wx.EVT_SPINCTRL, self.change_hate )
		self.resist_sub_tabs5.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.sub_tab_changed )
		self.resist_money5.Bind( wx.EVT_TEXT, self.update_money )
		self.resist_influence5.Bind( wx.EVT_TEXT, self.update_influence )
		self.resist_ops5.Bind( wx.EVT_TEXT, self.update_ops )
		self.resist_boost5.Bind( wx.EVT_TEXT, self.update_boost )
		self.resist_water5.Bind( wx.EVT_TEXT, self.update_water )
		self.resist_volatiles5.Bind( wx.EVT_TEXT, self.update_volatiles )
		self.resist_basemetals5.Bind( wx.EVT_TEXT, self.update_metals )
		self.resist_noblemetals5.Bind( wx.EVT_TEXT, self.update_noblemetals )
		self.resist_fissiles5.Bind( wx.EVT_TEXT, self.update_fissiles )
		self.resist_exotics5.Bind( wx.EVT_TEXT, self.update_exotics )
		self.resist_antimatter5.Bind( wx.EVT_TEXT, self.update_antimatter )
		self.resist_project1_progress5.Bind( wx.EVT_TEXT, self.update_project_1 )
		self.resist_project2_progress5.Bind( wx.EVT_TEXT, self.update_project_2 )
		self.resist_project3_progress5.Bind( wx.EVT_TEXT, self.update_project_3 )
		self.resist_c_class10.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion10.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation10.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage10.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command10.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration10.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science10.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security10.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty10.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class15.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion15.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation15.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage15.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command15.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration15.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science15.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security15.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty15.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class25.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion25.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation25.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage25.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command25.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration25.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science25.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security25.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty25.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class35.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion35.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation35.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage35.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command35.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration35.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science35.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security35.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty35.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class45.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion45.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation45.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage45.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command45.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration45.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science45.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security45.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty45.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class55.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion55.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation55.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage55.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command55.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration55.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science55.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security55.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty55.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.player_flag6.Bind( wx.EVT_CHECKBOX, self.player_checkbox )
		self.m_spinCtrl26.Bind( wx.EVT_SPINCTRL, self.change_hate )
		self.resist_sub_tabs6.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.sub_tab_changed )
		self.resist_money6.Bind( wx.EVT_TEXT, self.update_money )
		self.resist_influence6.Bind( wx.EVT_TEXT, self.update_influence )
		self.resist_ops6.Bind( wx.EVT_TEXT, self.update_ops )
		self.resist_boost6.Bind( wx.EVT_TEXT, self.update_boost )
		self.resist_water6.Bind( wx.EVT_TEXT, self.update_water )
		self.resist_volatiles6.Bind( wx.EVT_TEXT, self.update_volatiles )
		self.resist_basemetals6.Bind( wx.EVT_TEXT, self.update_metals )
		self.resist_noblemetals6.Bind( wx.EVT_TEXT, self.update_noblemetals )
		self.resist_fissiles6.Bind( wx.EVT_TEXT, self.update_fissiles )
		self.resist_exotics6.Bind( wx.EVT_TEXT, self.update_exotics )
		self.resist_antimatter6.Bind( wx.EVT_TEXT, self.update_antimatter )
		self.resist_project1_progress6.Bind( wx.EVT_TEXT, self.update_project_1 )
		self.resist_project2_progress6.Bind( wx.EVT_TEXT, self.update_project_2 )
		self.resist_project3_progress6.Bind( wx.EVT_TEXT, self.update_project_3 )
		self.resist_c_class16.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion16.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation16.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage16.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command16.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration16.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science16.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security16.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty16.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class17.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion17.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation17.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage17.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command17.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration17.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science17.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security17.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty17.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class26.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion26.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation26.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage26.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command26.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration26.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science26.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security26.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty26.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class36.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion36.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation36.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage36.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command36.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration36.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science36.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security36.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty36.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class46.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion46.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation46.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage46.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command46.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration46.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science46.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security46.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty46.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.resist_c_class56.Bind( wx.EVT_CHOICE, self.change_councilor_job )
		self.resist_c_persuasion56.Bind( wx.EVT_TEXT, self.change_councilor_persuasion )
		self.resist_c_investigation56.Bind( wx.EVT_TEXT, self.change_councilor_investigation )
		self.resist_c_espionage56.Bind( wx.EVT_TEXT, self.change_councilor_espionage )
		self.resist_c_command56.Bind( wx.EVT_TEXT, self.change_councilor_command )
		self.resist_c_administration56.Bind( wx.EVT_TEXT, self.change_councilor_administration )
		self.resist_c_science56.Bind( wx.EVT_TEXT, self.change_councilor_science )
		self.resist_c_security56.Bind( wx.EVT_TEXT, self.change_councilor_security )
		self.resist_c_loyalty56.Bind( wx.EVT_TEXT, self.change_councilor_loyalty )
		self.m_button1.Bind( wx.EVT_BUTTON, self.remove_trait )
		self.m_button2.Bind( wx.EVT_BUTTON, self.add_trait )
		self.c_age.Bind( wx.EVT_SPINCTRL, self.change_age )
		self.c_age.Bind( wx.EVT_TEXT, self.change_age )
		self.m_button3.Bind( wx.EVT_BUTTON, self.undo_project )
		self.m_button4.Bind( wx.EVT_BUTTON, self.complete_project )
		self.m_button5.Bind( wx.EVT_BUTTON, self.lock_project )
		self.m_button6.Bind( wx.EVT_BUTTON, self.unlock_project )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def open_file( self, event ):
		event.Skip()

	def save_file( self, event ):
		event.Skip()

	def save_as( self, event ):
		event.Skip()

	def on_quit( self, event ):
		event.Skip()

	def open_github( self, event ):
		event.Skip()

	def about_box( self, event ):
		event.Skip()

	def tab_changed( self, event ):
		event.Skip()

	def change_research_1( self, event ):
		event.Skip()

	def update_research_1( self, event ):
		event.Skip()

	def change_research_2( self, event ):
		event.Skip()

	def update_research_2( self, event ):
		event.Skip()

	def change_research_3( self, event ):
		event.Skip()

	def update_research_3( self, event ):
		event.Skip()

	def change_loose_nukes( self, event ):
		event.Skip()

	def player_checkbox( self, event ):
		event.Skip()

	def change_hate( self, event ):
		event.Skip()

	def sub_tab_changed( self, event ):
		event.Skip()

	def update_money( self, event ):
		event.Skip()

	def update_influence( self, event ):
		event.Skip()

	def update_ops( self, event ):
		event.Skip()

	def update_boost( self, event ):
		event.Skip()

	def update_water( self, event ):
		event.Skip()

	def update_volatiles( self, event ):
		event.Skip()

	def update_metals( self, event ):
		event.Skip()

	def update_noblemetals( self, event ):
		event.Skip()

	def update_fissiles( self, event ):
		event.Skip()

	def update_exotics( self, event ):
		event.Skip()

	def update_antimatter( self, event ):
		event.Skip()

	def update_project_1( self, event ):
		event.Skip()

	def update_project_2( self, event ):
		event.Skip()

	def update_project_3( self, event ):
		event.Skip()

	def change_councilor_job( self, event ):
		event.Skip()

	def change_councilor_persuasion( self, event ):
		event.Skip()

	def change_councilor_investigation( self, event ):
		event.Skip()

	def change_councilor_espionage( self, event ):
		event.Skip()

	def change_councilor_command( self, event ):
		event.Skip()

	def change_councilor_administration( self, event ):
		event.Skip()

	def change_councilor_science( self, event ):
		event.Skip()

	def change_councilor_security( self, event ):
		event.Skip()

	def change_councilor_loyalty( self, event ):
		event.Skip()






















































































































































































































































































































































































































































































	def remove_trait( self, event ):
		event.Skip()

	def add_trait( self, event ):
		event.Skip()

	def change_age( self, event ):
		event.Skip()


	def undo_project( self, event ):
		event.Skip()

	def complete_project( self, event ):
		event.Skip()

	def lock_project( self, event ):
		event.Skip()

	def unlock_project( self, event ):
		event.Skip()


