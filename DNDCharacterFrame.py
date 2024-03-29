import tkinter as tk
import customtkinter as ctk
from CharacterDataHandler import DataHandler

ctk.set_appearance_mode("Dark")


class DNDCharacterFrame(ctk.CTkScrollableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # defining character creator
        self.CC = DataHandler()

        # declaring fonts
        self.small_font = ctk.CTkFont(family="Rockwell", size=10)
        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.bold_font = ctk.CTkFont(family="Rockwell", size=14, weight="bold")
        self.special_font = ctk.CTkFont(family="Rockwell", size=18)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)

        self.stat_keys = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

        # creating container frames or "divs"
        self.stat_div = ctk.CTkFrame(self, border_width=1, border_color="black")
        self.attr_div = ctk.CTkFrame(self, border_width=1, border_color="black")
        self.aux_attr_div = ctk.CTkFrame(self, border_width=1, border_color="black")
        self.traits_div = ctk.CTkFrame(self, border_width=1, border_color="black")
        self.health_div = ctk.CTkFrame(self, border_width=1, border_color="black")
        self.attacks_div = ctk.CTkFrame(self, border_width=1, border_color="black")
        self.inner_attacks_div = ctk.CTkFrame(self.attacks_div, border_width=1, border_color="black")
        self.equipment_div = ctk.CTkFrame(self.attacks_div, border_width=1, border_color="black")
        self.saving_throws_div = ctk.CTkFrame(self, border_width=1, border_color="black")
        self.death_save_div = ctk.CTkFrame(self.health_div, border_width=1, border_color="black")

        # spell divs
        self.master_spell_div = ctk.CTkFrame(self, border_width=1, border_color="black")
        self.cantrips_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="red")
        self.first_level_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="green")
        self.second_level_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="blue")
        self.third_level_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="orange")
        self.fourth_level_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="cyan")
        self.fifth_level_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="indigo")
        self.sixth_level_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="violet")
        self.seventh_level_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="purple")
        self.eighth_level_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="pink")
        self.ninth_level_div = ctk.CTkFrame(self.master_spell_div, border_width=0, border_color="brown")

        # variables
        # kinter variables
        self.NameVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Character_Name"])
        self.ClassVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Class"])
        self.LevelVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Level"])
        self.RaceVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Race"])
        self.BackgroundVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Background"])
        self.AlignmentVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Alignment"])
        self.ExperienceVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Experience"])
        self.EquipmentVar = ctk.StringVar(value=self.CC.fields["Attacks"]["Equipment"])
        self.Attack1Var = ctk.StringVar(value=self.CC.fields["Attacks"]["Attack_1"])
        self.Attack2Var = ctk.StringVar(value=self.CC.fields["Attacks"]["Attack_2"])
        self.Attack3Var = ctk.StringVar(value=self.CC.fields["Attacks"]["Attack_3"])
        self.Attack1Bonus = ctk.StringVar(value=self.CC.fields["Attacks"]["Attack_1_Bonus"])
        self.Attack2Bonus = ctk.StringVar(value=self.CC.fields["Attacks"]["Attack_2_Bonus"])
        self.Attack3Bonus = ctk.StringVar(value=self.CC.fields["Attacks"]["Attack_3_Bonus"])
        self.Attack1Type = ctk.StringVar(value=self.CC.fields["Attacks"]["Attack_1_Type"])
        self.Attack2Type = ctk.StringVar(value=self.CC.fields["Attacks"]["Attack_2_Type"])
        self.Attack3Type = ctk.StringVar(value=self.CC.fields["Attacks"]["Attack_3_Type"])
        self.STRVar = ctk.StringVar(value=self.CC.fields["Stats"]["STR"])
        self.CONVar = ctk.StringVar(value=self.CC.fields["Stats"]["CON"])
        self.DEXVar = ctk.StringVar(value=self.CC.fields["Stats"]["DEX"])
        self.INTVar = ctk.StringVar(value=self.CC.fields["Stats"]["INT"])
        self.WISVar = ctk.StringVar(value=self.CC.fields["Stats"]["WIS"])
        self.CHAVar = ctk.StringVar(value=self.CC.fields["Stats"]["CHA"])
        self.PassivePVar = ctk.StringVar(value=self.CC.fields["Auxiliary"]["Passive_Perception"])
        self.ACVar = ctk.StringVar(value=self.CC.fields["Auxiliary"]["AC"])
        self.InitVar = ctk.StringVar(value=self.CC.fields["Auxiliary"]["Init"])
        self.SpeedVar = ctk.StringVar(value=self.CC.fields["Auxiliary"]["Speed"])
        self.ProfBonusVar = ctk.StringVar(value=self.CC.fields["Auxiliary"]["Prof_Bonus"])
        self.HPMaxVar = ctk.StringVar(value=self.CC.fields["HitPoints"]["HP_Max"])
        self.HPCurrVar = ctk.StringVar(value=self.CC.fields["HitPoints"]["HP_Curr"])
        self.HPTempVar = ctk.StringVar(value=self.CC.fields["HitPoints"]["HP_Temp"])
        self.HDTotVar = ctk.StringVar(value=self.CC.fields["HitDice"]["HD_Total"])
        self.HDCurrVar = ctk.StringVar(value=self.CC.fields["HitDice"]["HD_Curr"])
        self.ElecVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Electrum"])
        self.PlatVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Platinum"])
        self.GoldVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Gold"])
        self.SilvVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Silver"])
        self.CoppVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Copper"])
        self.Str_St_Var = ctk.StringVar()
        self.Dex_St_Var = ctk.StringVar()
        self.Con_St_Var = ctk.StringVar()
        self.Int_St_Var = ctk.StringVar()
        self.Wis_St_Var = ctk.StringVar()
        self.Cha_St_Var = ctk.StringVar()

        # spell vars
        self.SpellSlots = ctk.StringVar(value=self.CC.fields['Spells']['Spell_Slots'])

        self.CantripContainer = {"0": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_0']),
                                 "1": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_1']),
                                 "2": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_2']),
                                 "3": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_3']),
                                 "4": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_4']),
                                 "5": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_5']),
                                 "6": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_6']),
                                 "7": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_7']),
                                 "8": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_8']),
                                 "9": ctk.StringVar(value=self.CC.fields['Spells']['Cantrips']['Cantrip_Slot_9'])}

        self.FirstLevelContainer = {"0": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_0']),
                                    "1": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_1']),
                                    "2": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_2']),
                                    "3": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_3']),
                                    "4": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_4']),
                                    "5": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_5']),
                                    "6": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_6']),
                                    "7": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_7']),
                                    "8": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_8']),
                                    "9": ctk.StringVar(value=self.CC.fields['Spells']['First_Level']['Spell_Slot_9'])}

        self.SecondLevelContainer = {"0": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_0']),
                                     "1": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_1']),
                                     "2": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_2']),
                                     "3": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_3']),
                                     "4": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_4']),
                                     "5": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_5']),
                                     "6": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_6']),
                                     "7": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_7']),
                                     "8": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_8']),
                                     "9": ctk.StringVar(value=self.CC.fields['Spells']['Second_Level']['Spell_Slot_9'])}

        self.ThirdLevelContainer = {"0": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_0']),
                                    "1": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_1']),
                                    "2": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_2']),
                                    "3": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_3']),
                                    "4": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_4']),
                                    "5": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_5']),
                                    "6": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_6']),
                                    "7": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_7']),
                                    "8": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_8']),
                                    "9": ctk.StringVar(value=self.CC.fields['Spells']['Third_Level']['Spell_Slot_9'])}

        self.FourthLevelContainer = {"0": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_0']),
                                     "1": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_1']),
                                     "2": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_2']),
                                     "3": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_3']),
                                     "4": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_4']),
                                     "5": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_5']),
                                     "6": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_6']),
                                     "7": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_7']),
                                     "8": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_8']),
                                     "9": ctk.StringVar(value=self.CC.fields['Spells']['Fourth_Level']['Spell_Slot_9'])}

        self.FifthLevelContainer = {"0": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_0']),
                                    "1": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_1']),
                                    "2": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_2']),
                                    "3": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_3']),
                                    "4": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_4']),
                                    "5": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_5']),
                                    "6": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_6']),
                                    "7": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_7']),
                                    "8": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_8']),
                                    "9": ctk.StringVar(value=self.CC.fields['Spells']['Fifth_Level']['Spell_Slot_9'])}

        self.SixthLevelContainer = {"0": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_0']),
                                    "1": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_1']),
                                    "2": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_2']),
                                    "3": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_3']),
                                    "4": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_4']),
                                    "5": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_5']),
                                    "6": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_6']),
                                    "7": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_7']),
                                    "8": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_8']),
                                    "9": ctk.StringVar(value=self.CC.fields['Spells']['Sixth_Level']['Spell_Slot_9'])}

        self.SeventhLevelContainer = {
            "0": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_0']),
            "1": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_1']),
            "2": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_2']),
            "3": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_3']),
            "4": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_4']),
            "5": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_5']),
            "6": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_6']),
            "7": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_7']),
            "8": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_8']),
            "9": ctk.StringVar(value=self.CC.fields['Spells']['Seventh_Level']['Spell_Slot_9'])}

        self.EighthLevelContainer = {"0": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_0']),
                                     "1": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_1']),
                                     "2": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_2']),
                                     "3": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_3']),
                                     "4": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_4']),
                                     "5": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_5']),
                                     "6": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_6']),
                                     "7": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_7']),
                                     "8": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_8']),
                                     "9": ctk.StringVar(value=self.CC.fields['Spells']['Eighth_Level']['Spell_Slot_9'])}

        self.NinthLevelContainer = {"0": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_0']),
                                    "1": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_1']),
                                    "2": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_2']),
                                    "3": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_3']),
                                    "4": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_4']),
                                    "5": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_5']),
                                    "6": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_6']),
                                    "7": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_7']),
                                    "8": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_8']),
                                    "9": ctk.StringVar(value=self.CC.fields['Spells']['Ninth_Level']['Spell_Slot_9'])}

        # labels
        self.NameLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Character Name")
        self.ClassLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Class")
        self.LevelLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Level")
        self.RaceLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Race")
        self.BackgroundLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Background")
        self.AlignmentLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Alignment")
        self.ExperienceLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Experience")

        self.PersonalityLabel = ctk.CTkLabel(self.traits_div, font=self.font, text="Personality Traits")
        self.IdealsLabel = ctk.CTkLabel(self.traits_div, font=self.font, text="Ideals")
        self.BondsLabel = ctk.CTkLabel(self.traits_div, font=self.font, text="Bonds")
        self.FlawsLabel = ctk.CTkLabel(self.traits_div, font=self.font, text="Flaws")
        self.FeaturesLabel = ctk.CTkLabel(self.traits_div, font=self.font, text="Features")
        self.TraitsLabel = ctk.CTkLabel(self.traits_div, font=self.font, text="Traits")
        self.EquipmentLabel = ctk.CTkLabel(self.inner_attacks_div, font=self.font, text="Equipment")

        # attacks
        self.AttackNameLabel = ctk.CTkLabel(self.inner_attacks_div, font=self.font, text="Name")
        self.AttackBonusLabel = ctk.CTkLabel(self.inner_attacks_div, font=self.font, text="Bonus")
        self.AttackTypeLabel = ctk.CTkLabel(self.inner_attacks_div, font=self.font, text="Type")
        self.Attack1NameEntry = ctk.CTkEntry(self.inner_attacks_div, font=self.font, textvariable=self.Attack1Var)
        self.Attack2NameEntry = ctk.CTkEntry(self.inner_attacks_div, font=self.font, textvariable=self.Attack2Var)
        self.Attack3NameEntry = ctk.CTkEntry(self.inner_attacks_div, font=self.font, textvariable=self.Attack3Var)
        self.Attack1BonusEntry = ctk.CTkEntry(self.inner_attacks_div, font=self.font, textvariable=self.Attack1Bonus,
                                              width=35)
        self.Attack2BonusEntry = ctk.CTkEntry(self.inner_attacks_div, font=self.font, textvariable=self.Attack2Bonus,
                                              width=35)
        self.Attack3BonusEntry = ctk.CTkEntry(self.inner_attacks_div, font=self.font, textvariable=self.Attack3Bonus,
                                              width=35)
        self.Attack1TypeEntry = ctk.CTkEntry(self.inner_attacks_div, font=self.font, textvariable=self.Attack1Type)
        self.Attack2TypeEntry = ctk.CTkEntry(self.inner_attacks_div, font=self.font, textvariable=self.Attack2Type)
        self.Attack3TypeEntry = ctk.CTkEntry(self.inner_attacks_div, font=self.font, textvariable=self.Attack3Type)

        self.STRLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="STR")
        self.STRBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['STR_Mod']}", bg="#2B2B2B", fg="white")
        self.DEXLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="DEX")
        self.DEXBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['DEX_Mod']}", bg="#2B2B2B", fg="white")
        self.CONLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="CON")
        self.CONBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['CON_Mod']}", bg="#2B2B2B", fg="white")
        self.INTLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="INT")
        self.INTBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['INT_Mod']}", bg="#2B2B2B", fg="white")
        self.WISLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="WIS")
        self.WISBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['WIS_Mod']}", bg="#2B2B2B", fg="white")
        self.CHALabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="CHA")
        self.CHABonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['CHA_Mod']}", bg="#2B2B2B", fg="white")
        self.PassivePerceptionLabel = ctk.CTkLabel(self.stat_div, font=self.small_font,
                                                   text="Passive Wisdom (Perception)")

        self.ACLabel = ctk.CTkLabel(self.aux_attr_div, font=self.font, text="Armor Class")
        self.InitiativeLabel = ctk.CTkLabel(self.aux_attr_div, font=self.font, text="Initiative")
        self.SpeedLabel = ctk.CTkLabel(self.aux_attr_div, font=self.font, text="Speed")
        self.HPMAXLabel = ctk.CTkLabel(self.health_div, font=self.font, text="Maximum HP")
        self.HPCURRLabel = ctk.CTkLabel(self.health_div, font=self.font, text="Current HP")
        self.HPTEMPLabel = ctk.CTkLabel(self.health_div, font=self.font, text="Temporary HP")
        self.HDTOTLabel = ctk.CTkLabel(self.health_div, font=self.font, text="Total Hit Dice")
        self.HDCURRLabel = ctk.CTkLabel(self.health_div, font=self.font, text="Current Hit Dice")
        self.ElectrumLabel = ctk.CTkLabel(self.equipment_div, font=self.font, text="EP")
        self.SilverLabel = ctk.CTkLabel(self.equipment_div, font=self.font, text="SP")
        self.GoldLabel = ctk.CTkLabel(self.equipment_div, font=self.font, text="GP")
        self.PlatinumLabel = ctk.CTkLabel(self.equipment_div, font=self.font, text="PP")
        self.CopperLabel = ctk.CTkLabel(self.equipment_div, font=self.font, text="CP")
        self.DeathSavesLabel = ctk.CTkLabel(self.death_save_div, font=self.font, text="Death Saves")
        self.DSSLabel = ctk.CTkLabel(self.death_save_div, font=self.font, text="Successes: ")
        self.DSFLabel = ctk.CTkLabel(self.death_save_div, font=self.font, text="Failures: ")

        self.ACEntry = ctk.CTkEntry(self.aux_attr_div, font=self.font, textvariable=self.ACVar)
        self.InitEntry = ctk.CTkEntry(self.aux_attr_div, font=self.font, textvariable=self.InitVar)
        self.SpeedEntry = ctk.CTkEntry(self.aux_attr_div, font=self.font, textvariable=self.SpeedVar)

        self.DSSButton1 = ctk.CTkButton(self.death_save_div, text="( )", command=self._update_death_save_success1, width=10)
        self.DSSButton2 = ctk.CTkButton(self.death_save_div, text="( )", command=self._update_death_save_success2, width=10)
        self.DSSButton3 = ctk.CTkButton(self.death_save_div, text="( )", command=self._update_death_save_success3, width=10)
        self.DSFButton1 = ctk.CTkButton(self.death_save_div, text="( )", command=self._update_death_save_failures1, width=10)
        self.DSFButton2 = ctk.CTkButton(self.death_save_div, text="( )", command=self._update_death_save_failures2, width=10)
        self.DSFButton3 = ctk.CTkButton(self.death_save_div, text="( )", command=self._update_death_save_failures3, width=10)

        self.InspirationButton = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Inspiration", width=60,
                                               command=self._update_inspiration)
        self.ProfBonusLabel = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="Proficiency Bonus")
        self.SavingThrowsLabel = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="Saving Throws")
        self.Str_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Strength", width=50,
                                           command=lambda: self.update_saving_throws(st_label=self.Str_St_Label,
                                                                                     stat_key="STR",
                                                                                     second_label=self.Str_St_Label_2))
        self.Dex_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Dexterity", width=50,
                                           command=lambda: self.update_saving_throws(st_label=self.Dex_St_Label,
                                                                                     stat_key="DEX",
                                                                                     second_label=self.Dex_St_Label_2))
        self.Con_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Constitution", width=50,
                                           command=lambda: self.update_saving_throws(st_label=self.Con_St_Label,
                                                                                     stat_key="CON",
                                                                                     second_label=self.Con_St_Label_2))
        self.Int_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Intelligence", width=50,
                                           command=lambda: self.update_saving_throws(st_label=self.Int_St_Label,
                                                                                     stat_key="INT",
                                                                                     second_label=self.Int_St_Label_2))
        self.Wis_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Wisdom", width=50,
                                           command=lambda: self.update_saving_throws(st_label=self.Wis_St_Label,
                                                                                     stat_key="WIS",
                                                                                     second_label=self.Wis_St_Label_2))
        self.Cha_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Charisma", width=50,
                                           command=lambda: self.update_saving_throws(st_label=self.Cha_St_Label,
                                                                                     stat_key="CHA",
                                                                                     second_label=self.Cha_St_Label_2))

        # labels for the buttons
        self.Str_St_Label = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="( )")
        self.Dex_St_Label = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="( )")
        self.Con_St_Label = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="( )")
        self.Int_St_Label = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="( )")
        self.Wis_St_Label = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="( )")
        self.Cha_St_Label = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="( )")

        self.Str_St_Label_2 = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="+0")
        self.Dex_St_Label_2 = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="+0")
        self.Con_St_Label_2 = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="+0")
        self.Int_St_Label_2 = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="+0")
        self.Wis_St_Label_2 = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="+0")
        self.Cha_St_Label_2 = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="+0")

        # respective entry/buttons
        self.InspirationLabel = ctk.CTkLabel(self.saving_throws_div, text="( )")
        self.ProfBonusEntry = ctk.CTkEntry(self.saving_throws_div, textvariable=self.ProfBonusVar, width=30)

        # entry widgets
        self.NameEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.NameVar)
        self.ClassEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.ClassVar)
        self.LevelEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.LevelVar)
        self.RaceEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.RaceVar)
        self.BackgroundEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.BackgroundVar)
        self.AlignmentEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.AlignmentVar)
        self.ExperienceEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.ExperienceVar)
        self.PersonalityEntry = ctk.CTkTextbox(self.traits_div, font=self.font, width=250, height=100, border_width=2,
                                               wrap='word')
        self.IdealsEntry = ctk.CTkTextbox(self.traits_div, font=self.font, width=250, height=100, border_width=2,
                                          wrap='word')
        self.BondsEntry = ctk.CTkTextbox(self.traits_div, font=self.font, width=250, height=100, border_width=2,
                                         wrap='word')
        self.FlawsEntry = ctk.CTkTextbox(self.traits_div, font=self.font, width=250, height=100, border_width=2,
                                         wrap='word')
        self.FeaturesEntry = ctk.CTkTextbox(self.traits_div, font=self.font, width=250, height=100, border_width=2,
                                            wrap='word')
        self.TraitsEntry = ctk.CTkTextbox(self.traits_div, font=self.font, width=250, height=100, border_width=2,
                                          wrap='word')

        # equipment entry
        self.CopperEntry = ctk.CTkEntry(self.equipment_div, font=self.font, textvariable=self.CoppVar, width=30,
                                        justify=ctk.CENTER)
        self.SilverEntry = ctk.CTkEntry(self.equipment_div, font=self.font, textvariable=self.SilvVar, width=30,
                                        justify=ctk.CENTER)
        self.ElectrumEntry = ctk.CTkEntry(self.equipment_div, font=self.font, textvariable=self.ElecVar, width=30,
                                          justify=ctk.CENTER)
        self.GoldEntry = ctk.CTkEntry(self.equipment_div, font=self.font, textvariable=self.GoldVar, width=30,
                                      justify=ctk.CENTER)
        self.PlatinumEntry = ctk.CTkEntry(self.equipment_div, font=self.font, textvariable=self.PlatVar, width=30,
                                          justify=ctk.CENTER)
        self.EquipmentEntry = ctk.CTkTextbox(self.inner_attacks_div, font=self.font, width=400)

        self.STREntry = ctk.CTkEntry(self.stat_div, font=self.special_font, textvariable=self.STRVar, border_width=3,
                                     border_color="black", width=62, height=45, justify=ctk.CENTER, corner_radius=20)
        self.CONEntry = ctk.CTkEntry(self.stat_div, font=self.special_font, textvariable=self.CONVar, border_width=3,
                                     border_color="black", width=62, height=45, justify=ctk.CENTER, corner_radius=20)
        self.DEXEntry = ctk.CTkEntry(self.stat_div, font=self.special_font, textvariable=self.DEXVar, border_width=3,
                                     border_color="black", width=62, height=45, justify=ctk.CENTER, corner_radius=20)
        self.INTEntry = ctk.CTkEntry(self.stat_div, font=self.special_font, textvariable=self.INTVar, border_width=3,
                                     border_color="black", width=62, height=45, justify=ctk.CENTER, corner_radius=20)
        self.WISEntry = ctk.CTkEntry(self.stat_div, font=self.special_font, textvariable=self.WISVar, border_width=3,
                                     border_color="black", width=62, height=45, justify=ctk.CENTER, corner_radius=20)
        self.CHAEntry = ctk.CTkEntry(self.stat_div, font=self.special_font, textvariable=self.CHAVar, border_width=3,
                                     border_color="black", width=62, height=45, justify=ctk.CENTER, corner_radius=20)
        self.PassivePEntry = ctk.CTkEntry(self.stat_div, font=self.special_font, textvariable=self.PassivePVar,
                                          border_width=3, border_color="black", width=75, height=45, justify=ctk.CENTER,
                                          corner_radius=25)

        # hp entry
        self.HPMAXEntry = ctk.CTkEntry(self.health_div, font=self.font, textvariable=self.HPMaxVar, justify=ctk.CENTER,
                                       width=50)
        self.HPCURREntry = ctk.CTkEntry(self.health_div, font=self.font, textvariable=self.HPCurrVar,
                                        justify=ctk.CENTER, width=50)
        self.HPTEMPEntry = ctk.CTkEntry(self.health_div, font=self.font, textvariable=self.HPTempVar,
                                        justify=ctk.CENTER, width=50)
        self.HDTOTEntry = ctk.CTkEntry(self.health_div, font=self.font, textvariable=self.HDTotVar, justify=ctk.CENTER,
                                       width=50)
        self.HDCURREntry = ctk.CTkEntry(self.health_div, font=self.font, textvariable=self.HDCurrVar,
                                        justify=ctk.CENTER, width=50)

        # skill prof labels
        self.SkillBackground = tk.Label(self, bd=2, relief="solid", width=20, height=32)

        self.SkillsLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="Skills")
        self.AthleticsLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.AcrobaticsLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.SOHLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.StealthLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.ArcanaLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.HistoryLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.InvestigationLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.NatureLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.ReligionLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.AHLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.InsightLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.MedicineLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.PerceptionLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.SurvivalLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.DeceptionLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.IntimidationLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.PerformanceLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")
        self.PersuasionLabel = ctk.CTkLabel(self.stat_div, font=self.font, text="( )")

        # buttons for skill proficiencies
        self.AthleticsButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Athletics", height=6, width=6,
                                             command=lambda: self.update_proficiency(skill_label=self.AthleticsLabel,
                                                                                     stat_key="STR",
                                                                                     skill_key="Athletics"))
        self.AcrobaticsButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Acrobatics", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.AcrobaticsLabel,
                                                                                      stat_key="DEX",
                                                                                      skill_key="Acrobatics"))
        self.SOHButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Slight of Hand", height=6, width=6,
                                       command=lambda: self.update_proficiency(skill_label=self.SOHLabel,
                                                                               stat_key="DEX",
                                                                               skill_key="Slight_of_Hand"))
        self.StealthButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Stealth", height=6, width=6,
                                           command=lambda: self.update_proficiency(skill_label=self.StealthLabel,
                                                                                   stat_key="DEX", skill_key="Stealth"))
        self.ArcanaButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Arcana", height=6, width=6,
                                          command=lambda: self.update_proficiency(skill_label=self.ArcanaLabel,
                                                                                  stat_key="INT", skill_key="Arcana"))
        self.HistoryButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="History", height=6, width=6,
                                           command=lambda: self.update_proficiency(skill_label=self.HistoryLabel,
                                                                                   stat_key="INT", skill_key="History"))
        self.InvestigationButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Investigation", height=6,
                                                 width=6,
                                                 command=lambda: self.update_proficiency(
                                                     skill_label=self.InvestigationLabel, stat_key="INT",
                                                     skill_key="Investigation"))
        self.NatureButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Nature", height=6, width=6,
                                          command=lambda: self.update_proficiency(skill_label=self.NatureLabel,
                                                                                  stat_key="INT", skill_key="Nature"))
        self.ReligionButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Religion", height=6, width=6,
                                            command=lambda: self.update_proficiency(skill_label=self.ReligionLabel,
                                                                                    stat_key="INT",
                                                                                    skill_key="Religion"))
        self.AHButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Animal Handling", height=6, width=6,
                                      command=lambda: self.update_proficiency(skill_label=self.AHLabel, stat_key="WIS",
                                                                              skill_key="Animal_Handling"))
        self.InsightButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Insight", height=6, width=6,
                                           command=lambda: self.update_proficiency(skill_label=self.InsightLabel,
                                                                                   stat_key="WIS", skill_key="Insight"))
        self.MedicineButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Medicine", height=6, width=6,
                                            command=lambda: self.update_proficiency(skill_label=self.MedicineLabel,
                                                                                    stat_key="WIS",
                                                                                    skill_key="Medicine"))
        self.PerceptionButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Perception", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.PerceptionLabel,
                                                                                      stat_key="WIS",
                                                                                      skill_key="Perception"))
        self.SurvivalButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Survival", height=6, width=6,
                                            command=lambda: self.update_proficiency(skill_label=self.SurvivalLabel,
                                                                                    stat_key="WIS",
                                                                                    skill_key="Survival"))
        self.DeceptionButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Deception", height=6, width=6,
                                             command=lambda: self.update_proficiency(skill_label=self.DeceptionLabel,
                                                                                     stat_key="CHA",
                                                                                     skill_key="Deception"))
        self.IntimidationButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Intimidation", height=6,
                                                width=6,
                                                command=lambda: self.update_proficiency(
                                                    skill_label=self.IntimidationLabel, stat_key="CHA",
                                                    skill_key="Intimidation"))
        self.PerformanceButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Performance", height=6,
                                               width=6,
                                               command=lambda: self.update_proficiency(
                                                   skill_label=self.PerformanceLabel, stat_key="CHA",
                                                   skill_key="Performance"))
        self.PersuasionButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Persuasion", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.PersuasionLabel,
                                                                                      stat_key="CHA",
                                                                                      skill_key="Persuasion"))
        self.AthleticsButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Athletics", height=6, width=6,
                                             command=lambda: self.update_proficiency(skill_label=self.AthleticsLabel,
                                                                                     stat_key="STR",
                                                                                     skill_key="Athletics"))
        self.AcrobaticsButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Acrobatics", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.AcrobaticsLabel,
                                                                                      stat_key="DEX",
                                                                                      skill_key="Acrobatics"))
        self.SOHButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Slight of Hand", height=6, width=6,
                                       command=lambda: self.update_proficiency(skill_label=self.SOHLabel,
                                                                               stat_key="DEX",
                                                                               skill_key="Slight_of_Hand"))
        self.StealthButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Stealth", height=6, width=6,
                                           command=lambda: self.update_proficiency(skill_label=self.StealthLabel,
                                                                                   stat_key="DEX", skill_key="Stealth"))
        self.ArcanaButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Arcana", height=6, width=6,
                                          command=lambda: self.update_proficiency(skill_label=self.ArcanaLabel,
                                                                                  stat_key="INT", skill_key="Arcana"))
        self.HistoryButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="History", height=6, width=6,
                                           command=lambda: self.update_proficiency(skill_label=self.HistoryLabel,
                                                                                   stat_key="INT", skill_key="History"))
        self.InvestigationButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Investigation", height=6,
                                                 width=6,
                                                 command=lambda: self.update_proficiency(
                                                     skill_label=self.InvestigationLabel, stat_key="INT",
                                                     skill_key="Investigation"))
        self.NatureButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Nature", height=6, width=6,
                                          command=lambda: self.update_proficiency(skill_label=self.NatureLabel,
                                                                                  stat_key="INT", skill_key="Nature"))
        self.ReligionButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Religion", height=6, width=6,
                                            command=lambda: self.update_proficiency(skill_label=self.ReligionLabel,
                                                                                    stat_key="INT",
                                                                                    skill_key="Religion"))
        self.AHButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Animal Handling", height=6, width=6,
                                      command=lambda: self.update_proficiency(skill_label=self.AHLabel, stat_key="WIS",
                                                                              skill_key="Animal_Handling"))
        self.InsightButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Insight", height=6, width=6,
                                           command=lambda: self.update_proficiency(skill_label=self.InsightLabel,
                                                                                   stat_key="WIS", skill_key="Insight"))
        self.MedicineButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Medicine", height=6, width=6,
                                            command=lambda: self.update_proficiency(skill_label=self.MedicineLabel,
                                                                                    stat_key="WIS",
                                                                                    skill_key="Medicine"))
        self.PerceptionButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Perception", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.PerceptionLabel,
                                                                                      stat_key="WIS",
                                                                                      skill_key="Perception"))
        self.SurvivalButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Survival", height=6, width=6,
                                            command=lambda: self.update_proficiency(skill_label=self.SurvivalLabel,
                                                                                    stat_key="WIS",
                                                                                    skill_key="Survival"))
        self.DeceptionButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Deception", height=6, width=6,
                                             command=lambda: self.update_proficiency(skill_label=self.DeceptionLabel,
                                                                                     stat_key="CHA",
                                                                                     skill_key="Deception"))
        self.IntimidationButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Intimidation", height=6,
                                                width=6,
                                                command=lambda: self.update_proficiency(
                                                    skill_label=self.IntimidationLabel, stat_key="CHA",
                                                    skill_key="Intimidation"))
        self.PerformanceButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Performance", height=6,
                                               width=6,
                                               command=lambda: self.update_proficiency(
                                                   skill_label=self.PerformanceLabel, stat_key="CHA",
                                                   skill_key="Performance"))
        self.PersuasionButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Persuasion", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.PersuasionLabel,
                                                                                      stat_key="CHA",
                                                                                      skill_key="Persuasion"))

        # spell label and entry
        self.MasterSpellsLabel = ctk.CTkLabel(self.master_spell_div, text="Spell Casting", font=self.header_font)
        self.SpellSlotsLabel = ctk.CTkLabel(self.master_spell_div, text="Spell Slots:", font=self.header_font)

        self.CantripsLabel = ctk.CTkLabel(self.cantrips_div, text="Cantrips", font=self.font)
        self.FirstLevelLabel = ctk.CTkLabel(self.first_level_div, text="1st Level", font=self.font)
        self.SecondLevelLabel = ctk.CTkLabel(self.second_level_div, text="2nd Level", font=self.font)
        self.ThirdLevelLabel = ctk.CTkLabel(self.third_level_div, text="3rd Level", font=self.font)
        self.FourthLevelLabel = ctk.CTkLabel(self.fourth_level_div, text="4th Level", font=self.font)
        self.FifthLevelLabel = ctk.CTkLabel(self.fifth_level_div, text="5th Level", font=self.font)
        self.SixthLevelLabel = ctk.CTkLabel(self.sixth_level_div, text="6th Level", font=self.font)
        self.SeventhLevelLabel = ctk.CTkLabel(self.seventh_level_div, text="7th Level", font=self.font)
        self.EighthLevelLabel = ctk.CTkLabel(self.eighth_level_div, text="8th Level", font=self.font)
        self.NinthLevelLabel = ctk.CTkLabel(self.ninth_level_div, text="9th Level", font=self.font)

        # spell entry
        self.SpellSlotEntry = ctk.CTkEntry(self.master_spell_div, textvariable=self.SpellSlots, font=self.header_font)

        self.CantripSpells = [
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['0'], font=self.font),
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['1'], font=self.font),
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['2'], font=self.font),
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['3'], font=self.font),
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['4'], font=self.font),
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['5'], font=self.font),
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['6'], font=self.font),
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['7'], font=self.font),
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['8'], font=self.font),
            ctk.CTkEntry(self.cantrips_div, textvariable=self.CantripContainer['9'], font=self.font),
        ]
        self.FirstLevelSpells = [
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["0"], font=self.font),
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["1"], font=self.font),
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["2"], font=self.font),
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["3"], font=self.font),
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["4"], font=self.font),
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["5"], font=self.font),
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["6"], font=self.font),
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["7"], font=self.font),
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["8"], font=self.font),
            ctk.CTkEntry(self.first_level_div, textvariable=self.FirstLevelContainer["9"], font=self.font)]

        self.SecondLevelSpells = [
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["0"], font=self.font),
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["1"], font=self.font),
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["2"], font=self.font),
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["3"], font=self.font),
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["4"], font=self.font),
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["5"], font=self.font),
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["6"], font=self.font),
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["7"], font=self.font),
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["8"], font=self.font),
            ctk.CTkEntry(self.second_level_div, textvariable=self.SecondLevelContainer["9"], font=self.font)]

        self.ThirdLevelSpells = [
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["0"], font=self.font),
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["1"], font=self.font),
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["2"], font=self.font),
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["3"], font=self.font),
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["4"], font=self.font),
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["5"], font=self.font),
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["6"], font=self.font),
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["7"], font=self.font),
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["8"], font=self.font),
            ctk.CTkEntry(self.third_level_div, textvariable=self.ThirdLevelContainer["9"], font=self.font)]

        self.FourthLevelSpells = [
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["0"], font=self.font),
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["1"], font=self.font),
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["2"], font=self.font),
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["3"], font=self.font),
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["4"], font=self.font),
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["5"], font=self.font),
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["6"], font=self.font),
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["7"], font=self.font),
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["8"], font=self.font),
            ctk.CTkEntry(self.fourth_level_div, textvariable=self.FourthLevelContainer["9"], font=self.font)]

        self.FifthLevelSpells = [
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["0"], font=self.font),
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["1"], font=self.font),
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["2"], font=self.font),
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["3"], font=self.font),
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["4"], font=self.font),
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["5"], font=self.font),
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["6"], font=self.font),
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["7"], font=self.font),
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["8"], font=self.font),
            ctk.CTkEntry(self.fifth_level_div, textvariable=self.FifthLevelContainer["9"], font=self.font)]

        self.SixthLevelSpells = [
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["0"], font=self.font),
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["1"], font=self.font),
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["2"], font=self.font),
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["3"], font=self.font),
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["4"], font=self.font),
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["5"], font=self.font),
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["6"], font=self.font),
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["7"], font=self.font),
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["8"], font=self.font),
            ctk.CTkEntry(self.sixth_level_div, textvariable=self.SixthLevelContainer["9"], font=self.font)]

        self.SeventhLevelSpells = [
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["0"], font=self.font),
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["1"], font=self.font),
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["2"], font=self.font),
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["3"], font=self.font),
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["4"], font=self.font),
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["5"], font=self.font),
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["6"], font=self.font),
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["7"], font=self.font),
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["8"], font=self.font),
            ctk.CTkEntry(self.seventh_level_div, textvariable=self.SeventhLevelContainer["9"], font=self.font)]

        self.EighthLevelSpells = [
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["0"], font=self.font),
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["1"], font=self.font),
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["2"], font=self.font),
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["3"], font=self.font),
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["4"], font=self.font),
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["5"], font=self.font),
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["6"], font=self.font),
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["7"], font=self.font),
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["8"], font=self.font),
            ctk.CTkEntry(self.eighth_level_div, textvariable=self.EighthLevelContainer["9"], font=self.font)]

        self.NinthLevelSpells = [
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["0"], font=self.font),
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["1"], font=self.font),
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["2"], font=self.font),
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["3"], font=self.font),
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["4"], font=self.font),
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["5"], font=self.font),
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["6"], font=self.font),
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["7"], font=self.font),
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["8"], font=self.font),
            ctk.CTkEntry(self.ninth_level_div, textvariable=self.NinthLevelContainer["9"], font=self.font)]

        # whitespace labels
        self.whitespace1 = ctk.CTkLabel(self.stat_div, text="            ")
        self.sep_lab = ctk.CTkLabel(self.health_div, text="------------------------------------------------------",
                                    font=self.font)

        # placing death save widgets
        self.DeathSavesLabel.grid(row=0, column=0)
        self.DSSLabel.grid(row=1, column=0)
        self.DSSButton1.grid(row=1, column=1, padx=5, ipadx=5)
        self.DSSButton2.grid(row=1, column=2, padx=5, ipadx=5)
        self.DSSButton3.grid(row=1, column=3, padx=5, ipadx=5)
        self.DSFLabel.grid(row=2, column=0)
        self.DSFButton1.grid(row=2, column=1, padx=5, ipadx=5)
        self.DSFButton2.grid(row=2, column=2, padx=5, ipadx=5)
        self.DSFButton3.grid(row=2, column=3, padx=5, ipadx=5)

        # placing auxiliary attributes
        self.ACLabel.grid(row=0, column=0)
        self.InitiativeLabel.grid(row=0, column=1)
        self.SpeedLabel.grid(row=0, column=2)
        self.ACEntry.grid(row=1, column=0)
        self.InitEntry.grid(row=1, column=1)
        self.SpeedEntry.grid(row=1, column=2)

        # placing stats
        self.STRLabel.grid(row=0, column=0)
        self.STREntry.grid(row=1, column=0)
        self.STRBonusLabel.grid(row=2, column=0)
        self.DEXLabel.grid(row=3, column=0)
        self.DEXEntry.grid(row=4, column=0)
        self.DEXBonusLabel.grid(row=5, column=0)
        self.CONLabel.grid(row=6, column=0)
        self.CONEntry.grid(row=7, column=0)
        self.CONBonusLabel.grid(row=8, column=0)
        self.INTLabel.grid(row=9, column=0)
        self.INTEntry.grid(row=10, column=0)
        self.INTBonusLabel.grid(row=11, column=0)
        self.WISLabel.grid(row=12, column=0)
        self.WISEntry.grid(row=13, column=0)
        self.WISBonusLabel.grid(row=14, column=0)
        self.CHALabel.grid(row=15, column=0)
        self.CHAEntry.grid(row=16, column=0)
        self.CHABonusLabel.grid(row=17, column=0)
        self.PassivePEntry.grid(row=19, column=0)
        self.PassivePerceptionLabel.grid(row=19, column=2, columnspan=2)

        # need whitespace here
        self.whitespace1.grid(row=0, column=1)

        # placing skills on the frame
        self.SkillsLabel.grid(row=0, column=2)
        self.AthleticsLabel.grid(row=1, column=2)
        self.AthleticsButton.grid(row=1, column=3)
        self.AcrobaticsLabel.grid(row=2, column=2)
        self.AcrobaticsButton.grid(row=2, column=3)
        self.SOHLabel.grid(row=3, column=2)
        self.SOHButton.grid(row=3, column=3)
        self.StealthLabel.grid(row=4, column=2)
        self.StealthButton.grid(row=4, column=3)
        self.ArcanaLabel.grid(row=5, column=2)
        self.ArcanaButton.grid(row=5, column=3)
        self.HistoryLabel.grid(row=6, column=2)
        self.HistoryButton.grid(row=6, column=3)
        self.InvestigationLabel.grid(row=7, column=2)
        self.InvestigationButton.grid(row=7, column=3)
        self.NatureLabel.grid(row=8, column=2)
        self.NatureButton.grid(row=8, column=3)
        self.ReligionLabel.grid(row=9, column=2)
        self.ReligionButton.grid(row=9, column=3)
        self.AHLabel.grid(row=10, column=2)
        self.AHButton.grid(row=10, column=3)
        self.InsightLabel.grid(row=11, column=2)
        self.InsightButton.grid(row=11, column=3)
        self.MedicineLabel.grid(row=12, column=2)
        self.MedicineButton.grid(row=12, column=3)
        self.PerceptionLabel.grid(row=13, column=2)
        self.PerceptionButton.grid(row=13, column=3)
        self.SurvivalLabel.grid(row=14, column=2)
        self.SurvivalButton.grid(row=14, column=3)
        self.DeceptionLabel.grid(row=15, column=2)
        self.DeceptionButton.grid(row=15, column=3)
        self.IntimidationLabel.grid(row=16, column=2)
        self.IntimidationButton.grid(row=16, column=3)
        self.PerformanceLabel.grid(row=17, column=2)
        self.PerformanceButton.grid(row=17, column=3)
        self.PersuasionLabel.grid(row=18, column=2)
        self.PersuasionButton.grid(row=18, column=3)

        # placing attributes on the frame
        # column 1
        # row 1
        self.NameLabel.grid(row=0, column=0, padx=2, pady=1)
        self.NameEntry.grid(row=1, column=0, padx=2, pady=1)
        self.ClassLabel.grid(row=0, column=1, padx=2, pady=1)
        self.ClassEntry.grid(row=1, column=1, padx=2, pady=1)
        self.LevelLabel.grid(row=0, column=2, padx=2, pady=1)
        self.LevelEntry.grid(row=1, column=2, padx=2, pady=1)

        # row 2
        self.RaceLabel.grid(row=2, column=0, padx=2, pady=1)
        self.RaceEntry.grid(row=3, column=0, padx=2, pady=1)
        self.AlignmentLabel.grid(row=2, column=1, padx=2, pady=1)
        self.AlignmentEntry.grid(row=3, column=1, padx=2, pady=1)
        self.ExperienceLabel.grid(row=2, column=2, padx=2, pady=1)
        self.ExperienceEntry.grid(row=3, column=2, padx=2, pady=1)

        # column 2
        # row 1
        self.PersonalityLabel.grid(row=0, column=0, padx=2, pady=2)
        self.PersonalityEntry.grid(row=1, column=0, padx=2, pady=2)
        # row 2
        self.IdealsLabel.grid(row=2, column=0, padx=2, pady=2)
        self.IdealsEntry.grid(row=3, column=0, padx=2, pady=2)
        # row 3
        self.BondsLabel.grid(row=4, column=0, padx=2, pady=2)
        self.BondsEntry.grid(row=5, column=0, padx=2, pady=2)
        # row 4
        self.FlawsLabel.grid(row=6, column=0, padx=2, pady=2)
        self.FlawsEntry.grid(row=7, column=0, padx=2, pady=2)
        # row 5
        self.FeaturesLabel.grid(row=8, column=0, padx=2, pady=2)
        self.FeaturesEntry.grid(row=9, column=0, padx=2, pady=2)

        self.TraitsLabel.grid(row=10, column=0, padx=2, pady=2)
        self.TraitsEntry.grid(row=11, column=0, padx=2, pady=2)

        # placing equipment
        self.CopperEntry.grid(row=0, column=0, padx=2, pady=2)
        self.CopperLabel.grid(row=0, column=1, padx=2, pady=2)
        self.SilverEntry.grid(row=1, column=0, padx=2, pady=2)
        self.SilverLabel.grid(row=1, column=1, padx=2, pady=2)
        self.ElectrumEntry.grid(row=2, column=0, padx=2, pady=2)
        self.ElectrumLabel.grid(row=2, column=1, padx=2, pady=2)
        self.GoldEntry.grid(row=3, column=0, padx=2, pady=2)
        self.GoldLabel.grid(row=3, column=1, padx=2, pady=2)
        self.PlatinumEntry.grid(row=4, column=0, padx=2, pady=2)
        self.PlatinumLabel.grid(row=4, column=1, padx=2, pady=2)
        self.EquipmentLabel.grid(row=5, column=0, columnspan=3, pady=10)
        self.EquipmentEntry.grid(row=6, column=0, columnspan=3)

        # placing attacks
        self.AttackNameLabel.grid(row=0, column=0)
        self.AttackBonusLabel.grid(row=0, column=1)
        self.AttackTypeLabel.grid(row=0, column=2)
        self.Attack1NameEntry.grid(row=1, column=0)
        self.Attack1BonusEntry.grid(row=1, column=1)
        self.Attack1TypeEntry.grid(row=1, column=2)
        self.Attack2NameEntry.grid(row=2, column=0)
        self.Attack2BonusEntry.grid(row=2, column=1)
        self.Attack2TypeEntry.grid(row=2, column=2)
        self.Attack3NameEntry.grid(row=3, column=0)
        self.Attack3BonusEntry.grid(row=3, column=1)
        self.Attack3TypeEntry.grid(row=3, column=2)

        # health frame grid
        self.HPMAXLabel.grid(row=0, column=0, padx=2, pady=2)
        self.HPMAXEntry.grid(row=0, column=1, padx=2, pady=2)
        self.HPCURRLabel.grid(row=1, column=0, padx=2, pady=2)
        self.HPCURREntry.grid(row=1, column=1, padx=2, pady=2)
        self.HPTEMPLabel.grid(row=2, column=0, padx=2, pady=2)
        self.HPTEMPEntry.grid(row=2, column=1, padx=2, pady=2)
        self.sep_lab.grid(row=3, column=0, sticky=ctk.S, columnspan=2)
        self.HDTOTLabel.grid(row=4, column=0)
        self.HDTOTEntry.grid(row=4, column=1)
        self.HDCURRLabel.grid(row=5, column=0)
        self.HDCURREntry.grid(row=5, column=1)
        self.death_save_div.grid(row=6, column=0)

        # packing saving throw div
        self.InspirationLabel.grid(row=0, column=0)
        self.InspirationButton.grid(row=0, column=1, columnspan=2)
        self.ProfBonusEntry.grid(row=1, column=0)
        self.ProfBonusLabel.grid(row=1, column=1, columnspan=2, padx=5)
        self.SavingThrowsLabel.grid(row=2, column=0, columnspan=3, pady=20)

        self.Str_St_Label.grid(row=3, column=0)
        self.Str_St_Label_2.grid(row=3, column=1)
        self.Str_St_Button.grid(row=3, column=2)

        self.Dex_St_Label.grid(row=4, column=0)
        self.Dex_St_Label_2.grid(row=4, column=1)
        self.Dex_St_Button.grid(row=4, column=2)

        self.Con_St_Label.grid(row=5, column=0)
        self.Con_St_Label_2.grid(row=5, column=1)
        self.Con_St_Button.grid(row=5, column=2)

        self.Int_St_Label.grid(row=6, column=0)
        self.Int_St_Label_2.grid(row=6, column=1)
        self.Int_St_Button.grid(row=6, column=2)

        self.Wis_St_Label.grid(row=7, column=0)
        self.Wis_St_Label_2.grid(row=7, column=1)
        self.Wis_St_Button.grid(row=7, column=2)

        self.Cha_St_Label.grid(row=8, column=0)
        self.Cha_St_Label_2.grid(row=8, column=1)
        self.Cha_St_Button.grid(row=8, column=2)

        # placing spells inside divs
        self.MasterSpellsLabel.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
        self.SpellSlotsLabel.grid(row=0, column=3, padx=5, pady=5, columnspan=1)
        self.SpellSlotEntry.grid(row=0, column=4, padx=5, pady=5, columnspan=1)

        self.cantrips_div.grid(row=1, column=0, padx=5, pady=5)
        self.first_level_div.grid(row=1, column=1, padx=5, pady=5)
        self.second_level_div.grid(row=1, column=2, padx=5, pady=5)
        self.third_level_div.grid(row=1, column=3, padx=5, pady=5)
        self.fourth_level_div.grid(row=1, column=4, padx=5, pady=5)
        self.fifth_level_div.grid(row=1, column=5, padx=5, pady=5)
        self.sixth_level_div.grid(row=2, column=0, padx=5, pady=5)
        self.seventh_level_div.grid(row=2, column=1, padx=5, pady=5)
        self.eighth_level_div.grid(row=2, column=2, padx=5, pady=5)
        self.ninth_level_div.grid(row=2, column=3, padx=5, pady=5)

        self.CantripsLabel.grid()
        self.FirstLevelLabel.grid()
        self.SecondLevelLabel.grid()
        self.ThirdLevelLabel.grid()
        self.FourthLevelLabel.grid()
        self.FifthLevelLabel.grid()
        self.SixthLevelLabel.grid()
        self.SeventhLevelLabel.grid()
        self.EighthLevelLabel.grid()
        self.NinthLevelLabel.grid()

        for slot in self.CantripSpells:
            slot.grid(pady=3)

        for slot in self.FirstLevelSpells:
            slot.grid(pady=3)

        for slot in self.SecondLevelSpells:
            slot.grid(pady=3)

        for slot in self.ThirdLevelSpells:
            slot.grid(pady=3)

        for slot in self.FourthLevelSpells:
            slot.grid(pady=3)

        for slot in self.FifthLevelSpells:
            slot.grid(pady=3)

        for slot in self.SixthLevelSpells:
            slot.grid(pady=3)

        for slot in self.SeventhLevelSpells:
            slot.grid(pady=3)

        for slot in self.EighthLevelSpells:
            slot.grid(pady=3)

        for slot in self.NinthLevelSpells:
            slot.grid(pady=3)

        # configuring textbox widgets
        self.PersonalityEntry.insert("0.0", self.CC.fields["Attributes"]["Personality"])
        self.IdealsEntry.insert("0.0", self.CC.fields["Attributes"]["Ideals"])
        self.BondsEntry.insert("0.0", self.CC.fields["Attributes"]["Bonds"])
        self.FlawsEntry.insert("0.0", self.CC.fields["Attributes"]["Flaws"])
        self.FeaturesEntry.insert("0.0", self.CC.fields["Attributes"]["Features"])
        self.TraitsEntry.insert("0.0", self.CC.fields["Attributes"]["Traits"])
        self.EquipmentEntry.insert("0.0", self.CC.fields["Attacks"]["Equipment"])

        # inserting last data for saving throws
        temp = [self.Str_St_Label, self.Dex_St_Label, self.Con_St_Label,
                self.Int_St_Label, self.Wis_St_Label, self.Cha_St_Label]
        temp2 = [self.Str_St_Label_2, self.Dex_St_Label_2, self.Con_St_Label_2,
                 self.Int_St_Label_2, self.Wis_St_Label_2, self.Cha_St_Label_2]
        for label, label2, key in zip(temp, temp2, self.stat_keys):
            if self.CC.fields["SavingThrows"][key]["Proficient"] == 1:
                label.configure(text=f"{'(' + chr(215) + ')'}")
                label2.configure(text=self.CC.fields["Auxiliary"]["Prof_Bonus"])

        self._load_ds()
        self._load_skills()
        self._load_insp()

        # gridding containters
        self.stat_div.grid(row=0, column=0, rowspan=10, ipadx=10, ipady=10)
        self.attr_div.grid(row=0, column=2, rowspan=2, columnspan=2, ipadx=10, ipady=10)
        self.aux_attr_div.grid(row=2, column=2, columnspan=2)
        self.saving_throws_div.grid(row=0, column=1, rowspan=4)
        self.health_div.grid(row=3, column=2, columnspan=2, rowspan=4)
        self.attacks_div.grid(row=7, column=2, columnspan=2, rowspan=6, padx=5)
        self.equipment_div.grid(row=0, column=0, padx=10, rowspan=2)
        self.inner_attacks_div.grid(row=0, column=1, rowspan=4)
        self.traits_div.grid(row=0, column=7, rowspan=10)
        self.master_spell_div.grid(row=13, column=0, rowspan=20, columnspan=30)

        # defining class methods

    def update_proficiency(self, skill_label: ctk.CTkLabel, stat_key, skill_key):
        if skill_label.cget("text") == "( )":
            skill_label.configure(text="(" + chr(215) + ")")
            self.CC.fields["Skills"][stat_key][skill_key]["Proficient"] = 1
            print(self.CC.fields["Skills"][stat_key][skill_key])
        else:
            skill_label.configure(text="( )")
            self.CC.fields["Skills"][stat_key][skill_key]["Proficient"] = 0
            print(self.CC.fields["Skills"][stat_key][skill_key])

    def update_saving_throws(self, st_label: ctk.CTkLabel, second_label: ctk.CTkLabel, stat_key):
        if st_label.cget("text") == "( )":
            st_label.configure(text="(" + chr(215) + ")")
            self.CC.fields["SavingThrows"][stat_key]["Proficient"] = 1
            second_label.configure(text=f"{self.CC.fields['Auxiliary']['Prof_Bonus']}")
        else:
            st_label.configure(text="( )")
            self.CC.fields["SavingThrows"][stat_key]["Proficient"] = 0
            second_label.configure(text="+0")

    def _save_spell_slots(self):
        self.CC.fields["Spells"]["Spell_Slots"] = self.SpellSlots.get()
    def _update_death_save_success1(self):
        if self.DSSButton1.cget('text') == "( )":
            self.DSSButton1.configure(text="(" + chr(215) + ")")
            self.CC.fields["DeathSaves"]["Death_Saves_Successes1"] = 'true'
        else:
            self.DSSButton1.configure(text="( )")
            self.CC.fields["DeathSaves"]["Death_Saves_Successes1"] = 'false'

    def _update_death_save_success2(self):
        if self.DSSButton2.cget('text') == "( )":
            self.DSSButton2.configure(text="(" + chr(215) + ")")
            self.CC.fields["DeathSaves"]["Death_Saves_Successes2"] = 'true'
        else:
            self.DSSButton2.configure(text="( )")
            self.CC.fields["DeathSaves"]["Death_Saves_Successes2"] = 'false'

    def _update_death_save_success3(self):
        if self.DSSButton3.cget('text') == "( )":
            self.DSSButton3.configure(text="(" + chr(215) + ")")
            self.CC.fields["DeathSaves"]["Death_Saves_Successes3"] = 'true'
        else:
            self.DSSButton3.configure(text="( )")
            self.CC.fields["DeathSaves"]["Death_Saves_Successes3"] = 'false'

    def _update_death_save_failures1(self):
        if self.DSFButton1.cget('text') == "( )":
            self.DSFButton1.configure(text="(" + chr(215) + ")")
            self.CC.fields["DeathSaves"]["Death_Saves_Failures1"] = 'true'
        else:
            self.DSFButton1.configure(text="( )")
            self.CC.fields["DeathSaves"]["Death_Saves_Failures1"] = 'false'

    def _update_death_save_failures2(self):
        if self.DSFButton2.cget('text') == "( )":
            self.DSFButton2.configure(text="(" + chr(215) + ")")
            self.CC.fields["DeathSaves"]["Death_Saves_Failures2"] = 'true'
        else:
            self.DSFButton2.configure(text="( )")
            self.CC.fields["DeathSaves"]["Death_Saves_Failures2"] = 'false'

    def _update_death_save_failures3(self):
        if self.DSFButton3.cget('text') == "( )":
            self.DSFButton3.configure(text="(" + chr(215) + ")")
            self.CC.fields["DeathSaves"]["Death_Saves_Failures3"] = 'true'
        else:
            self.DSFButton3.configure(text="( )")
            self.CC.fields["DeathSaves"]["Death_Saves_Failures3"] = 'false'

    def _update_inspiration(self):
        if self.InspirationLabel.cget('text') == '( )':
            self.InspirationLabel.configure(text='(' + chr(215) + ')')
            self.CC.fields["Auxiliary"]["Inspiration"] = "true"
        else:
            self.InspirationLabel.configure(text="( )")
            self.CC.fields["Auxiliary"]["Inspiration"] = "false"

    def save(self, event):
        current = {
            "stats": [self.STRVar.get(), self.DEXVar.get(), self.CONVar.get(), self.INTVar.get(), self.WISVar.get(),
                      self.CHAVar.get()],
            "attr": [self.NameVar.get(), self.ClassVar.get(), self.LevelVar.get(), self.RaceVar.get(),
                     self.BackgroundVar.get(), self.AlignmentVar.get(), self.ExperienceVar.get(),
                     self.PersonalityEntry.get("0.0", "end"), self.IdealsEntry.get("0.0", "end"),
                     self.BondsEntry.get("0.0", "end")],
            "ProfBonus": self.ProfBonusVar.get(),
        }
        self.CC.update_stats(values=current['stats'])
        self.CC.update_prof_bonus(value=current["ProfBonus"])
        self._update_stat_mod()
        self._update_stats()
        self._update_st()
        self._save_cantrips()
        self._save_1st_spells()
        self._save_2nd_spells()
        self._save_3rd_spells()
        self._save_4th_spells()
        self._save_5th_spells()
        self._save_6th_spells()
        self._save_7th_spells()
        self._save_8th_spells()
        self._save_9th_spells()
        self._save_money()
        self._save_attacks()
        self._save_hp()
        self._save_hd()
        self._save_aux()
        self._save_spell_slots()

    def _save_aux(self):
        to_save = [self.ACVar.get(), self.InitVar.get(), self.SpeedVar.get()]
        self.CC.update_auxiliary(to_save)

    def _save_hp(self):
        to_save = [self.HPMaxVar.get(), self.HPCurrVar.get(), self.HPTempVar.get()]
        self.CC.update_hit_points(to_save)

    def _save_hd(self):
        to_save = [self.HDTotVar.get(), self.HDCurrVar.get()]
        self.CC.update_hit_dice(to_save)

    def _save_money(self):
        to_save = [self.CoppVar.get(), self.SilvVar.get(), self.ElecVar.get(),
                   self.GoldVar.get(), self.PlatVar.get()]
        self.CC.update_money(to_save)

    def _save_attacks(self):
        to_save = [self.EquipmentEntry.get('0.0', ctk.END), self.Attack1Var.get(), self.Attack2Var.get(),
                   self.Attack3Var.get(),
                   self.Attack1Bonus.get(), self.Attack2Bonus.get(), self.Attack3Bonus.get(),
                   self.Attack1Type.get(), self.Attack2Type.get(), self.Attack3Type.get()]
        self.CC.update_attacks(to_save)

    def _save_cantrips(self):
        to_save = []
        for key in self.CantripContainer.keys():
            to_save.append(self.CantripContainer[key].get())
        self.CC.update_cantrip(to_save)

    def _save_1st_spells(self):
        to_save = []
        for key in self.FirstLevelContainer.keys():
            to_save.append(self.FirstLevelContainer[key].get())
        self.CC.update_spells(values=to_save, level="First_Level")

    def _save_2nd_spells(self):
        to_save = []
        for key in self.SecondLevelContainer.keys():
            to_save.append(self.SecondLevelContainer[key].get())
        self.CC.update_spells(values=to_save, level="Second_Level")

    def _save_3rd_spells(self):
        to_save = []
        for key in self.ThirdLevelContainer.keys():
            to_save.append(self.ThirdLevelContainer[key].get())
        self.CC.update_spells(values=to_save, level="Third_Level")

    def _save_4th_spells(self):
        to_save = []
        for key in self.FourthLevelContainer.keys():
            to_save.append(self.FourthLevelContainer[key].get())
        self.CC.update_spells(values=to_save, level="Fourth_Level")

    def _save_5th_spells(self):
        to_save = []
        for key in self.FifthLevelContainer.keys():
            to_save.append(self.FifthLevelContainer[key].get())
        self.CC.update_spells(values=to_save, level="Fifth_Level")

    def _save_6th_spells(self):
        to_save = []
        for key in self.SixthLevelContainer.keys():
            to_save.append(self.SixthLevelContainer[key].get())
        self.CC.update_spells(values=to_save, level="Sixth_Level")

    def _save_7th_spells(self):
        to_save = []
        for key in self.SeventhLevelContainer.keys():
            to_save.append(self.SeventhLevelContainer[key].get())
        self.CC.update_spells(values=to_save, level="Seventh_Level")

    def _save_8th_spells(self):
        to_save = []
        for key in self.EighthLevelContainer.keys():
            to_save.append(self.EighthLevelContainer[key].get())
        self.CC.update_spells(values=to_save, level="Eighth_Level")

    def _save_9th_spells(self):
        to_save = []
        for key in self.NinthLevelContainer.keys():
            to_save.append(self.NinthLevelContainer[key].get())
        self.CC.update_spells(values=to_save, level="Ninth_Level")

    def _update_stat_mod(self):
        """helper function to update the stat modifiers while the application is running"""
        self.STRBonusLabel.configure(text=f"{self.CC.fields['Stat_Modifiers']['STR_Mod']}")
        self.DEXBonusLabel.configure(text=f"{self.CC.fields['Stat_Modifiers']['DEX_Mod']}")
        self.CONBonusLabel.configure(text=f"{self.CC.fields['Stat_Modifiers']['CON_Mod']}")
        self.INTBonusLabel.configure(text=f"{self.CC.fields['Stat_Modifiers']['INT_Mod']}")
        self.WISBonusLabel.configure(text=f"{self.CC.fields['Stat_Modifiers']['WIS_Mod']}")
        self.CHABonusLabel.configure(text=f"{self.CC.fields['Stat_Modifiers']['CHA_Mod']}")

    def _update_stats(self):
        """helper function to update the stat values in case any bad inputs are given"""
        self.STRVar.set(value=f"{self.CC.fields['Stats']['STR']}")
        self.DEXVar.set(value=f"{self.CC.fields['Stats']['DEX']}")
        self.CONVar.set(value=f"{self.CC.fields['Stats']['CON']}")
        self.INTVar.set(value=f"{self.CC.fields['Stats']['INT']}")
        self.WISVar.set(value=f"{self.CC.fields['Stats']['WIS']}")
        self.CHAVar.set(value=f"{self.CC.fields['Stats']['CHA']}")

    def _update_st(self):
        labels = [self.Str_St_Label_2, self.Dex_St_Label_2, self.Con_St_Label_2,
                  self.Int_St_Label_2, self.Wis_St_Label_2, self.Cha_St_Label_2]
        for stat, label in zip(self.stat_keys, labels):
            if self.CC.fields["SavingThrows"][stat]["Proficient"] == 1:
                label.configure(text=f"{self.CC.fields['Auxiliary']['Prof_Bonus']}")

    def _load_ds(self):
        buttons = [self.DSSButton1, self.DSSButton2, self.DSSButton3, self.DSFButton1,
                   self.DSFButton2, self.DSFButton3]
        keys = ["Death_Saves_Successes1", "Death_Saves_Successes2", "Death_Saves_Successes3",
                "Death_Saves_Failures1", "Death_Saves_Failures2", "Death_Saves_Failures3"]
        for button, key in zip(buttons, keys):
            if self.CC.fields["DeathSaves"][key] == "true":
                button.configure(text="(" + chr(215) + ")")
            else:
                button.configure(text="( )")

    def _load_insp(self):
        if self.CC.fields["Auxiliary"]["Inspiration"] == "true":
            self.InspirationLabel.configure(text="(" + chr(215) + ")")

    def _load_skills(self):
        str_labels = [self.AthleticsLabel]
        dex_labels = [self.AcrobaticsLabel, self.SOHLabel, self.StealthLabel]
        dex_keys = ["Acrobatics", "Slight_of_Hand", "Stealth"]
        int_labels = [self.ArcanaLabel, self.HistoryLabel, self.InvestigationLabel, self.NatureLabel, self.ReligionLabel]
        int_keys = ["Arcana", "History", "Investigation", "Nature", "Religion"]
        wis_labels = [self.AHLabel, self.InsightLabel, self.MedicineLabel, self.PerceptionLabel, self.SurvivalLabel]
        wis_keys = ["Animal_Handling", "Insight", "Medicine", "Perception", "Survival"]
        cha_labels = [self.DeceptionLabel, self.IntimidationLabel, self.PerformanceLabel, self.PersuasionLabel]
        cha_keys = ["Deception", "Intimidation", "Performance", "Persuasion"]

        # update str
        if self.CC.fields["Skills"]["STR"]["Athletics"]["Proficient"] == 1:
            str_labels[0].configure(text="(" + chr(215) + ")")

        for label, key in zip(dex_labels, dex_keys):
            if self.CC.fields["Skills"]["DEX"][key]["Proficient"] == 1:
                label.configure(text="(" + chr(215) + ")")

        for label, key in zip(int_labels, int_keys):
            if self.CC.fields["Skills"]["INT"][key]["Proficient"] == 1:
                label.configure(text="(" + chr(215) + ")")

        for label, key in zip(wis_labels, wis_keys):
            if self.CC.fields["Skills"]["WIS"][key]["Proficient"] == 1:
                label.configure(text="(" + chr(215) + ")")

        for label, key in zip(cha_labels, cha_keys):
            if self.CC.fields["Skills"]["CHA"][key]["Proficient"] == 1:
                label.configure(text="(" + chr(215) + ")")



if __name__ == '__main__':
    test = ctk.CTk()
    test.geometry("1350x820")
    test.iconbitmap("dice-icon.ico")
    test.title("Character Sheet")

    ssf = DNDCharacterFrame(test)

    test.bind('<Control-s>', ssf.save)

    ssf.pack(fill=ctk.BOTH, expand=True)

    test.mainloop()
