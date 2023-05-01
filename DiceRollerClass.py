import random as r


class DiceRoller(object):
    def __init__(self):
        self.advantage = False
        self.disadvantage = False
        self.modifier = 0
        self.num_dice = 1

    def RollD4(self):
        dice1 = r.randint(1, 4)  # default dice
        dice2 = r.randint(1, 4)
        total = 0
        for i in range(self.num_dice):
            if self.advantage:
                total += (dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                total += (dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                total += dice1 + self.modifier  # add to total the default dice given that advantage and disadvantage are both false
        return total, self.modifier, self.advantage, self.disadvantage

    def RollD6(self):
        dice1 = r.randint(1, 6)  # default dice
        dice2 = r.randint(1, 6)
        total = 0
        for i in range(self.num_dice):
            if self.advantage:
                total += (dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                total += (dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                total += dice1 + self.modifier  # add to total the default dice given that advantage and disadvantage are both false
        return total, self.modifier, self.advantage, self.disadvantage

    def RollD8(self):
        dice1 = r.randint(1, 8)  # default dice
        dice2 = r.randint(1, 8)
        total = 0
        for i in range(self.num_dice):
            if self.advantage:
                total += (dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                total += (dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                total += dice1 + self.modifier  # add to total the default dice given that advantage and disadvantage are both false
        return total, self.modifier, self.advantage, self.disadvantage

    def RollD10(self):
        dice1 = r.randint(1, 10)  # default dice
        dice2 = r.randint(1, 10)
        total = 0
        for i in range(self.num_dice):
            if self.advantage:
                total += (dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                total += (dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                total += dice1 + self.modifier  # add to total the default dice given that advantage and disadvantage are both false
        return total, self.modifier, self.advantage, self.disadvantage

    def RollD12(self):
        dice1 = r.randint(1, 12)  # default dice
        dice2 = r.randint(1, 12)
        total = 0
        for i in range(self.num_dice):
            if self.advantage:
                total += (dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                total += (dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                total += dice1 + self.modifier  # add to total the default dice given that advantage and disadvantage are both false
        return total, self.modifier, self.advantage, self.disadvantage

    def RollD20(self):
        dice1 = r.randint(1, 20)  # default dice
        dice2 = r.randint(1, 20)
        total = 0
        for i in range(self.num_dice):
            if self.advantage:
                total += (dice1 + self.modifier) if dice1 > dice2 else (dice2 + self.modifier)  # add to the total larger of two values from dice
            elif self.disadvantage:
                total += (dice1 + self.modifier) if dice1 < dice2 else (dice2 + self.modifier)  # add to the total the smaller of two values from dice
            else:
                total += dice1 + self.modifier  # add to total the default dice given that advantage and disadvantage are both false
        return total, self.modifier, self.advantage, self.disadvantage

    def set_modifier(self, mod):
        self.modifier = mod

    def set_num_dice(self, number_of_dice):
        self.num_dice = number_of_dice



if __name__ == '__main__':
    d = DiceRoller()
    d.set_modifier(5)
    print(d.RollD4())
