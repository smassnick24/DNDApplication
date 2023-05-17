from PyPDFForm import PyPDFForm
import json


class FillPDF(object):
    def __init__(self):
        self.template = "template/DnD_5E_CharacterSheet_FormFillable.pdf"
        self.output = "character_sheets/Default.pdf"
        self.form_fields = {
            "CharacterName 2": {},
            "Age": {},
            "Height": {},
            "Weight": {},
            "Eyes": {},
            "Skin": {},
            "Hair": {},
            "Allies": {},
            "FactionName": {},
            "Backstory": {},
            "Feat+Traits": {},
            "Treasure": {},
            "CHARACTER IMAGE": {},
            "Faction Symbol Image": {},
            "ClassLevel": {},
            "Background": {},
            "PlayerName": {},
            "CharacterName": {},
            "Race ": {},
            "Alignment": {},
            "XP": {},
            "Inspiration": {},
            "STR": {},
            "ProfBonus": {},
            "AC": {},
            "Initiative": {},
            "Speed": {},
            "PersonalityTraits ": {},
            "STRmod": {},
            "HPMax": {},
            "ST Strength": {},
            "DEX": {},
            "HPCurrent": {},
            "Ideals": {},
            "DEXmod ": {},
            "HPTemp": {},
            "Bonds": {},
            "CON": {},
            "HDTotal": {},
            "Check Box 12": {},
            "Check Box 13": {},
            "Check Box 14": {},
            "CONmod": {},
            "Check Box 15": {},
            "Check Box 16": {},
            "Check Box 17": {},
            "HD": {},
            "Flaws": {},
            "INT": {},
            "ST Dexterity": {},
            "ST Constitution": {},
            "ST Intelligence": {},
            "ST Wisdom": {},
            "ST Charisma": {},
            "Acrobatics": {},
            "Animal": {},
            "Athletics": {},
            "Deception ": {},
            "History ": {},
            "Insight": {},
            "Intimidation": {},
            "Check Box 11": {},
            "Check Box 18": {},
            "Check Box 19": {},
            "Check Box 20": {},
            "Check Box 21": {},
            "Check Box 22": {},
            "Wpn Name": {},
            "Wpn1 AtkBonus": {},
            "Wpn1 Damage": {},
            "INTmod": {},
            "Wpn Name 2": {},
            "Wpn2 AtkBonus ": {},
            "Wpn2 Damage ": {},
            "Investigation ": {},
            "WIS": {},
            "Wpn Name 3": {},
            "Wpn3 AtkBonus  ": {},
            "Arcana": {},
            "Wpn3 Damage ": {},
            "Perception ": {},
            "WISmod": {},
            "CHA": {},
            "Nature": {},
            "Performance": {},
            "Medicine": {},
            "Religion": {},
            "Stealth ": {},
            "Check Box 23": {},
            "Check Box 24": {},
            "Check Box 25": {},
            "Check Box 26": {},
            "Check Box 27": {},
            "Check Box 28": {},
            "Check Box 29": {},
            "Check Box 30": {},
            "Check Box 31": {},
            "Check Box 32": {},
            "Check Box 33": {},
            "Check Box 34": {},
            "Check Box 35": {},
            "Check Box 36": {},
            "Check Box 37": {},
            "Check Box 38": {},
            "Check Box 39": {},
            "Check Box 40": {},
            "Persuasion": {},
            "SleightofHand": {},
            "CHamod": {},
            "Survival": {},
            "AttacksSpellcasting": {},
            "Passive": {},
            "CP": {},
            "ProficienciesLang": {},
            "SP": {},
            "EP": {},
            "GP": {},
            "PP": {},
            "Equipment": {},
            "Features and Traits": {},
            "Spellcasting Class 2": {},
            "SpellcastingAbility 2": {},
            "SpellSaveDC  2": {},
            "SpellAtkBonus 2": {},
            "SlotsTotal 19": {},
            "SlotsRemaining 19": {},

        }

    @staticmethod
    def _gather_input(form_field):
        data = input(f"{form_field}")
        return data

    def update_fields(self):
        fields_to_fill = ["CharacterName", "ClassLevel", "Background", "PlayerName", "Race ",
                          "Alignment", "XP", "STR", "DEX", "CON", "INT", "WIS", "CHA", "ProfBonus",
                          "PersonalityTraits ", "Ideals", "Bonds", "Flaws"]

        field_inquiries = {"CharacterName": "What is the name of your character?: ",
                           "ClassLevel": "What is the Class and Level of your character?: ",
                           "Background": "What is the character's Background?: ",
                           "PlayerName": "Who is playing this character?: ",
                           "Race ": "What is the race of your character?: ",
                           "Alignment": "What is your character's Alignment?: ",
                           "XP": "What is the current XP of the character?: ",
                           "STR": "What is the character's Strength?: ",
                           "DEX": "What is the character's Dexterity?: ",
                           "CON": "What is the character's Constitution?: ",
                           "INT": "What is the character's Intelligence?: ",
                           "WIS": "What is the character's Wisdom?: ",
                           "CHA": "What is the character's Charisma?: ",
                           "ProfBonus": "What is the character's Proficiency Bonus?: ",
                           "PersonalityTraits ": "What are some Personality Traits of your character?: ",
                           "Ideals": "What are some Ideals of your character?: ",
                           "Bonds": "What are some Bonds of your character?: ",
                           "Flaws": "What are some Flaws of your character?: "}

        stat_fields = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0,
            "Initiative": 0,
            "Speed": 0
        }

        filled = {}

        # self._determine_stat_mods(stat_fields)

        for field in fields_to_fill:
            filled[field] = self._gather_input(field_inquiries[field])

        self.form_fields.update(filled)

        with open(self.output, "wb") as out:
            out.write(PyPDFForm(self.template).fill(self.form_fields).read())

    # @staticmethod
    # def _determine_stat_mods(stat_dict: dict):
    #     stat_vals = stat_dict.values()

if __name__ == '__main__':
    test = FillPDF()
    test.update_fields()