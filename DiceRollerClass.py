import random as r


class DiceRoller(object):
    def __init__(self):
        self.advantage = False
        self.disadvantage = False
        self.modifier = 0
        self.num_dice = 1

    def RollD4(self):
        total = 0
        rolls = []
        for i in range(self.num_dice):
            dice1 = r.randint(1, 4)  # default dice
            dice2 = r.randint(1, 4)
            if self.advantage:
                rolls.append((dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                rolls.append((dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                rolls.append(dice1 + self.modifier)
                total += dice1 + self.modifier  # add to total the default dice given that advantage and disadvantage are both false
        if len(rolls) > 12:
            rolls = rolls[0: 11]
        return total, self.modifier, self.advantage, self.disadvantage, rolls

    def RollD6(self):
        total = 0
        rolls = []
        for i in range(self.num_dice):
            dice1 = r.randint(1, 6)  # default dice
            dice2 = r.randint(1, 6)
            if self.advantage:
                rolls.append((dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 > dice2 else (
                            dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                rolls.append((dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 < dice2 else (
                            dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                rolls.append(dice1 + self.modifier)
                total += dice1 + self.modifier
        if len(rolls) > 12:
            rolls = rolls[0:11]
        return total, self.modifier, self.advantage, self.disadvantage, rolls

    def RollD8(self):
        total = 0
        rolls = []
        for i in range(self.num_dice):
            dice1 = r.randint(1, 8)  # default dice
            dice2 = r.randint(1, 8)
            if self.advantage:
                rolls.append((dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 > dice2 else (
                            dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                rolls.append((dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 < dice2 else (
                            dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                rolls.append(dice1 + self.modifier)
                total += dice1 + self.modifier
        if len(rolls) > 12:
            rolls = rolls[0:11]
        return total, self.modifier, self.advantage, self.disadvantage, rolls

    def RollD10(self):
        total = 0
        rolls = []
        for i in range(self.num_dice):
            dice1 = r.randint(1, 10)  # default dice
            dice2 = r.randint(1, 10)
            if self.advantage:
                rolls.append((dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 > dice2 else (
                            dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                rolls.append((dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 < dice2 else (
                            dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                rolls.append(dice1 + self.modifier)
                total += dice1 + self.modifier
        if len(rolls) > 12:
            rolls = rolls[0:11]
        return total, self.modifier, self.advantage, self.disadvantage, rolls

    def RollD12(self):
        total = 0
        rolls = []
        for i in range(self.num_dice):
            dice1 = r.randint(1, 12)  # default dice
            dice2 = r.randint(1, 12)
            if self.advantage:
                rolls.append((dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 > dice2 else (
                            dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                rolls.append((dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 < dice2 else (
                            dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                rolls.append(dice1 + self.modifier)
                total += dice1 + self.modifier
        if len(rolls) > 12:
            rolls = rolls[0:11]
        return total, self.modifier, self.advantage, self.disadvantage, rolls

    def RollD20(self):
        total = 0
        rolls = []
        for i in range(self.num_dice):
            dice1 = r.randint(1, 20)  # default dice
            dice2 = r.randint(1, 20)
            if self.advantage:
                rolls.append((dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 > dice2 else (
                            dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                rolls.append((dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 < dice2 else (
                            dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                rolls.append(dice1 + self.modifier)
                total += dice1 + self.modifier
        if len(rolls) > 12:
            rolls = rolls[0:11]
        return total, self.modifier, self.advantage, self.disadvantage, rolls

    def RollD100(self):
        total = 0
        rolls = []
        for i in range(self.num_dice):
            dice1 = r.randint(1, 100)  # default dice
            dice2 = r.randint(1, 100)
            if self.advantage:
                rolls.append((dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 > dice2 else (
                        dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                rolls.append((dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier))
                total += (dice1 + self.modifier) if dice1 < dice2 else (
                        dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                rolls.append(dice1 + self.modifier)
                total += dice1 + self.modifier
        if len(rolls) > 12:
            rolls = rolls[0:11]
        return total, self.modifier, self.advantage, self.disadvantage, rolls

    def set_modifier(self, mod):
        self.modifier = mod

    def set_num_dice(self, number_of_dice):
        self.num_dice = number_of_dice


