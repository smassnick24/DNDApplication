import json


class CharacterCreator(object):
    def __init__(self, data_template="characters/character_sheet.json"):
        self.data = data_template
        self.fields = {}

        with open(self.data, 'r') as character:
            self.fields = json.loads(character.read())

    def determine_modifier(self):
        """
        A class method which takes the values of the stats from the current json file
        and calculates the modifiers for each stat.

        This method uses dictionaries to hold stat and modifier values as accessing a dictionary is
        O(1) time, which is just as fast as a normal computation. This avenue removes error
        from calculation as formulas are not always perfect.

        Once all values have been assigned, the json file is updated.

        :return: None
        """
        stats = {"STR": "STR_Mod", "DEX": "DEX_Mod", "CON": "CON_Mod", "INT": "INT_Mod", "WIS": "WIS_Mod",
                 "CHA": "CHA_Mod"}
        modifiers = {'20': '5', '19': '4', '18': '4', '17': '3', '16': '3', '15': '2', '14': '2', '13': '1', '12': '1',
                     '11': '0', '10': '0',
                     '9': '-1', '8': '-1', '7': '-2',
                     '6': '-2', '5': '-3', '4': '-3', '3': '-4', '2': '-4', '1': '-5', '0': '-5'}

        totals = []
        for stat in stats.keys():  # adding the stat values from the json file to the list for iteration
            totals.append(self.fields["Stats"][stat])

        for val, stat_mod in zip(totals, stats.values()):  # calculating the stat modifier
            if int(val) > 20:
                val = "20"
            elif int(val) < 0:
                val = "0"
            self.fields["Stat_Modifiers"][stat_mod] = "+" + modifiers[val] if int(modifiers[val]) >= 0 else modifiers[
                val]

        updated = json.dumps(self.fields, indent=True)
        with open(self.data, 'w') as data:
            data.write(updated)

    def determine_skill(self):
        """
        A class method which calculates the skill modifiers using the previously calculated stat modifiers and
        the character's proficiency bonus.

        This method uses dictionaries for quicker access to leave some running time for the
        nested for loops which run at O(n*m) time.

        Once all skills have been accounted for, the json file is updated.

        :return: None
        """
        skills = {"STR": self.fields["Skills"]["STR"], "DEX": self.fields["Skills"]["DEX"],
                  "INT": self.fields["Skills"]["INT"], "WIS": self.fields["Skills"]["WIS"],
                  "CHA": self.fields["Skills"]["CHA"]}
        mods = []
        prof_bonus = self.fields["Prof_Bonus"]

        for key in self.fields["Stat_Modifiers"].keys():  # collecting modifiers for future use
            if key == "CON":
                continue
            else:
                mods.append(self.fields["Stat_Modifiers"][key])

        for stat, mod in zip(skills.keys(), mods):
            for skill in self.fields["Skills"][stat].keys():
                if self.fields["Skills"][stat][skill]["Proficient"] == 1:
                    total = int(mod) + int(prof_bonus)
                    self.fields["Skills"][stat][skill]["Mod"] = "+" + str(total) if total >= 0 else str(total)
                else:
                    self.fields["Skills"][stat][skill]["Mod"] = mod

        updated = json.dumps(self.fields, indent=True)
        with open(self.data, 'w') as data:
            data.write(updated)



if __name__ == '__main__':
    CharacterCreator().determine_modifier()
    CharacterCreator().determine_skill()
