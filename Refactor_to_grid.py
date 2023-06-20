import tkinter as tk
import customtkinter as ctk
from CreateCharacterClass import CharacterCreator


class SamsScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # defining character creator
        self.CC = CharacterCreator()

        # creating container frames or "divs"
        self.stat_div = ctk.CTkFrame(self, border_width=2, border_color="red")
        self.attr_div = ctk.CTkFrame(self, border_width=2, border_color="blue")

        # declaring fonts
        self.small_font = ctk.CTkFont(family="Rockwell", size=10)
        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.bold_font = ctk.CTkFont(family="Rockwell", size=14, weight="bold")
        self.special_font = ctk.CTkFont(family="Rockwell", size=18)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)
        # labels

        self.NameLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Character Name")
        self.ClassLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Class")
        self.LevelLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Level")
        self.RaceLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Race")
        self.BackgroundLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Background")
        self.AlignmentLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Alignment")
        self.ExperienceLabel = ctk.CTkLabel(self.attr_div, font=self.font, text="Experience")

        self.PersonalityLabel = ctk.CTkLabel(self, font=self.font, text="Personality Traits")
        self.IdealsLabel = ctk.CTkLabel(self, font=self.font, text="Ideals")
        self.BondsLabel = ctk.CTkLabel(self, font=self.font, text="Bonds")
        self.FlawsLabel = ctk.CTkLabel(self, font=self.font, text="Flaws")
        self.FeaturesLabel = ctk.CTkLabel(self, font=self.font, text="Features")
        self.TraitsLabel = ctk.CTkLabel(self, font=self.font, text="Traits")
        self.EquipmentLabel = ctk.CTkLabel(self, font=self.font, text="Equipment")
        self.Attack1Label = ctk.CTkLabel(self, font=self.font, text="Attack 1")
        self.Attack2Label = ctk.CTkLabel(self, font=self.font, text="Attack 2")
        self.Attack3Label = ctk.CTkLabel(self, font=self.font, text="Attack 3")

        self.STRLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="STR")
        self.STRBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['STR_Mod']}")
        self.DEXLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="DEX")
        self.DEXBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['DEX_Mod']}")
        self.CONLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="CON")
        self.CONBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['CON_Mod']}")
        self.INTLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="INT")
        self.INTBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['INT_Mod']}")
        self.WISLabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="WIS")
        self.WISBonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['WIS_Mod']}")
        self.CHALabel = ctk.CTkLabel(self.stat_div, font=self.bold_font, text="CHA")
        self.CHABonusLabel = tk.Label(self.stat_div, bd=2, width=3, relief="solid", font=self.font,
                                      text=f"{self.CC.fields['Stat_Modifiers']['CHA_Mod']}")

        self.PassivePerceptionLabel = ctk.CTkLabel(self, font=self.font, text="Passive Wisdom (Perception)")
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
        self.DeathSavesLabel = ctk.CTkLabel(self, font=self.font, text="Death Saves")

        self.InspirationLabel = ctk.CTkLabel(self, font=self.font, text="Inspiration")
        self.InitiativeLabel = ctk.CTkLabel(self, font=self.font, text="Initiative")
        self.SavingThrowsLabel = ctk.CTkLabel(self, font=self.font, text="Saving Throws")
        self.Str_St_Label = ctk.CTkLabel(self, font=self.font, text="Strength")
        self.Dex_St_Label = ctk.CTkLabel(self, font=self.font, text="Dexterity")
        self.Con_St_Label = ctk.CTkLabel(self, font=self.font, text="Constitution")
        self.Int_St_Label = ctk.CTkLabel(self, font=self.font, text="Intelligence")
        self.Wis_St_Label = ctk.CTkLabel(self, font=self.font, text="Wisdom")
        self.Cha_St_Label = ctk.CTkLabel(self, font=self.font, text="Charisma+")

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
        # death saves

        # entry widgets
        self.NameEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.NameVar)
        self.ClassEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.ClassVar)
        self.LevelEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.LevelVar)
        self.RaceEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.RaceVar)
        self.BackgroundEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.BackgroundVar)
        self.AlignmentEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.AlignmentVar)
        self.ExperienceEntry = ctk.CTkEntry(self.attr_div, font=self.font, textvariable=self.ExperienceVar)
        self.PersonalityEntry = ctk.CTkTextbox(self, font=self.font, width=250, height=100, border_width=2, wrap='word')
        self.IdealsEntry = ctk.CTkTextbox(self, font=self.font, width=250, height=100, border_width=2, wrap='word')
        self.BondsEntry = ctk.CTkTextbox(self, font=self.font, width=250, height=100, border_width=2, wrap='word')
        self.FlawsEntry = ctk.CTkTextbox(self, font=self.font, width=250, height=100, border_width=2, wrap='word')
        self.FeaturesEntry = ctk.CTkTextbox(self, font=self.font, width=250, height=100, border_width=2, wrap='word')
        self.TraitsEntry = ctk.CTkTextbox(self, font=self.font, width=250, height=100, border_width=2, wrap='word')

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
        self.InvestigationButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Investigation", height=6, width=6,
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
        self.IntimidationButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Intimidation", height=6, width=6,
                                                command=lambda: self.update_proficiency(
                                                    skill_label=self.IntimidationLabel, stat_key="CHA",
                                                    skill_key="Intimidation"))
        self.PerformanceButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Performance", height=6, width=6,
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
        self.InvestigationButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Investigation", height=6, width=6,
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
        self.IntimidationButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Intimidation", height=6, width=6,
                                                command=lambda: self.update_proficiency(
                                                    skill_label=self.IntimidationLabel, stat_key="CHA",
                                                    skill_key="Intimidation"))
        self.PerformanceButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Performance", height=6, width=6,
                                               command=lambda: self.update_proficiency(
                                                   skill_label=self.PerformanceLabel, stat_key="CHA",
                                                   skill_key="Performance"))
        self.PersuasionButton = ctk.CTkButton(self.stat_div, font=self.small_font, text="Persuasion", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.PersuasionLabel,
                                                                                      stat_key="CHA",
                                                                                      skill_key="Persuasion"))

        # whitespace labels
        self.whitespace1 = ctk.CTkLabel(self.stat_div, text="            ")

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
        #
        # # column 2
        # # row 1
        # self.PersonalityLabel.grid(row=0, column=0)
        # self.PersonalityEntry.grid(row=0, column=0)
        # # row 2
        # self.IdealsLabel.grid(row=0, column=0)
        # self.IdealsEntry.grid(row=0, column=0)
        # # row 3
        # self.BondsLabel.grid(row=0, column=0)
        # self.BondsEntry.grid(row=0, column=0)
        # # row 4
        # self.FlawsLabel.grid(row=0, column=0)
        # self.FlawsEntry.grid(row=0, column=0)
        # # row 5
        # self.FeaturesLabel.grid(row=0, column=0)
        # self.FeaturesEntry.grid(row=0, column=0)

        # configuring textbox widgets
        self.PersonalityEntry.insert("0.0", self.CC.fields["Attributes"]["Personality"])
        self.IdealsEntry.insert("0.0", self.CC.fields["Attributes"]["Ideals"])
        self.BondsEntry.insert("0.0", self.CC.fields["Attributes"]["Bonds"])
        self.FlawsEntry.insert("0.0", self.CC.fields["Attributes"]["Flaws"])


        # gridding containters
        self.stat_div.grid(row=0, column=0)
        self.attr_div.grid(row=0, column=2, sticky=ctk.N, padx=5)

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


if __name__ == '__main__':
    test = ctk.CTk()
    test.geometry("1280x720")

    ssf = SamsScrollableFrame(test)
    ssf.configure(width=1280)
    ssf.configure(height=720)

    ssf.pack(fill=ctk.BOTH, expand=True)

    test.mainloop()