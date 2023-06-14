import tkinter as tk
import customtkinter as ctk
from CreateCharacterClass import CharacterCreator

ctk.set_appearance_mode("Light")


class StatEntryFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # allowing the new frame to have a CTk obj as a master
        self.master = master

        # defining character creator
        self.CC = CharacterCreator()

        # declaring fonts
        self.small_font = ctk.CTkFont(family="Rockwell", size=10)
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
        self.EquipmentLabel = ctk.CTkLabel(self, font=self.font, text="Equipment")
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
        self.NameVar = ctk.StringVar(value="")
        self.ClassVar = ctk.StringVar(value="")
        self.LevelVar = ctk.IntVar(value=1)
        self.RaceVar = ctk.StringVar(value="")
        self.BackgroundVar = ctk.StringVar(value="")
        self.AlignmentVar = ctk.StringVar(value="")
        self.PersonalityVar = ctk.StringVar(value="")
        self.IdealsVar = ctk.StringVar(value="")
        self.BondsVar = ctk.StringVar(value="")
        self.FlawsVar = ctk.StringVar(value="")
        self.FeaturesVar = ctk.StringVar(value="")
        self.TraitsVar = ctk.StringVar(value="")
        self.EquipmentVar = ctk.StringVar(value="")
        self.Attack1Var = ctk.StringVar(value="")
        self.Attack2Var = ctk.StringVar(value="")
        self.Attack3Var = ctk.StringVar(value="")
        self.STRVar = ctk.IntVar(value=10)
        self.CONVar = ctk.IntVar(value=10)
        self.DEXVar = ctk.IntVar(value=10)
        self.INTVar = ctk.IntVar(value=10)
        self.WISVar = ctk.IntVar(value=10)
        self.CHAVar = ctk.IntVar(value=10)
        self.ACVar = ctk.StringVar(value="")
        self.SpeedVar = ctk.StringVar(value="0ft")
        self.ProfBonusVar = ctk.StringVar(value="")
        self.HPMaxVar = ctk.IntVar(value=0)
        self.HPCurrVar = ctk.IntVar(value=0)
        self.HPTempVar = ctk.IntVar(value=0)
        self.HDTotVar = ctk.IntVar(value=0)
        self.HDCurrVar = ctk.IntVar(value=0)
        self.ElecVar = ctk.IntVar(value=0)
        self.PlatVar = ctk.IntVar(value=0)
        self.GoldVar = ctk.IntVar(value=0)
        self.SilvVar = ctk.IntVar(value=0)
        self.CoppVar = ctk.IntVar(value=0)
        # death saves

        # entry widgets
        self.NameEntry = ctk.CTkEntry(self, font=self.font, textvariable=self.NameVar)
        self.ClassEntry = ctk.CTkEntry(self, font=self.font, textvariable=self.ClassVar)
        self.LevelEntry = ctk.CTkEntry(self, font=self.font, textvariable=self.LevelVar)
        self.RaceEntry = ctk.CTkEntry(self, font=self.font, textvariable=self.RaceVar)
        self.BackgroundEntry = ctk.CTkEntry(self, font=self.font, textvariable=self.RaceVar)
        self.AlignmentEntry = ctk.CTkEntry(self, font=self.font, textvariable=self.RaceVar)

        # skill prof labels
        self.SkillsLabel = ctk.CTkLabel(self, font=self.font, text="Skills")
        self.AthleticsLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.AcrobaticsLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.SOHLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.StealthLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.ArcanaLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.HistoryLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.InvestigationLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.NatureLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.ReligionLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.AHLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.InsightLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.MedicineLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.PerceptionLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.SurvivalLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.DeceptionLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.IntimidationLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.PerformanceLabel = ctk.CTkLabel(self, font=self.font, text="( )")
        self.PersuasionLabel = ctk.CTkLabel(self, font=self.font, text="( )")

        # buttons for skill proficiencies
        self.AthleticsButton = ctk.CTkButton(self, font=self.small_font, text="Athletics", height=6, width=6,
                                             command=lambda: self.update_proficiency(skill_label=self.AthleticsLabel,
                                                                                     stat_key="STR",
                                                                                     skill_key="Athletics"))
        self.AcrobaticsButton = ctk.CTkButton(self, font=self.small_font, text="Acrobatics", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.AcrobaticsLabel,
                                                                                      stat_key="DEX",
                                                                                      skill_key="Acrobatics"))
        self.SOHButton = ctk.CTkButton(self, font=self.small_font, text="Slight of Hand", height=6, width=6,
                                       command=lambda: self.update_proficiency(skill_label=self.SOHLabel,
                                                                               stat_key="DEX",
                                                                               skill_key="Slight_of_Hand"))
        self.StealthButton = ctk.CTkButton(self, font=self.small_font, text="Stealth", height=6, width=6,
                                           command=lambda: self.update_proficiency(skill_label=self.StealthLabel,
                                                                                   stat_key="DEX", skill_key="Stealth"))
        self.ArcanaButton = ctk.CTkButton(self, font=self.small_font, text="Arcana", height=6, width=6,
                                          command=lambda: self.update_proficiency(skill_label=self.ArcanaLabel,
                                                                                  stat_key="INT", skill_key="Arcana"))
        self.HistoryButton = ctk.CTkButton(self, font=self.small_font, text="History", height=6, width=6,
                                           command=lambda: self.update_proficiency(skill_label=self.HistoryLabel,
                                                                                   stat_key="INT", skill_key="History"))
        self.InvestigationButton = ctk.CTkButton(self, font=self.small_font, text="Investigation", height=6, width=6,
                                                 command=lambda: self.update_proficiency(
                                                     skill_label=self.InvestigationLabel, stat_key="INT",
                                                     skill_key="Investigation"))
        self.NatureButton = ctk.CTkButton(self, font=self.small_font, text="Nature", height=6, width=6,
                                          command=lambda: self.update_proficiency(skill_label=self.NatureLabel,
                                                                                  stat_key="INT", skill_key="Nature"))
        self.ReligionButton = ctk.CTkButton(self, font=self.small_font, text="Religion", height=6, width=6,
                                            command=lambda: self.update_proficiency(skill_label=self.ReligionLabel,
                                                                                    stat_key="INT",
                                                                                    skill_key="Religion"))
        self.AHButton = ctk.CTkButton(self, font=self.small_font, text="Animal Handling", height=6, width=6,
                                      command=lambda: self.update_proficiency(skill_label=self.AHLabel, stat_key="WIS",
                                                                              skill_key="Animal_Handling"))
        self.InsightButton = ctk.CTkButton(self, font=self.small_font, text="Insight", height=6, width=6,
                                           command=lambda: self.update_proficiency(skill_label=self.InsightLabel,
                                                                                   stat_key="WIS", skill_key="Insight"))
        self.MedicineButton = ctk.CTkButton(self, font=self.small_font, text="Medicine", height=6, width=6,
                                            command=lambda: self.update_proficiency(skill_label=self.MedicineLabel,
                                                                                    stat_key="WIS",
                                                                                    skill_key="Medicine"))
        self.PerceptionButton = ctk.CTkButton(self, font=self.small_font, text="Perception", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.PerceptionLabel,
                                                                                      stat_key="WIS",
                                                                                      skill_key="Perception"))
        self.SurvivalButton = ctk.CTkButton(self, font=self.small_font, text="Survival", height=6, width=6,
                                            command=lambda: self.update_proficiency(skill_label=self.SurvivalLabel,
                                                                                    stat_key="WIS",
                                                                                    skill_key="Survival"))
        self.DeceptionButton = ctk.CTkButton(self, font=self.small_font, text="Deception", height=6, width=6,
                                             command=lambda: self.update_proficiency(skill_label=self.DeceptionLabel,
                                                                                     stat_key="CHA",
                                                                                     skill_key="Deception"))
        self.IntimidationButton = ctk.CTkButton(self, font=self.small_font, text="Intimidation", height=6, width=6,
                                                command=lambda: self.update_proficiency(
                                                    skill_label=self.IntimidationLabel, stat_key="CHA",
                                                    skill_key="Intimidation"))
        self.PerformanceButton = ctk.CTkButton(self, font=self.small_font, text="Performance", height=6, width=6,
                                               command=lambda: self.update_proficiency(
                                                   skill_label=self.PerformanceLabel, stat_key="CHA",
                                                   skill_key="Performance"))
        self.PersuasionButton = ctk.CTkButton(self, font=self.small_font, text="Persuasion", height=6, width=6,
                                              command=lambda: self.update_proficiency(skill_label=self.PersuasionLabel,
                                                                                      stat_key="CHA",
                                                                                      skill_key="Persuasion"))

        # placing attributes on the frame
        self.SkillsLabel.place(x=175, y=20)
        self.AthleticsLabel.place(x=175, y=43)
        self.AthleticsButton.place(x=200, y=50)
        self.AcrobaticsLabel.place(x=175, y=69)
        self.AcrobaticsButton.place(x=200, y=75)
        self.SOHLabel.place(x=175, y=95)
        self.SOHButton.place(x=200, y=100)
        self.StealthLabel.place(x=175, y=119)
        self.StealthButton.place(x=200, y=125)
        self.ArcanaLabel.place(x=175, y=144)
        self.ArcanaButton.place(x=200, y=150)
        self.HistoryLabel.place(x=175, y=168)
        self.HistoryButton.place(x=200, y=175)
        self.InvestigationLabel.place(x=175, y=193)
        self.InvestigationButton.place(x=200, y=200)
        self.NatureLabel.place(x=175, y=218)
        self.NatureButton.place(x=200, y=225)
        self.ReligionLabel.place(x=175, y=243)
        self.ReligionButton.place(x=200, y=250)
        self.AHLabel.place(x=175, y=268)
        self.AHButton.place(x=200, y=275)
        self.InsightLabel.place(x=175, y=293)
        self.InsightButton.place(x=200, y=300)
        self.MedicineLabel.place(x=175, y=318)
        self.MedicineButton.place(x=200, y=325)
        self.PerceptionLabel.place(x=175, y=343)
        self.PerceptionButton.place(x=200, y=350)
        self.SurvivalLabel.place(x=175, y=368)
        self.SurvivalButton.place(x=200, y=375)
        self.DeceptionLabel.place(x=175, y=393)
        self.DeceptionButton.place(x=200, y=400)
        self.IntimidationLabel.place(x=175, y=418)
        self.IntimidationButton.place(x=200, y=425)
        self.PerformanceLabel.place(x=175, y=443)
        self.PerformanceButton.place(x=200, y=450)
        self.PersuasionLabel.place(x=175, y=468)
        self.PersuasionButton.place(x=200, y=475)

    # defining class methods
    def update_proficiency(self, skill_label: ctk.CTkLabel, stat_key, skill_key):
        if skill_label.cget("text") == "( )":
            skill_label.configure(text="(o)")
            self.CC.fields["Skills"][stat_key][skill_key]["Proficient"] = 1
            print(self.CC.fields["Skills"][stat_key][skill_key])
        else:
            skill_label.configure(text="( )")
            self.CC.fields["Skills"][stat_key][skill_key]["Proficient"] = 0
            print(self.CC.fields["Skills"][stat_key][skill_key])


if __name__ == '__main__':
    test = ctk.CTk()
    frame = StatEntryFrame(master=test)
    test.geometry("1422x603")
    test.iconbitmap("dice-icon.ico")
    test.title("DND App")
    frame.pack(fill=ctk.BOTH, expand=True)

    test.mainloop()
