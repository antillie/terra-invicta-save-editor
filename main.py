#!/usr/bin/env python3

#######################################################################################
## Terra Invicta Save Editor v0.4.3
##
## Copyright (C) 2022 George Markeloff
## 
## Distributed under the terms of the GNU General Public License v3.
## See LICENSE.txt or https://www.gnu.org/licenses/gpl-3.0.html for license details.
##
## This program is not associated with Hooded Horse or Pavonis Interactive in any way.
## You are strongly encouraged to back up your save file before modifying it.
#######################################################################################

import json, gzip, os, webbrowser, wx, gui, game_data
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Make a class that inherits from the "Main" frame created in wxFormBuilder.
class ti_save_editor(gui.Main):
    
    def __init__(self,parent):
        # Initialize parent class so the GUI will load and function.
        gui.Main.__init__(self, parent)
        
        # Set some defaults.
        self.docs = os.path.expanduser("~\Documents\My Games\TerraInvicta\Saves\\")
        self.using_compression = ""
        self.data = {}
        self.player_faction = ""
        self.faction_ids = {}
        self.faction_ids["resist"] = 0
        self.faction_ids["humanity"] = 0
        self.faction_ids["initative"] = 0
        self.faction_ids["servants"] = 0
        self.faction_ids["protectorate"] = 0
        self.faction_ids["academy"] = 0
        self.faction_ids["exodus"] = 0
        
        self.research_slot1.AppendItems(game_data.tech_list)
        self.research_slot2.AppendItems(game_data.tech_list)
        self.research_slot3.AppendItems(game_data.tech_list)
        
        self.resist_c_class.AppendItems(game_data.jobs)
        self.resist_c_class1.AppendItems(game_data.jobs)
        self.resist_c_class2.AppendItems(game_data.jobs)
        self.resist_c_class3.AppendItems(game_data.jobs)
        self.resist_c_class4.AppendItems(game_data.jobs)
        self.resist_c_class5.AppendItems(game_data.jobs)
        self.resist_c_class6.AppendItems(game_data.jobs)
        self.resist_c_class11.AppendItems(game_data.jobs)
        self.resist_c_class21.AppendItems(game_data.jobs)
        self.resist_c_class31.AppendItems(game_data.jobs)
        self.resist_c_class41.AppendItems(game_data.jobs)
        self.resist_c_class51.AppendItems(game_data.jobs)
        self.resist_c_class7.AppendItems(game_data.jobs)
        self.resist_c_class12.AppendItems(game_data.jobs)
        self.resist_c_class22.AppendItems(game_data.jobs)
        self.resist_c_class32.AppendItems(game_data.jobs)
        self.resist_c_class42.AppendItems(game_data.jobs)
        self.resist_c_class52.AppendItems(game_data.jobs)
        self.resist_c_class8.AppendItems(game_data.jobs)
        self.resist_c_class13.AppendItems(game_data.jobs)
        self.resist_c_class23.AppendItems(game_data.jobs)
        self.resist_c_class33.AppendItems(game_data.jobs)
        self.resist_c_class43.AppendItems(game_data.jobs)
        self.resist_c_class53.AppendItems(game_data.jobs)
        self.resist_c_class9.AppendItems(game_data.jobs)
        self.resist_c_class14.AppendItems(game_data.jobs)
        self.resist_c_class24.AppendItems(game_data.jobs)
        self.resist_c_class34.AppendItems(game_data.jobs)
        self.resist_c_class44.AppendItems(game_data.jobs)
        self.resist_c_class54.AppendItems(game_data.jobs)
        self.resist_c_class10.AppendItems(game_data.jobs)
        self.resist_c_class15.AppendItems(game_data.jobs)
        self.resist_c_class25.AppendItems(game_data.jobs)
        self.resist_c_class35.AppendItems(game_data.jobs)
        self.resist_c_class45.AppendItems(game_data.jobs)
        self.resist_c_class55.AppendItems(game_data.jobs)
        self.resist_c_class16.AppendItems(game_data.jobs)
        self.resist_c_class17.AppendItems(game_data.jobs)
        self.resist_c_class26.AppendItems(game_data.jobs)
        self.resist_c_class36.AppendItems(game_data.jobs)
        self.resist_c_class46.AppendItems(game_data.jobs)
        self.resist_c_class56.AppendItems(game_data.jobs)
        
        self.player_checkboxes = []
        self.player_checkboxes.append(self.player_flag)
        self.player_checkboxes.append(self.player_flag1)
        self.player_checkboxes.append(self.player_flag2)
        self.player_checkboxes.append(self.player_flag3)
        self.player_checkboxes.append(self.player_flag4)
        self.player_checkboxes.append(self.player_flag5)
        self.player_checkboxes.append(self.player_flag6)
        
        self.m_staticText580.Hide()
        self.m_staticText581.Hide()
        self.m_staticText582.Hide()
        self.m_staticText583.Hide()
        self.m_listBox1.Hide()
        self.m_listBox2.Hide()
        self.m_button1.Hide()
        self.m_button2.Hide()
        self.c_age.Hide()
        
        self.m_staticText589.Hide()
        self.m_staticText590.Hide()
        self.m_staticText591.Hide()
        self.m_staticText592.Hide()
        self.m_button3.Hide()
        self.m_button4.Hide()
        self.m_button5.Hide()
        self.m_button6.Hide()
        self.c_projects.Hide()
        self.m_projects.Hide()
        self.a_projects.Hide()
        
        self.councilors = {}
        
    # Prompts the user to select a TI save file to load using the system's standard open file dialog.
    def open_file(self, event):
        with wx.FileDialog(self, "Open Terra Invicta Save File", wildcard="Terra Invicta Saves (*.gz;*.json)|*.gz;*.json", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, defaultDir=self.docs) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            self.active_file = fileDialog.GetPath()
            self.load_save()
    
    # Opens the file at the location selected in the open_file function, reads it, and parses the JSON into a dictionary so we can work with it.
    def load_save(self):
        
        # Split the filename on the "." so we can get the file extension.
        parts = self.active_file.split(".")
        
        # Use the file extension to determine if we are using compression or not, open the file accordingly, and make a note of if we are using compression or not.
        if parts[1] == "gz":
            # Open compressed save files with gzip.
            f = gzip.open(self.active_file, "rb")
            file_content = f.read()
            f.close()
            # Convert the raw binary gzip output to proper utf-8 text.
            text = file_content.decode()
            self.using_compression = True
        else:
            # Open uncompressed save files as straight text.
            f = open(self.active_file, "r")
            text = f.read()
            f.close()
            self.using_compression = False
        
        # Parse the JSON data from the save file into a dictionary so we can work with it.
        self.data = json.loads(text)
        
        # Some shortcuts to make addressing these parts of the save easier.
        self.global_research = self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalResearchState"][0]["Value"]["techProgress"]
        self.finished_global_techs = self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalResearchState"][0]["Value"]["finishedTechsNames"]
        
        # Get the current in game date.
        self.game_date = self.make_date_object(self.data["gamestates"]["PavonisInteractive.TerraInvicta.TITimeState"][0]["Value"]["currentDateTime"])
        
        # Update the UI with the new data.
        self.update_ui_data()
    
    # Converts a Terra Invicta JSON date object into a Python datetime object.
    def make_date_object(self, game_date):
        
        if game_date["month"] < 10:
            month = "0" + str(game_date["month"])
        else:
            month = str(game_date["month"])
        if game_date["day"] < 10:
            day = "0" + str(game_date["day"])
        else:
            day = str(game_date["day"])
            
        datetime_str = str(game_date["year"]) + ":" + month + ":" + day
        date_object = datetime.strptime(datetime_str, "%Y:%m:%d")
        return date_object
        
    # Saves the current data, overwriting the most recently opened file.
    def save_file(self, event):
        
        # Don't try to write anything if we haven't opened a save file yet.
        if self.using_compression == "":
            return
        
        # Make our save data dictionary a JSON string with pretty spacing exactly like the game does.
        text_data = json.dumps(self.data, indent=4, separators=(",", ": "))
        
        # Write the new file in either gzip or text format depending on what type of file we opened.
        if self.using_compression:
            # Gzip needs binary input so convert our utf-8 JSON string to binary.
            binary_data = text_data.encode()
            f = gzip.open(self.active_file, "wb")
            f.write(binary_data)
            f.close()
        else:
            # Uncompressed save files can simply be written to disk directly.
            f = open(self.active_file, "w")
            f.write(text_data)
            f.close()
    
    # Uses a stanndard system save dialog to prompt the user for the filename and location at which to save a file.
    def save_as(self, event):
        
        # Don't try to write anything if we haven't opened a save file yet.
        if self.using_compression == "":
            return
        # Compressed save files should have a ".gz" file extension.
        elif self.using_compression == True:
            wildcard = "Compressed Terra Invicta Save (*.gz)|*.gz"
        # Uncompressed save files should have a ".json" file extension.
        elif self.using_compression == False:
            wildcard = "Uncompressed Terra Invicta Save (*.json)|*.json"
        
        with wx.FileDialog(self, "Save As", wildcard=wildcard, style=wx.FD_SAVE, defaultDir=self.docs) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            save_location = fileDialog.GetPath()
        
        # Confirm before overwiriting an existing file.
        if os.path.exists(save_location):
            confirm = wx.MessageDialog(None, ("Overwrite exiting file?"), ("Target File Already Exists"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION).ShowModal()
            
            # If the user didn't decide to overwrite the existing file then don't do anything.
            if confirm != wx.ID_YES:
                return
        
        # Make our save data dictionary a string with pretty spacing exactly like the game does..
        text_data = json.dumps(self.data, indent=4, separators=(",", ": "))
        
        # Write the new file in either gzip or text format depending on what type of file we opened.
        if self.using_compression:
            # Gzip needs binary input so convert our utf-8 JSON string to binary.
            binary_data = text_data.encode()
            f = gzip.open(save_location, "wb")
            f.write(binary_data)
            f.close()
        else:
            # Uncompressed save files can simply be written to disk directly.
            f = open(save_location, "w")
            f.write(text_data)
            f.close()
    
    def open_github(self, event):
        webbrowser.open_new_tab("https://github.com/antillie/terra-invicta-save-editor")
    
    # Keeps track of which faction tab is selected.
    def tab_changed(self, event):
        self.page = self.app_tabs.GetPageText(event.GetSelection())
        self.sub_tab_changed(self, self.get_active_faction_id())
        
    # Keeps track of which councilor tab is selected.
    def sub_tab_changed(self, event, faction=None):
        if faction == None:
            self.sub_page = event.GetEventObject().GetPageText(event.GetSelection())
        else:
            for key, value in self.faction_ids.items():
                if faction == value:
                    if key == "resist":
                        self.sub_page = self.resist_sub_tabs.GetSelection()
                    if key == "humanity":
                        self.sub_page = self.resist_sub_tabs1.GetSelection()
                    if key == "initative":
                        self.sub_page = self.resist_sub_tabs2.GetSelection()
                    if key == "servants":
                        self.sub_page = self.resist_sub_tabs3.GetSelection()
                    if key == "protectorate":
                        self.sub_page = self.resist_sub_tabs4.GetSelection()
                    if key == "academy":
                        self.sub_page = self.resist_sub_tabs5.GetSelection()
                    if key == "exodus":
                        self.sub_page = self.resist_sub_tabs6.GetSelection()

        self.m_staticText580.Hide()
        self.m_staticText581.Hide()
        self.m_staticText582.Hide()
        self.m_staticText583.Hide()
        self.m_listBox1.Hide()
        self.m_listBox2.Hide()
        self.m_button1.Hide()
        self.m_button2.Hide()
        self.c_age.Hide()
        self.m_staticText589.Hide()
        self.m_staticText590.Hide()
        self.m_staticText591.Hide()
        self.m_staticText592.Hide()
        self.m_button3.Hide()
        self.m_button4.Hide()
        self.m_button5.Hide()
        self.m_button6.Hide()
        self.c_projects.Hide()
        self.m_projects.Hide()
        self.a_projects.Hide()
        
        if self.sub_page == 0:
            return
        elif self.sub_page == 1:
            self.sub_page = "Project R"
        elif self.sub_page == 2:
            self.sub_page = "Councilor 1"
        elif self.sub_page == 3:
            self.sub_page = "Councilor 2"
        elif self.sub_page == 4:
            self.sub_page = "Councilor 3"
        elif self.sub_page == 5:
            self.sub_page = "Councilor 4"
        elif self.sub_page == 6:
            self.sub_page = "Councilor 5"
        elif self.sub_page == 9:
            self.sub_page = "Councilor 6"
        
        if "Councilor" in self.sub_page:
            self.m_staticText580.Show()
            self.m_staticText581.Show()
            self.m_staticText582.Show()
            self.m_staticText583.Show()
            self.m_listBox1.Show()
            self.m_listBox2.Show()
            self.m_button1.Show()
            self.m_button2.Show()
            self.c_age.Show()
            self.show_councilor_extras()
        elif "Project" in self.sub_page:
            self.m_staticText589.Show()
            self.m_staticText590.Show()
            self.m_staticText591.Show()
            self.m_staticText592.Show()
            self.m_button3.Show()
            self.m_button4.Show()
            self.m_button5.Show()
            self.m_button6.Show()
            self.c_projects.Show()
            self.m_projects.Show()
            self.a_projects.Show()
            self.show_project_extras()
        
        # Update the positions of the GUI widgets so the councilor and project area's can share the same space.
        self.Layout()
        
    # Manages loading the data from the save file into the UI.
    def update_ui_data(self):
        # Update the global research tab.
        self.update_global_research()
        
        # Look for the player controled faction and get the faction IDs.
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIPlayerState"]:
            if item["Value"]["name"] == "ResistPlayer":
                self.faction_ids["resist"] = self.get_faction_id_from_player_id(item["Value"]["ID"]["value"])
                self.councilors[str(self.get_faction_id_from_player_id(item["Value"]["ID"]["value"]))] = [""]
                if not item["Value"]["isAI"]:
                    self.player_faction = "resist"
                    self.player_flag.SetValue(True)
            elif item["Value"]["name"] == "DestroyPlayer":
                self.faction_ids["humanity"] = self.get_faction_id_from_player_id(item["Value"]["ID"]["value"])
                self.councilors[str(self.get_faction_id_from_player_id(item["Value"]["ID"]["value"]))] = [""]
                if not item["Value"]["isAI"]:
                    self.player_faction = "humanity"
                    self.player_flag1.SetValue(True)
            elif item["Value"]["name"] == "ExploitPlayer":
                self.faction_ids["initative"] = self.get_faction_id_from_player_id(item["Value"]["ID"]["value"])
                self.councilors[str(self.get_faction_id_from_player_id(item["Value"]["ID"]["value"]))] = [""]
                if not item["Value"]["isAI"]:
                    self.player_faction = "initative"
                    self.player_flag2.SetValue(True)
            elif item["Value"]["name"] == "SubmitPlayer":
                self.faction_ids["servants"] = self.get_faction_id_from_player_id(item["Value"]["ID"]["value"])
                self.councilors[str(self.get_faction_id_from_player_id(item["Value"]["ID"]["value"]))] = [""]
                if not item["Value"]["isAI"]:
                    self.player_faction = "servants"
                    self.player_flag3.SetValue(True)
            elif item["Value"]["name"] == "AppeasePlayer":
                self.faction_ids["protectorate"] = self.get_faction_id_from_player_id(item["Value"]["ID"]["value"])
                self.councilors[str(self.get_faction_id_from_player_id(item["Value"]["ID"]["value"]))] = [""]
                if not item["Value"]["isAI"]:
                    self.player_faction = "protectorate"
                    self.player_flag4.SetValue(True)
            elif item["Value"]["name"] == "CooperatePlayer":
                self.faction_ids["academy"] = self.get_faction_id_from_player_id(item["Value"]["ID"]["value"])
                self.councilors[str(self.get_faction_id_from_player_id(item["Value"]["ID"]["value"]))] = [""]
                if not item["Value"]["isAI"]:
                    self.player_faction = "academy"
                    self.player_flag5.SetValue(True)
            elif item["Value"]["name"] == "EscapePlayer":
                self.faction_ids["exodus"] = self.get_faction_id_from_player_id(item["Value"]["ID"]["value"])
                self.councilors[str(self.get_faction_id_from_player_id(item["Value"]["ID"]["value"]))] = [""]
                if not item["Value"]["isAI"]:
                    self.player_faction = "exodus"
                    self.player_flag6.SetValue(True)
            elif item["Value"]["name"] == "AlienPlayer":
                self.faction_ids["alien"] = self.get_faction_id_from_player_id(item["Value"]["ID"]["value"])
                self.councilors[str(self.get_faction_id_from_player_id(item["Value"]["ID"]["value"]))] = [""]
        
        # The alien faction data is read a bit differently.    
        self.aliens = self.get_aliens()
        self.read_alien_hate()
        
        # Load the number of loose nukes.
        self.rouge_nuke_count.SetValue(self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalValuesState"][0]["Value"]["looseNukes"])
        
        # Update each faction's resource tab.
        self.update_resources()
        
        # Update each faction's projects.
        self.update_projects()
        
        # Update each faction's councilors.
        self.update_councilors()
            
    def get_faction_id_from_player_id(self, player_id):
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Value"]["player"]["value"] == player_id:
                return item["Key"]["value"]
    
    # Changes the number of loose nukes.
    def change_loose_nukes(self, event):
        self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalValuesState"][0]["Value"]["looseNukes"] = int(self.rouge_nuke_count.GetValue())
    
    # Get the faction ID for whatever faction tab is currently selected.
    def get_active_faction_id(self):
        try:
            if self.page == "The Resistance":
                faction_id = self.faction_ids["resist"]
            elif self.page == "Humanity First":
                faction_id = self.faction_ids["humanity"]
            elif self.page == "The Initiative":
                faction_id = self.faction_ids["initative"]
            elif self.page == "The Servants":
                faction_id = self.faction_ids["servants"]
            elif self.page == "The Protectorate":
                faction_id = self.faction_ids["protectorate"]
            elif self.page == "The Academy":
                faction_id = self.faction_ids["academy"]
            elif self.page == "Project Exodus":
                faction_id = self.faction_ids["exodus"]
            return faction_id
        except:
            return 0
    
    # Assigns the alien faction data block an easily accessable label.
    def get_aliens(self):
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.faction_ids["alien"]:
                return item
        
    # Reads the alien's hate levels and puts them in the UI.
    def read_alien_hate(self):
        self.alien_hate = {}
        for item in self.aliens["Value"]["factionHate"]:
            self.alien_hate[str(item["Key"]["value"])] = item["Value"]
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.faction_ids["resist"]:
                self.m_spinCtrl2.SetValue(int(self.alien_hate[str(self.faction_ids["resist"])]))
            if item["Key"]["value"] == self.faction_ids["humanity"]:
                self.m_spinCtrl21.SetValue(int(self.alien_hate[str(self.faction_ids["humanity"])]))
            if item["Key"]["value"] == self.faction_ids["initative"]:
                self.m_spinCtrl22.SetValue(int(self.alien_hate[str(self.faction_ids["initative"])]))
            if item["Key"]["value"] == self.faction_ids["protectorate"]:
                self.m_spinCtrl24.SetValue(int(self.alien_hate[str(self.faction_ids["protectorate"])]))
            if item["Key"]["value"] == self.faction_ids["academy"]:
                self.m_spinCtrl25.SetValue(int(self.alien_hate[str(self.faction_ids["academy"])]))
            if item["Key"]["value"] == self.faction_ids["exodus"]:
                self.m_spinCtrl26.SetValue(int(self.alien_hate[str(self.faction_ids["exodus"])]))
    
    # Displays each faction's resources in the UI.
    def update_resources(self):
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.faction_ids["resist"]:
                self.resist_money.SetValue(str(item["Value"]["resources"]["Money"]))
                self.resist_influence.SetValue(str(item["Value"]["resources"]["Influence"]))
                self.resist_ops.SetValue(str(item["Value"]["resources"]["Operations"]))
                self.resist_boost.SetValue(str(item["Value"]["resources"]["Boost"]))
                self.resist_water.SetValue(str(item["Value"]["resources"]["Water"]))
                self.resist_volatiles.SetValue(str(item["Value"]["resources"]["Volatiles"]))
                self.resist_basemetals.SetValue(str(item["Value"]["resources"]["Metals"]))
                self.resist_noblemetals.SetValue(str(item["Value"]["resources"]["NobleMetals"]))
                self.resist_fissiles.SetValue(str(item["Value"]["resources"]["Fissiles"]))
                self.resist_exotics.SetValue(str(item["Value"]["resources"]["Exotics"]))
                self.resist_antimatter.SetValue(str(item["Value"]["resources"]["Antimatter"]))
            if item["Key"]["value"] == self.faction_ids["humanity"]:
                self.resist_money1.SetValue(str(item["Value"]["resources"]["Money"]))
                self.resist_influence1.SetValue(str(item["Value"]["resources"]["Influence"]))
                self.resist_ops1.SetValue(str(item["Value"]["resources"]["Operations"]))
                self.resist_boost1.SetValue(str(item["Value"]["resources"]["Boost"]))
                self.resist_water1.SetValue(str(item["Value"]["resources"]["Water"]))
                self.resist_volatiles1.SetValue(str(item["Value"]["resources"]["Volatiles"]))
                self.resist_basemetals1.SetValue(str(item["Value"]["resources"]["Metals"]))
                self.resist_noblemetals1.SetValue(str(item["Value"]["resources"]["NobleMetals"]))
                self.resist_fissiles1.SetValue(str(item["Value"]["resources"]["Fissiles"]))
                self.resist_exotics1.SetValue(str(item["Value"]["resources"]["Exotics"]))
                self.resist_antimatter1.SetValue(str(item["Value"]["resources"]["Antimatter"]))
            if item["Key"]["value"] == self.faction_ids["initative"]:
                self.resist_money2.SetValue(str(item["Value"]["resources"]["Money"]))
                self.resist_influence2.SetValue(str(item["Value"]["resources"]["Influence"]))
                self.resist_ops2.SetValue(str(item["Value"]["resources"]["Operations"]))
                self.resist_boost2.SetValue(str(item["Value"]["resources"]["Boost"]))
                self.resist_water2.SetValue(str(item["Value"]["resources"]["Water"]))
                self.resist_volatiles2.SetValue(str(item["Value"]["resources"]["Volatiles"]))
                self.resist_basemetals2.SetValue(str(item["Value"]["resources"]["Metals"]))
                self.resist_noblemetals2.SetValue(str(item["Value"]["resources"]["NobleMetals"]))
                self.resist_fissiles2.SetValue(str(item["Value"]["resources"]["Fissiles"]))
                self.resist_exotics2.SetValue(str(item["Value"]["resources"]["Exotics"]))
                self.resist_antimatter2.SetValue(str(item["Value"]["resources"]["Antimatter"]))
            if item["Key"]["value"] == self.faction_ids["servants"]:
                self.resist_money3.SetValue(str(item["Value"]["resources"]["Money"]))
                self.resist_influence3.SetValue(str(item["Value"]["resources"]["Influence"]))
                self.resist_ops3.SetValue(str(item["Value"]["resources"]["Operations"]))
                self.resist_boost3.SetValue(str(item["Value"]["resources"]["Boost"]))
                self.resist_water3.SetValue(str(item["Value"]["resources"]["Water"]))
                self.resist_volatiles3.SetValue(str(item["Value"]["resources"]["Volatiles"]))
                self.resist_basemetals3.SetValue(str(item["Value"]["resources"]["Metals"]))
                self.resist_noblemetals3.SetValue(str(item["Value"]["resources"]["NobleMetals"]))
                self.resist_fissiles3.SetValue(str(item["Value"]["resources"]["Fissiles"]))
                self.resist_exotics3.SetValue(str(item["Value"]["resources"]["Exotics"]))
                self.resist_antimatter3.SetValue(str(item["Value"]["resources"]["Antimatter"]))
            if item["Key"]["value"] == self.faction_ids["protectorate"]:
                self.resist_money4.SetValue(str(item["Value"]["resources"]["Money"]))
                self.resist_influence4.SetValue(str(item["Value"]["resources"]["Influence"]))
                self.resist_ops4.SetValue(str(item["Value"]["resources"]["Operations"]))
                self.resist_boost4.SetValue(str(item["Value"]["resources"]["Boost"]))
                self.resist_water4.SetValue(str(item["Value"]["resources"]["Water"]))
                self.resist_volatiles4.SetValue(str(item["Value"]["resources"]["Volatiles"]))
                self.resist_basemetals4.SetValue(str(item["Value"]["resources"]["Metals"]))
                self.resist_noblemetals4.SetValue(str(item["Value"]["resources"]["NobleMetals"]))
                self.resist_fissiles4.SetValue(str(item["Value"]["resources"]["Fissiles"]))
                self.resist_exotics4.SetValue(str(item["Value"]["resources"]["Exotics"]))
                self.resist_antimatter4.SetValue(str(item["Value"]["resources"]["Antimatter"]))
            if item["Key"]["value"] == self.faction_ids["academy"]:
                self.resist_money5.SetValue(str(item["Value"]["resources"]["Money"]))
                self.resist_influence5.SetValue(str(item["Value"]["resources"]["Influence"]))
                self.resist_ops5.SetValue(str(item["Value"]["resources"]["Operations"]))
                self.resist_boost5.SetValue(str(item["Value"]["resources"]["Boost"]))
                self.resist_water5.SetValue(str(item["Value"]["resources"]["Water"]))
                self.resist_volatiles5.SetValue(str(item["Value"]["resources"]["Volatiles"]))
                self.resist_basemetals5.SetValue(str(item["Value"]["resources"]["Metals"]))
                self.resist_noblemetals5.SetValue(str(item["Value"]["resources"]["NobleMetals"]))
                self.resist_fissiles5.SetValue(str(item["Value"]["resources"]["Fissiles"]))
                self.resist_exotics5.SetValue(str(item["Value"]["resources"]["Exotics"]))
                self.resist_antimatter5.SetValue(str(item["Value"]["resources"]["Antimatter"]))
            if item["Key"]["value"] == self.faction_ids["exodus"]:
                self.resist_money6.SetValue(str(item["Value"]["resources"]["Money"]))
                self.resist_influence6.SetValue(str(item["Value"]["resources"]["Influence"]))
                self.resist_ops6.SetValue(str(item["Value"]["resources"]["Operations"]))
                self.resist_boost6.SetValue(str(item["Value"]["resources"]["Boost"]))
                self.resist_water6.SetValue(str(item["Value"]["resources"]["Water"]))
                self.resist_volatiles6.SetValue(str(item["Value"]["resources"]["Volatiles"]))
                self.resist_basemetals6.SetValue(str(item["Value"]["resources"]["Metals"]))
                self.resist_noblemetals6.SetValue(str(item["Value"]["resources"]["NobleMetals"]))
                self.resist_fissiles6.SetValue(str(item["Value"]["resources"]["Fissiles"]))
                self.resist_exotics6.SetValue(str(item["Value"]["resources"]["Exotics"]))
                self.resist_antimatter6.SetValue(str(item["Value"]["resources"]["Antimatter"]))
    
    # Displays each faction's research projects in the UI.
    def update_projects(self):
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.faction_ids["resist"]:
                try:
                    parts = item["Value"]["currentProjectProgress"][0]["projectTemplateName"].split("_")
                    self.resist_project1.SetLabel(parts[1])
                    self.resist_project1_progress.SetValue(str(item["Value"]["currentProjectProgress"][0]["accumulatedResearch"]))
                except:
                    self.resist_project1.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][1]["projectTemplateName"].split("_")
                    self.resist_project2.SetLabel(parts[1])
                    self.resist_project2_progress.SetValue(str(item["Value"]["currentProjectProgress"][1]["accumulatedResearch"]))
                except:
                    self.resist_project2.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][2]["projectTemplateName"].split("_")
                    self.resist_project3.SetLabel(parts[1])
                    self.resist_project3_progress.SetValue(str(item["Value"]["currentProjectProgress"][2]["accumulatedResearch"]))
                except:
                    self.resist_project3.SetLabel("-None Set-")
            if item["Key"]["value"] == self.faction_ids["humanity"]:
                try:
                    parts = item["Value"]["currentProjectProgress"][0]["projectTemplateName"].split("_")
                    self.resist_project11.SetLabel(parts[1])
                    self.resist_project1_progress1.SetValue(str(item["Value"]["currentProjectProgress"][0]["accumulatedResearch"]))
                except:
                    self.resist_project11.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][1]["projectTemplateName"].split("_")
                    self.resist_project21.SetLabel(parts[1])
                    self.resist_project2_progress1.SetValue(str(item["Value"]["currentProjectProgress"][1]["accumulatedResearch"]))
                except:
                    self.resist_project21.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][2]["projectTemplateName"].split("_")
                    self.resist_project31.SetLabel(parts[1])
                    self.resist_project3_progress1.SetValue(str(item["Value"]["currentProjectProgress"][2]["accumulatedResearch"]))
                except:
                    self.resist_project31.SetLabel("-None Set-")
            if item["Key"]["value"] == self.faction_ids["initative"]:
                try:
                    parts = item["Value"]["currentProjectProgress"][0]["projectTemplateName"].split("_")
                    self.resist_project12.SetLabel(parts[1])
                    self.resist_project1_progress2.SetValue(str(item["Value"]["currentProjectProgress"][0]["accumulatedResearch"]))
                except:
                    self.resist_project12.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][1]["projectTemplateName"].split("_")
                    self.resist_project22.SetLabel(parts[1])
                    self.resist_project2_progress2.SetValue(str(item["Value"]["currentProjectProgress"][1]["accumulatedResearch"]))
                except:
                    self.resist_project22.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][2]["projectTemplateName"].split("_")
                    self.resist_project32.SetLabel(parts[1])
                    self.resist_project3_progress2.SetValue(str(item["Value"]["currentProjectProgress"][2]["accumulatedResearch"]))
                except:
                    self.resist_project31.SetLabel("-None Set-")
            if item["Key"]["value"] == self.faction_ids["servants"]:
                try:
                    parts = item["Value"]["currentProjectProgress"][0]["projectTemplateName"].split("_")
                    self.resist_project13.SetLabel(parts[1])
                    self.resist_project1_progress3.SetValue(str(item["Value"]["currentProjectProgress"][0]["accumulatedResearch"]))
                except:
                    self.resist_project13.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][1]["projectTemplateName"].split("_")
                    self.resist_project23.SetLabel(parts[1])
                    self.resist_project2_progress3.SetValue(str(item["Value"]["currentProjectProgress"][1]["accumulatedResearch"]))
                except:
                    self.resist_project23.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][2]["projectTemplateName"].split("_")
                    self.resist_project33.SetLabel(parts[1])
                    self.resist_project3_progress3.SetValue(str(item["Value"]["currentProjectProgress"][2]["accumulatedResearch"]))
                except:
                    self.resist_project33.SetLabel("-None Set-")
            if item["Key"]["value"] == self.faction_ids["protectorate"]:
                try:
                    parts = item["Value"]["currentProjectProgress"][0]["projectTemplateName"].split("_")
                    self.resist_project14.SetLabel(parts[1])
                    self.resist_project1_progress4.SetValue(str(item["Value"]["currentProjectProgress"][0]["accumulatedResearch"]))
                except:
                    self.resist_project14.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][1]["projectTemplateName"].split("_")
                    self.resist_project24.SetLabel(parts[1])
                    self.resist_project2_progress4.SetValue(str(item["Value"]["currentProjectProgress"][1]["accumulatedResearch"]))
                except:
                    self.resist_project24.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][2]["projectTemplateName"].split("_")
                    self.resist_project34.SetLabel(parts[1])
                    self.resist_project3_progress4.SetValue(str(item["Value"]["currentProjectProgress"][2]["accumulatedResearch"]))
                except:
                    self.resist_project34.SetLabel("-None Set-")
            if item["Key"]["value"] == self.faction_ids["academy"]:
                try:
                    parts = item["Value"]["currentProjectProgress"][0]["projectTemplateName"].split("_")
                    self.resist_project15.SetLabel(parts[1])
                    self.resist_project1_progress5.SetValue(str(item["Value"]["currentProjectProgress"][0]["accumulatedResearch"]))
                except:
                    self.resist_project15.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][1]["projectTemplateName"].split("_")
                    self.resist_project25.SetLabel(parts[1])
                    self.resist_project2_progress5.SetValue(str(item["Value"]["currentProjectProgress"][1]["accumulatedResearch"]))
                except:
                    self.resist_project25.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][2]["projectTemplateName"].split("_")
                    self.resist_project35.SetLabel(parts[1])
                    self.resist_project3_progress5.SetValue(str(item["Value"]["currentProjectProgress"][2]["accumulatedResearch"]))
                except:
                    self.resist_project35.SetLabel("-None Set-")
            if item["Key"]["value"] == self.faction_ids["exodus"]:
                try:
                    parts = item["Value"]["currentProjectProgress"][0]["projectTemplateName"].split("_")
                    self.resist_project16.SetLabel(parts[1])
                    self.resist_project1_progress6.SetValue(str(item["Value"]["currentProjectProgress"][0]["accumulatedResearch"]))
                except:
                    self.resist_project16.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][1]["projectTemplateName"].split("_")
                    self.resist_project26.SetLabel(parts[1])
                    self.resist_project2_progress6.SetValue(str(item["Value"]["currentProjectProgress"][1]["accumulatedResearch"]))
                except:
                    self.resist_project26.SetLabel("-None Set-")
                try:
                    parts = item["Value"]["currentProjectProgress"][2]["projectTemplateName"].split("_")
                    self.resist_project36.SetLabel(parts[1])
                    self.resist_project3_progress6.SetValue(str(item["Value"]["currentProjectProgress"][2]["accumulatedResearch"]))
                except:
                    self.resist_project36.SetLabel("-None Set-")
    
    # Shows the available, completed, and missed projects.
    def show_project_extras(self):
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                self.c_projects.Set(item["Value"]["finishedProjectNames"])
                self.m_projects.Set(item["Value"]["missedProjects"])
                
                possible_projects = []
                for entry in item["Value"]["activeProjectTriggers"]:
                    possible_projects.append(entry["projectTemplateName"])
                    
                display_a_projects = item["Value"]["availableProjectNames"] + possible_projects
                
                self.a_projects.Set(display_a_projects)
                
    # Updates the global research section of the UI.
    def update_global_research(self):
        try:
            slot1_index = game_data.tech_list.index(self.global_research[0]["techTemplateName"])
            self.research_slot1.SetSelection(slot1_index)
            self.research1_progress.SetValue(str(self.global_research[0]["accumulatedResearch"]))
        except:
            print("Error: Could not find " + self.global_research[0]["techTemplateName"] + " in game data.")
        try:
            slot2_index = game_data.tech_list.index(self.global_research[1]["techTemplateName"])
            self.research_slot2.SetSelection(slot2_index)
            self.research2_progress.SetValue(str(self.global_research[1]["accumulatedResearch"]))
        except:
            print("Error: Could not find " + self.global_research[1]["techTemplateName"] + " in game data.")
        try:
            slot3_index = game_data.tech_list.index(self.global_research[2]["techTemplateName"])
            self.research_slot3.SetSelection(slot3_index)
            self.research3_progress.SetValue(str(self.global_research[2]["accumulatedResearch"]))
        except:
            print("Error: Could not find " + self.global_research[2]["techTemplateName"] + " in game data.")
        
    # The three functions handle changing the global research.
    def change_research_1(self, event):
        self.global_research[0]["techTemplateName"] = event.GetString()
    
    def change_research_2(self, event):
        self.global_research[1]["techTemplateName"] = event.GetString()
    
    def change_research_3(self, event):
        self.global_research[2]["techTemplateName"] = event.GetString()
    
    # These three functions handle changing global research progress.
    def update_research_1(self, event):
        new_value = self.research1_progress.GetValue()
        try:
            number = float(new_value)
            self.global_research[0]["accumulatedResearch"] = number
        except:
            try:
                self.research1_progress.SetValue(str(self.global_research[0]["accumulatedResearch"]))
            except:
                self.research1_progress.SetValue("")
    
    def update_research_2(self, event):
        new_value = self.research2_progress.GetValue()
        try:
            number = float(new_value)
            self.global_research[1]["accumulatedResearch"] = number
        except:
            try:
                self.research2_progress.SetValue(str(self.global_research[1]["accumulatedResearch"]))
            except:
                self.research2_progress.SetValue("")
    
    def update_research_3(self, event):
        new_value = self.research3_progress.GetValue()
        try:
            number = float(new_value)
            self.global_research[2]["accumulatedResearch"] = number
        except:
            try:
                self.research3_progress.SetValue(str(self.global_research[2]["accumulatedResearch"]))
            except:
                self.research3_progress.SetValue("")
    
    # Handles changing which faction is controled by the player per the checkboxes.
    def player_checkbox(self, event):
        caller = event.GetEventObject()
        
        if event.IsChecked():
            # Uncheck all boxes.
            for checkbox in self.player_checkboxes:
                checkbox.SetValue(False)
            
            # Make the callling box checked again.
            caller.SetValue(True)
            
            # Make the currently selected faction the player faction.
            for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIPlayerState"]:
                if item["Value"]["faction"]["value"] == self.get_active_faction_id():
                    item["Value"]["isAI"] = False
                else:
                    item["Value"]["isAI"] = True
        else:
            # Don't allow people to uncheck the box for the currently active faction.
            caller.SetValue(True)
    
    # These three functions handle changing faction research projects.
    def update_project_1(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["currentProjectProgress"][0]["accumulatedResearch"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["currentProjectProgress"][0]["accumulatedResearch"]))
                    except:
                        caller.SetValue("")
    
    def update_project_2(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["currentProjectProgress"][1]["accumulatedResearch"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["currentProjectProgress"][1]["accumulatedResearch"]))
                    except:
                        caller.SetValue("")
    
    def update_project_3(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["currentProjectProgress"][2]["accumulatedResearch"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["currentProjectProgress"][2]["accumulatedResearch"]))
                    except:
                        caller.SetValue("")
    
    # This batch of functions handles changing faction resources.
    def update_money(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Money"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Money"]))
                    except:
                        caller.SetValue("")
    
    def update_influence(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Influence"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Influence"]))
                    except:
                        caller.SetValue("")
                        
    def update_ops(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Operations"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Operations"]))
                    except:
                        caller.SetValue("")
    
    def update_boost(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Boost"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Boost"]))
                    except:
                        caller.SetValue("")
    
    def update_water(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Water"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Water"]))
                    except:
                        caller.SetValue("")
    
    def update_volatiles(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Volatiles"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Volatiles"]))
                    except:
                        caller.SetValue("")
    
    def update_metals(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Metals"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Metals"]))
                    except:
                        caller.SetValue("")
    
    def update_noblemetals(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["NobleMetals"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["NobleMetals"]))
                    except:
                        caller.SetValue("")
    
    def update_fissiles(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Fissiles"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Fissiles"]))
                    except:
                        caller.SetValue("")
    
    def update_exotics(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Exotics"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Exotics"]))
                    except:
                        caller.SetValue("")
    
    def update_antimatter(self, event):
        caller = event.GetEventObject()
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                try:
                    number = float(caller.GetValue())
                    item["Value"]["resources"]["Antimatter"] = number
                except:
                    try:
                        caller.SetValue(str(item["Value"]["resources"]["Antimatter"]))
                    except:
                        caller.SetValue("")
    
    # Manages process of diaplying counilor data in the UI.
    def update_councilors(self):
        for fname, fid in self.faction_ids.items():
            x = 0
            for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
                try:
                    if item["Value"]["faction"]["value"] == fid:
                        self.display_councilor(item, fname, x)
                        self.councilors[str(fid)].append(item["Value"]["ID"]["value"])
                        x = x + 1
                except:
                    continue
    
    # Handles the changing of councilor professions.
    def change_councilor_job(self, event):
        parts = self.sub_page.split()
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:               
                    item["Value"]["typeTemplateName"] = event.GetString()
            except:
                continue
    
    # The next batch of functions handles changing councilor attributes.
    def change_councilor_persuasion(self, event):
        caller = event.GetEventObject()
        try:
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:               
                    try:
                        number = int(caller.GetValue())
                        item["Value"]["attributes"]["Persuasion"] = number
                    except:
                        try:
                            caller.SetValue(str(item["Value"]["attributes"]["Persuasion"]))
                        except:
                            caller.SetValue("")
            except:
                continue
    
    def change_councilor_investigation(self, event):
        caller = event.GetEventObject()
        try:
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:               
                    try:
                        number = int(caller.GetValue())
                        item["Value"]["attributes"]["Investigation"] = number
                    except:
                        try:
                            caller.SetValue(str(item["Value"]["attributes"]["Investigation"]))
                        except:
                            caller.SetValue("")
            except:
                continue
    
    def change_councilor_espionage(self, event):
        caller = event.GetEventObject()
        try:
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:               
                    try:
                        number = int(caller.GetValue())
                        item["Value"]["attributes"]["Espionage"] = number
                    except:
                        try:
                            caller.SetValue(str(item["Value"]["attributes"]["Espionage"]))
                        except:
                            caller.SetValue("")
            except:
                continue
    
    def change_councilor_command(self, event):
        caller = event.GetEventObject()
        try:
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:               
                    try:
                        number = int(caller.GetValue())
                        item["Value"]["attributes"]["Command"] = number
                    except:
                        try:
                            caller.SetValue(str(item["Value"]["attributes"]["Command"]))
                        except:
                            caller.SetValue("")
            except:
                continue
                
    def change_councilor_administration(self, event):
        caller = event.GetEventObject()
        try:
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:               
                    try:
                        number = int(caller.GetValue())
                        item["Value"]["attributes"]["Administration"] = number
                    except:
                        try:
                            caller.SetValue(str(item["Value"]["attributes"]["Administration"]))
                        except:
                            caller.SetValue("")
            except:
                continue
    
    def change_councilor_science(self, event):
        caller = event.GetEventObject()
        try:
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:               
                    try:
                        number = int(caller.GetValue())
                        item["Value"]["attributes"]["Science"] = number
                    except:
                        try:
                            caller.SetValue(str(item["Value"]["attributes"]["Science"]))
                        except:
                            caller.SetValue("")
            except:
                continue
    
    def change_councilor_security(self, event):
        caller = event.GetEventObject()
        try:
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:               
                    try:
                        number = int(caller.GetValue())
                        item["Value"]["attributes"]["Security"] = number
                    except:
                        try:
                            caller.SetValue(str(item["Value"]["attributes"]["Security"]))
                        except:
                            caller.SetValue("")
            except:
                continue
                
    def change_councilor_loyalty(self, event):
        caller = event.GetEventObject()
        try:
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:               
                    try:
                        number = int(caller.GetValue())
                        item["Value"]["attributes"]["Loyalty"] = number
                    except:
                        try:
                            caller.SetValue(str(item["Value"]["attributes"]["Loyalty"]))
                        except:
                            caller.SetValue("")
            except:
                continue
    
    # Displays the age and traits of the currently selected councilor.
    def show_councilor_extras(self):
        try:
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:
                    birthday = self.make_date_object(item["Value"]["dateBorn"])
                    age_delta = self.game_date - birthday
                    age = int(age_delta.days / 365)
                    self.c_age.SetValue(age)
                    
                    active_traits = []
                    non_active_traits = []
                    
                    for trait in game_data.traits:
                        if trait in item["Value"]["traitTemplateNames"]:
                            active_traits.append(trait)
                        else:
                            non_active_traits.append(trait)

                    self.m_listBox1.Set(active_traits)
                    self.m_listBox2.Set(non_active_traits)
            except:
                continue
    
    # Adds a trait to a councilor.
    def add_trait(self, event):
        try:
            selection = self.m_listBox2.GetString(self.m_listBox2.GetSelection())
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:
                    item["Value"]["traitTemplateNames"].append(selection)
                    self.show_councilor_extras()
            except:
                continue
                
    # Removes a trait from a councilor.
    def remove_trait(self, event):
        try:
            selection = self.m_listBox1.GetString(self.m_listBox1.GetSelection())
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:
                    item["Value"]["traitTemplateNames"].remove(selection)
                    self.show_councilor_extras()        
            except:
                continue
    
    # Displays counilor data in the IU. Called in a sequantial manner by update_councilors.
    def display_councilor(self, councilor, faction, slot):
        if faction == "resist":
            if slot == 0:
                self.resist_c_fname.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class.SetSelection(job_index)
                self.resist_c_persuasion.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 1:
                self.resist_c_fname1.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname1.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class1.SetSelection(job_index)
                self.resist_c_persuasion1.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation1.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage1.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command1.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration1.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science1.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security1.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty1.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 2:
                self.resist_c_fname2.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname2.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class2.SetSelection(job_index)
                self.resist_c_persuasion2.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation2.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage2.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command2.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration2.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science2.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security2.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty2.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 3:
                self.resist_c_fname3.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname3.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class3.SetSelection(job_index)
                self.resist_c_persuasion3.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation3.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage3.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command3.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration3.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science3.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security3.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty3.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 4:
                self.resist_c_fname4.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname4.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class4.SetSelection(job_index)
                self.resist_c_persuasion4.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation4.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage4.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command4.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration4.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science4.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security4.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty4.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 5:
                self.resist_c_fname5.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname5.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class5.SetSelection(job_index)
                self.resist_c_persuasion5.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation5.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage5.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command5.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration5.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science5.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security5.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty5.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
        if faction == "humanity":
            if slot == 0:
                self.resist_c_fname6.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname6.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class6.SetSelection(job_index)
                self.resist_c_persuasion6.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation6.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage6.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command6.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration6.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science6.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security6.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty6.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 1:
                self.resist_c_fname11.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname11.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class11.SetSelection(job_index)
                self.resist_c_persuasion11.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation11.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage11.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command11.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration11.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science11.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security11.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty11.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 2:
                self.resist_c_fname21.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname21.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class21.SetSelection(job_index)
                self.resist_c_persuasion21.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation21.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage21.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command21.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration21.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science21.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security21.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty21.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 3:
                self.resist_c_fname31.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname31.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class31.SetSelection(job_index)
                self.resist_c_persuasion31.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation31.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage31.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command31.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration31.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science31.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security31.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty31.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 4:
                self.resist_c_fname41.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname41.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class41.SetSelection(job_index)
                self.resist_c_persuasion41.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation41.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage41.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command41.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration41.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science41.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security41.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty41.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 5:
                self.resist_c_fname51.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname51.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class51.SetSelection(job_index)
                self.resist_c_persuasion51.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation51.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage51.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command51.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration51.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science51.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security51.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty51.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
        if faction == "initative":
            if slot == 0:
                self.resist_c_fname7.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname7.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class7.SetSelection(job_index)
                self.resist_c_persuasion7.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation7.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage7.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command7.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration7.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science7.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security7.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty7.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 1:
                self.resist_c_fname12.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname12.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class12.SetSelection(job_index)
                self.resist_c_persuasion12.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation12.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage12.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command12.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration12.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science12.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security12.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty12.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 2:
                self.resist_c_fname22.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname22.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class22.SetSelection(job_index)
                self.resist_c_persuasion22.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation22.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage22.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command22.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration22.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science22.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security22.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty22.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 3:
                self.resist_c_fname32.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname32.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class32.SetSelection(job_index)
                self.resist_c_persuasion32.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation32.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage32.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command32.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration32.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science32.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security32.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty32.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 4:
                self.resist_c_fname42.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname42.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class42.SetSelection(job_index)
                self.resist_c_persuasion42.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation42.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage42.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command42.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration42.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science42.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security42.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty42.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 5:
                self.resist_c_fname52.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname52.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class52.SetSelection(job_index)
                self.resist_c_persuasion52.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation52.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage52.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command52.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration52.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science52.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security52.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty52.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
        if faction == "servants":
            if slot == 0:
                self.resist_c_fname8.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname8.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class8.SetSelection(job_index)
                self.resist_c_persuasion8.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation8.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage8.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command8.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration8.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science8.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security8.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty8.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 1:
                self.resist_c_fname13.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname13.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class13.SetSelection(job_index)
                self.resist_c_persuasion13.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation13.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage13.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command13.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration13.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science13.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security13.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty13.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 2:
                self.resist_c_fname23.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname23.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class23.SetSelection(job_index)
                self.resist_c_persuasion23.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation23.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage23.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command23.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration23.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science23.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security23.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty23.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 3:
                self.resist_c_fname33.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname33.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class33.SetSelection(job_index)
                self.resist_c_persuasion33.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation33.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage33.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command33.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration33.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science33.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security33.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty33.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 4:
                self.resist_c_fname43.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname43.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class43.SetSelection(job_index)
                self.resist_c_persuasion43.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation43.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage43.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command43.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration43.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science43.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security43.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty43.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 5:
                self.resist_c_fname53.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname53.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class53.SetSelection(job_index)
                self.resist_c_persuasion53.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation53.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage53.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command53.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration53.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science53.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security53.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty53.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
        if faction == "protectorate":
            if slot == 0:
                self.resist_c_fname9.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname9.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class9.SetSelection(job_index)
                self.resist_c_persuasion9.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation9.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage9.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command9.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration9.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science9.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security9.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty9.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 1:
                self.resist_c_fname14.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname14.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class14.SetSelection(job_index)
                self.resist_c_persuasion14.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation14.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage14.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command14.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration14.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science14.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security14.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty14.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 2:
                self.resist_c_fname24.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname24.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class24.SetSelection(job_index)
                self.resist_c_persuasion24.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation24.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage24.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command24.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration24.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science24.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security24.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty24.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 3:
                self.resist_c_fname34.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname34.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class34.SetSelection(job_index)
                self.resist_c_persuasion34.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation34.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage34.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command34.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration34.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science34.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security34.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty34.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 4:
                self.resist_c_fname44.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname44.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class44.SetSelection(job_index)
                self.resist_c_persuasion44.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation44.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage44.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command44.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration44.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science44.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security44.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty44.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 5:
                self.resist_c_fname54.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname54.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class54.SetSelection(job_index)
                self.resist_c_persuasion54.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation54.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage54.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command54.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration54.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science54.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security54.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty54.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
        if faction == "academy":
            if slot == 0:
                self.resist_c_fname10.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname10.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class10.SetSelection(job_index)
                self.resist_c_persuasion10.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation10.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage10.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command10.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration10.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science10.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security10.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty10.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 1:
                self.resist_c_fname15.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname15.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class15.SetSelection(job_index)
                self.resist_c_persuasion15.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation15.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage15.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command15.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration15.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science15.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security15.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty15.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 2:
                self.resist_c_fname25.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname25.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class25.SetSelection(job_index)
                self.resist_c_persuasion25.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation25.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage25.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command25.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration25.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science25.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security25.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty25.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 3:
                self.resist_c_fname35.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname35.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class35.SetSelection(job_index)
                self.resist_c_persuasion35.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation35.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage35.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command35.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration35.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science35.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security35.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty35.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 4:
                self.resist_c_fname45.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname45.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class45.SetSelection(job_index)
                self.resist_c_persuasion45.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation45.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage45.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command45.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration45.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science45.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security45.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty45.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 5:
                self.resist_c_fname55.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname55.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class55.SetSelection(job_index)
                self.resist_c_persuasion55.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation55.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage55.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command55.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration55.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science55.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security55.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty55.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
        if faction == "exodus":
            if slot == 0:
                self.resist_c_fname16.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname16.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class16.SetSelection(job_index)
                self.resist_c_persuasion16.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation16.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage16.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command16.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration16.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science16.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security16.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty16.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 1:
                self.resist_c_fname17.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname17.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class17.SetSelection(job_index)
                self.resist_c_persuasion17.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation17.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage17.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command17.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration17.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science17.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security17.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty17.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 2:
                self.resist_c_fname26.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname26.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class26.SetSelection(job_index)
                self.resist_c_persuasion26.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation26.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage26.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command26.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration26.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science26.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security26.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty26.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 3:
                self.resist_c_fname36.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname36.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class36.SetSelection(job_index)
                self.resist_c_persuasion36.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation36.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage36.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command36.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration36.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science36.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security36.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty36.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 4:
                self.resist_c_fname46.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname46.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class46.SetSelection(job_index)
                self.resist_c_persuasion46.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation46.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage46.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command46.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration46.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science46.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security46.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty46.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
            if slot == 5:
                self.resist_c_fname56.SetLabel(councilor["Value"]["personalName"])
                self.resist_c_lname56.SetLabel(councilor["Value"]["familyName"])
                job_index = game_data.jobs.index(councilor["Value"]["typeTemplateName"])
                self.resist_c_class56.SetSelection(job_index)
                self.resist_c_persuasion56.SetValue(str(councilor["Value"]["attributes"]["Persuasion"]))
                self.resist_c_investigation56.SetValue(str(councilor["Value"]["attributes"]["Investigation"]))
                self.resist_c_espionage56.SetValue(str(councilor["Value"]["attributes"]["Espionage"]))
                self.resist_c_command56.SetValue(str(councilor["Value"]["attributes"]["Command"]))
                self.resist_c_administration56.SetValue(str(councilor["Value"]["attributes"]["Administration"]))
                self.resist_c_science56.SetValue(str(councilor["Value"]["attributes"]["Science"]))
                self.resist_c_security56.SetValue(str(councilor["Value"]["attributes"]["Security"]))
                self.resist_c_loyalty56.SetValue(str(councilor["Value"]["attributes"]["Loyalty"]))
    
    # Changes a councilor's age.
    def change_age(self, event):
        try:
            new_age = self.c_age.GetValue()
            parts = self.sub_page.split()
        except:
            return
        index = int(parts[1])
        
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"]:
            try:
                if item["Value"]["ID"]["value"] == self.councilors[str(self.get_active_faction_id())][index]:
                    new_birthday = self.game_date - relativedelta(years=new_age)
                    item["Value"]["dateBorn"]["year"] = int(new_birthday.strftime("%Y"))
                    self.show_councilor_extras()
            except:
                continue
    
    # Changes how much hate a faction has with the aliens.
    def change_hate(self, event):
        new_hate = event.GetEventObject().GetValue()
        for item in self.aliens["Value"]["factionHate"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                item["Value"] = float(new_hate)
    
    # Makes a project no longer complete.
    def undo_project(self, event):
        selection = self.c_projects.GetString(self.c_projects.GetSelection())
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                item["Value"]["finishedProjectNames"].remove(selection)
                item["Value"]["availableProjectNames"].append(selection)
                self.show_project_extras()
                
    # Completes a project.
    def complete_project(self, event):
        selection = self.a_projects.GetString(self.a_projects.GetSelection())
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                self.remove_from_available_projects(item, selection)
                item["Value"]["finishedProjectNames"].append(selection)
                self.show_project_extras()
    
    # Unlocks a missed project.
    def unlock_project(self, event):
        selection = self.m_projects.GetString(self.m_projects.GetSelection())
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                item["Value"]["missedProjects"].remove(selection)
                item["Value"]["availableProjectNames"].append(selection)
                self.show_project_extras()
    
    # Locks an available project.
    def lock_project(self, event):
        selection = self.a_projects.GetString(self.a_projects.GetSelection())
        for item in self.data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"]:
            if item["Key"]["value"] == self.get_active_faction_id():
                self.remove_from_available_projects(item, selection)
                item["Value"]["missedProjects"].append(selection)
                self.show_project_extras()
    
    # Handles the fact that "available" projects counts both unlocked projects and projects that are still trying to unlock.
    def remove_from_available_projects(self, faction, project):
        try:
            faction["Value"]["availableProjectNames"].remove(project)
        except:
            pass
        try:
            x = 0
            found = False
            for item in faction["Value"]["activeProjectTriggers"]:
                if project == item["projectTemplateName"]:
                    found = True
                    break
                else:
                    x = x + 1
            if found:
                del faction["Value"]["activeProjectTriggers"][x]
        except:
            pass
    
    # Displays the about dialog.
    def about_box(self, event):
        
        message = """
                    Terra Invicta Save Editor v0.4.3
                    
                    Copyright (C) 2022 George Markeloff
                    
                    Distributed under the terms of the GNU General Public License v3.
                    See LICENSE.txt or https://www.gnu.org/licenses/gpl-3.0.html for license details.
                    
                    This program is not associated with Hooded Horse or Pavonis Interactive.
                    You are strongly encouraged to back up your save file before modifying it.
                    """
        
        wx.MessageBox(message, "About" ,wx.OK | wx.ICON_INFORMATION)  
    
    # Closes the program.
    def on_quit(self, event):
        self.Close()
        
# Make a wx app.
app = wx.App(False)
# Make an instance of our class and display it. 
frame = ti_save_editor(None)
frame.Show(True)
# Start the GUI IO loop.
app.MainLoop()
