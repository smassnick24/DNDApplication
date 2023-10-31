import json


class DataHandler(object):
    def __init__(self, character_name="character_sheet", ):
        self.data = f"characters/{character_name}.json"
        self.fields = {}

        with open(self.data, 'r') as character:
            self.fields = json.loads(character.read())

    def update_stats(self, values: list):
        """
        A class method which takes a list of ints, the value for stats,
        and inserts them into self.fields and updates the json file which stores
        the data for the character.

        The method has some validation in case an edgecase makes it past the validation
        from the StatEntryFrame methods.

        :param values: list of int
        :return:
        """
        stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for stat, val in zip(stats, values):
            try:
                if len(val) > 2:
                    val = val[0:2]
                val = int(val)
            except ValueError:
                val = 0
            self.fields["Stats"][stat] = str(val)

        self._determine_modifier()
        self._determine_skill()

        self.update_json()

    def update_cantrip(self, values: list):
        count = 0
        for val in values:
            self.fields["Spells"]["Cantrips"][f'Cantrip_Slot_{count}'] = val
            count += 1

    def update_spells(self, values: list, level: str):
        count = 0
        for val in values:
            self.fields["Spells"][level][f'Spell_Slot_{count}'] = val
            count += 1

    def update_attributes(self, values: list):
        attributes = ["Character_Name", "Class", "Level", "Race", "Background",
                      "Alignment", "Experience", "Personality", "Ideals",
                      "Bonds", "Flaws", "Features", "Traits"]

        for attr, val in zip(attributes, values):
            self.fields["Attributes"][attr] = val

        self.update_json()

    def update_attacks(self, values: list):
        arr = ["Equipment", "Attack_1", "Attack_2", "Attack_3", "Attack_1_Bonus", "Attack_2_Bonus", "Attack_3_Bonus",
                  "Attack_1_Type", "Attack_2_Type", "Attack_3_Type"]
        for attr, val in zip(arr, values):
            self.fields["Attacks"][attr] = val

    def update_money(self, values: list):
        arr = ["Copper", "Silver", "Electrum", "Gold", "Platinum"]
        for attr, val in zip(arr, values):
            try:
                val = int(val)
            except ValueError:
                val = 0

            self.fields["Equipment"][attr] = val

    def update_hit_points(self, values: list):
        arr = ["HP_Max", "HP_Curr", "HP_Temp"]
        for attr, val in zip(arr, values):
            self.fields["HitPoints"][attr] = val

    def update_hit_dice(self, values: list):
        arr = ["HD_Total", "HD_Curr"]
        for attr, val in zip(arr, values):
            self.fields["HitDice"][attr] = val

    def update_death_saves(self, values: list):
        pass

    def update_auxiliary(self, values: list):
        pass


    def update_prof_bonus(self, value: str):
        if value == "" or value == " ":
            value = "0"
        self.fields["Auxiliary"]["Prof_Bonus"] = value
        self.update_json()

    def update_json(self):
        """
        Helper method to update the json file.
        This method is mainly for reducing redundancy.
        :return:
        """
        updated = json.dumps(self.fields, indent=True)
        with open(self.data, 'w') as data:
            data.write(updated)



    def _determine_modifier(self):
        """
        A helper method which takes the values of the stats from the current json file
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

    def _determine_skill(self):
        """
        A helper method which calculates the skill modifiers using the previously calculated stat modifiers and
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
        prof_bonus = self.fields["Auxiliary"]["Prof_Bonus"]

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
