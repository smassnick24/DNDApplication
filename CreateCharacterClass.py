from PyPDFForm import PyPDFForm
import json


class CharacterCreator(object):
    def __init__(self, data_template="character_sheet.json"):
        self.template = "template/DnD_5E_CharacterSheet_FormFillable.pdf"
        self.data = data_template
        self.fields = {}

        with open(self.data, 'r') as character:
            self.fields = json.loads(character.read())

    def determine_modifier(self):
        stats = {"STR": "STR_Mod", "DEX": "DEX_Mod", "CON": "CON_Mod", "INT": "INT_Mod", "WIS": "WIS_Mod",
                 "CHA": "CHA_Mod"}
        modifiers = {'20': '5', '19': '4', '18': '4', '17': '3', '16': '3', '15': '2', '14': '2', '13': '1', '12': '1',
                     '11': '0', '10': '0',
                     '9': '-1', '8': '-1', '7': '-2',
                     '6': '-2', '5': '-3', '4': '-3', '3': '-4', '2': '-4', '1': '-5'}

        totals = []
        for stat in stats.keys():  # adding the stat values from the json file to the list for iteration
            totals.append(self.fields[stat])

        for val, stat_mod in zip(totals, stats.values()):  # calculating the stat modifier
            self.fields[stat_mod] = "+" + modifiers[val] if int(modifiers[val]) >= 0 else modifiers[val]

        updated = json.dumps(self.fields, indent=True)
        with open(self.data, 'w') as data:
            data.write(updated)

    def update_fields(self, data: dict):
        updated_data = json.dumps(self.fields, indent=True)
        with open(self.data, 'w') as to_update:
            to_update.write(updated_data)


if __name__ == '__main__':
    CharacterCreator().determine_modifier()
