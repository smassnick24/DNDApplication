import tkinter as tk
import customtkinter as ctk
from CreateCharacterClass import CharacterCreator

class StatEntryFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # allowing the new frame to have a CTk obj as a master
        self.master = master
        # declaring fonts
        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.special_font = ctk.CTkFont(family="Rockwell", size=18)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)
        # labels
        self.NameLabel = ctk.CTkLabel(self, font=self.font, text="Character Name")
        self.ClassLabel = ctk.CTkLabel(self, font=self.font, text="Class")
        self.LevelLabel = ctk.CTkLabel(self, font=self.font, text="Level")
        self.RaceLabel = ctk.CTkLabel(self, font=self.font, text="Race")
        self.BackgroundLabel = ctk.CTkLabel(self, font=self.font, text="Background")
        self.AlignmentLabel = ctk.CTkLabel(self, font=self.font, text="Alignment")
        self.PersonalityLabel = ctk.CTkLabel(self, font=self.font, text="Personality")
        self.IdealsLabel = ctk.CTkLabel(self, font=self.font, text="Ideals")
        self.BondsLabel = ctk.CTkLabel(self, font=self.font, text="Bonds")
        self.FlawsLabel = ctk.CTkLabel(self, font=self.font, text="Flaws")
        self.FeaturesLabel = ctk.CTkLabel(self, font=self.font, text="Features")
        self.TraitsLabel = ctk.CTkLabel(self, font=self.font, text="Traits")
        self.Attack1Label = ctk.CTkLabel(self, font=self.font, text="Attack 1")
        self.Attack2Label = ctk.CTkLabel(self, font=self.font, text="Attack 2")
        self.Attack3Label = ctk.CTkLabel(self, font=self.font, text="Attack 3")
        self.STRLabel = ctk.CTkLabel(self, font=self.font, text="STR")
        self.STRBonusLabel = ctk.CTkLabel(self, font=self.font, text="")
        self.DEXLabel = ctk.CTkLabel(self, font=self.font, text="STR")
        self.DEXBonusLabel = ctk.CTkLabel(self, font=self.font, text="")
        self.CONLabel = ctk.CTkLabel(self, font=self.font, text="STR")
        self.CONBonusLabel = ctk.CTkLabel(self, font=self.font, text="")
        self.INTLabel = ctk.CTkLabel(self, font=self.font, text="STR")
        self.INTBonusLabel = ctk.CTkLabel(self, font=self.font, text="")
        self.WISLabel = ctk.CTkLabel(self, font=self.font, text="STR")
        self.WISBonusLabel = ctk.CTkLabel(self, font=self.font, text="")
        self.CHALabel = ctk.CTkLabel(self, font=self.font, text="STR")
        self.CHABonusLabel = ctk.CTkLabel(self, font=self.font, text="")
        self.ACLabel = ctk.CTkLabel(self, font=self.font, text="Armor Class")
        self.SpeedLabel = ctk.CTkLabel(self, font=self.font, text="Speed")
        self.ProfBonusLabel = ctk.CTkLabel(self, font=self.font, text="Proficiency Bonus")
        self.HPMAXLabel = ctk.CTkLabel(self, font=self.font, text="Maximum HP")
        self.HPCURRLabel = ctk.CTkLabel(self, font=self.font, text="Current HP")
        self.HPTEMPLabel = ctk.CTkLabel(self, font=self.font, text="Temporary HP")
        self.HDTOTLabel = ctk.CTkLabel(self, font=self.font, text="Total Hit Dice")
        self.HDCURRLabel = ctk.CTkLabel(self, font=self.font, text="Current Hit Dice")
        self.ElectrumLabel = ctk.CTkLabel(self, font=self.font, text="EP")
        self.SilverLabel = ctk.CTkLabel(self, font=self.font, text="SP")
        self.GoldLabel = ctk.CTkLabel(self, font=self.font, text="GP")
        self.PlatinumLabel = ctk.CTkLabel(self, font=self.font, text="PP")
        self.CopperLabel = ctk.CTkLabel(self, font=self.font, text="CP")