import tkinter as tk
import customtkinter as ctk
from CharacterDataHandler import DataHandler

ctk.set_appearance_mode("Dark")


class DNDCharacterFrame(ctk.CTkScrollableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # defining character creator
        self.CC = DataHandler()

        self.stat_keys = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

        # creating container frames or "divs"
        self.stat_div = ctk.CTkFrame(self, border_width=2, border_color="red")
        self.attr_div = ctk.CTkFrame(self, border_width=2, border_color="blue")
        self.traits_div = ctk.CTkFrame(self, border_width=2, border_color="orange")
        self.health_div = ctk.CTkFrame(self, border_width=2, border_color="pink")
        self.attacks_div = ctk.CTkFrame(self, border_width=2, border_color="purple")
        self.inner_attacks_div = ctk.CTkFrame(self.attacks_div, border_width=2, border_color="yellow")
        self.equipment_div = ctk.CTkFrame(self.attacks_div, border_width=2, border_color="green")
        self.passivep_div = ctk.CTkFrame(self, border_width=2, border_color="indigo")
        self.saving_throws_div = ctk.CTkFrame(self, border_width=2, border_color="teal")

        # declaring fonts
        self.small_font = ctk.CTkFont(family="Rockwell", size=10)
        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.bold_font = ctk.CTkFont(family="Rockwell", size=14, weight="bold")
        self.special_font = ctk.CTkFont(family="Rockwell", size=18)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)

        # variables
        # kinter variables
        self.NameVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Character_Name"])
        self.ClassVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Class"])
        self.LevelVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Level"])
        self.RaceVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Race"])
        self.BackgroundVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Background"])
        self.AlignmentVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Alignment"])
        self.ExperienceVar = ctk.StringVar(value=self.CC.fields["Attributes"]["Experience"])
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
        self.SpeedVar = ctk.StringVar(value=self.CC.fields["Auxiliary"]["Speed"])
        self.ProfBonusVar = ctk.StringVar(value=self.CC.fields["Auxiliary"]["Prof_Bonus"])
        self.HPMaxVar = ctk.IntVar(value=self.CC.fields["HitPoints"]["HP_Max"])
        self.HPCurrVar = ctk.IntVar(value=self.CC.fields["HitPoints"]["HP_Curr"])
        self.HPTempVar = ctk.IntVar(value=self.CC.fields["HitPoints"]["HP_Temp"])
        self.HDTotVar = ctk.IntVar(value=self.CC.fields["HitDice"]["HD_Total"])
        self.HDCurrVar = ctk.IntVar(value=self.CC.fields["HitDice"]["HD_Curr"])
        self.ElecVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Electrum"])
        self.PlatVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Platinum"])
        self.GoldVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Gold"])
        self.SilvVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Silver"])
        self.CoppVar = ctk.IntVar(value=self.CC.fields["Equipment"]["Copper"])
        self.InspirationVar = ctk.StringVar()
        self.Str_St_Var = ctk.StringVar()
        self.Dex_St_Var = ctk.StringVar()
        self.Con_St_Var = ctk.StringVar()
        self.Int_St_Var = ctk.StringVar()
        self.Wis_St_Var = ctk.StringVar()
        self.Cha_St_Var = ctk.StringVar()

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
        self.Attack1Label = ctk.CTkLabel(self, font=self.font, text="Attack 1")
        self.Attack2Label = ctk.CTkLabel(self, font=self.font, text="Attack 2")
        self.Attack3Label = ctk.CTkLabel(self, font=self.font, text="Attack 3")

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
        self.PassivePerceptionLabel = ctk.CTkLabel(self.passivep_div, font=self.small_font,
                                                   text="Passive Wisdom (Perception)")

        self.ACLabel = ctk.CTkLabel(self, font=self.font, text="Armor Class")
        self.SpeedLabel = ctk.CTkLabel(self, font=self.font, text="Speed")
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
        self.DeathSavesLabel = ctk.CTkLabel(self, font=self.font, text="Death Saves")
        self.InitiativeLabel = ctk.CTkLabel(self, font=self.font, text="Initiative")

        self.InspirationLabel = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Inspiration", width=60)
        self.ProfBonusLabel = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="Proficiency Bonus")
        self.SavingThrowsLabel = ctk.CTkLabel(self.saving_throws_div, font=self.font, text="Saving Throws")
        self.Str_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Strength", width=50, command=lambda: self.update_saving_throws(st_label=self.Str_St_Label, stat_key="STR", second_label=self.Str_St_Label_2))
        self.Dex_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Dexterity", width=50, command=lambda: self.update_saving_throws(st_label=self.Dex_St_Label, stat_key="DEX", second_label=self.Dex_St_Label_2))
        self.Con_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Constitution", width=50, command=lambda: self.update_saving_throws(st_label=self.Con_St_Label, stat_key="CON", second_label=self.Con_St_Label_2))
        self.Int_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Intelligence", width=50, command=lambda: self.update_saving_throws(st_label=self.Int_St_Label, stat_key="INT", second_label=self.Int_St_Label_2))
        self.Wis_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Wisdom", width=50, command=lambda: self.update_saving_throws(st_label=self.Wis_St_Label, stat_key="WIS", second_label=self.Wis_St_Label_2))
        self.Cha_St_Button = ctk.CTkButton(self.saving_throws_div, font=self.font, text="Charisma", width=50, command=lambda: self.update_saving_throws(st_label=self.Cha_St_Label, stat_key="CHA", second_label=self.Cha_St_Label_2))

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
        self.InspirationEntry = ctk.CTkLabel(self.saving_throws_div, text="( )")
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
        self.EquipmentEntry = ctk.CTkTextbox(self.inner_attacks_div, font=self.font)

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
        self.PassivePEntry = ctk.CTkEntry(self.passivep_div, font=self.special_font, textvariable=self.PassivePVar,
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

        self.SaveButton = ctk.CTkButton(self, text="Save", command=self.save)

        # whitespace labels
        self.whitespace1 = ctk.CTkLabel(self.stat_div, text="            ")
        self.sep_lab = ctk.CTkLabel(self.health_div, text="------------------------------------------------------",
                                    font=self.font)

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
        self.PassivePEntry.grid(row=0, column=0, pady=15, rowspan=2)
        self.PassivePerceptionLabel.grid(row=0, column=1, pady=15, rowspan=2)

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
        self.EquipmentLabel.grid(row=0, column=0)
        self.EquipmentEntry.grid(row=1, column=0)

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

        # packing saving throw div
        self.InspirationEntry.grid(row=0, column=0)
        self.InspirationLabel.grid(row=0, column=1, columnspan=2)
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


        # gridding containters
        self.stat_div.grid(row=0, column=0, sticky=ctk.NW, rowspan=8, padx=10)
        self.passivep_div.grid(row=5, column=0)
        self.attr_div.grid(row=0, column=1, sticky=ctk.N, padx=10, columnspan=10, ipadx=5, ipady=5)
        self.saving_throws_div.grid(row=1, column=1, padx=10, columnspan=2)
        self.health_div.grid(row=1, column=3, padx=10)

        self.attacks_div.grid(row=2, column=3, padx=10, ipadx=5, ipady=5)
        self.equipment_div.grid(row=0, column=0, padx=10, ipadx=5, ipady=5, sticky=ctk.NW)
        self.inner_attacks_div.grid(row=0, column=1)

        self.traits_div.grid(row=0, column=11, sticky=ctk.NE, rowspan=10, padx=10)



        self.SaveButton.grid()

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



    def save(self, event):
        current = {
            "stats": [self.STRVar.get(), self.DEXVar.get(), self.CONVar.get(), self.INTVar.get(), self.WISVar.get(),
                      self.CHAVar.get()],
            "attr": [self.NameVar.get(), self.ClassVar.get(), self.LevelVar.get(), self.RaceVar.get(),
                     self.BackgroundVar.get(), self.AlignmentVar.get(), self.ExperienceVar.get(),
                     self.PersonalityEntry.get("0.0", "end"), self.IdealsEntry.get("0.0", "end"),
                     self.BondsEntry.get("0.0", "end")],
            "hit_points": [],
            "hit_dice": [],
            "death_saves": [],
            "saving_throws": [],
            "auxiliary": [],
            "equipment": [],
            "attacks": [],
            "ProfBonus": self.ProfBonusVar.get(),
        }
        self.CC.update_stats(values=current['stats'])
        self.CC.update_prof_bonus(value=current["ProfBonus"])
        self._update_stat_mod()
        self._update_stats()
        self._update_st()

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


if __name__ == '__main__':
    test = ctk.CTk()
    test.geometry("1080x720")
    test.iconbitmap("dice-icon.ico")
    test.title("Character Sheet")

    ssf = DNDCharacterFrame(test)

    test.bind('<Control-s>', ssf.save)

    ssf.pack(fill=ctk.BOTH, expand=True)

    test.mainloop()
