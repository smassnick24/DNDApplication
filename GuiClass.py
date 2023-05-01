import tkinter as tk
import customtkinter as ctk
from DiceRollerClass import DiceRoller


class DiceRollFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # house-keeping
        self.master = master
        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.special_font = ctk.CTkFont(family="Rockwell", size=18)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)
        self.DiceRoller = DiceRoller()
        self.modifier = ctk.StringVar(value="0")
        self.num_dice = ctk.StringVar(value="1")
        self.advantage = False
        self.disadvantage = False

        # button widgets
        self.RollD4 = ctk.CTkButton(self, text="Roll D4", font=self.font, width=20, corner_radius=8,
                                    command=self.RollD4)
        self.RollD6 = ctk.CTkButton(self, text="Roll D6", font=self.font, width=20, corner_radius=8,
                                    command=self.RollD6)
        self.RollD8 = ctk.CTkButton(self, text="Roll D8", font=self.font, width=20, corner_radius=8,
                                    command=self.RollD8)
        self.RollD10 = ctk.CTkButton(self, text="Roll D10", font=self.font, width=20, corner_radius=8,
                                     command=self.RollD10)
        self.RollD12 = ctk.CTkButton(self, text="Roll D12", font=self.font, width=20, corner_radius=8,
                                     command=self.RollD12)
        self.RollD20 = ctk.CTkButton(self, text="Roll D20", font=self.font, width=20, corner_radius=8,
                                     command=self.RollD20)

        # entry widgets
        self.EnterModifier = ctk.CTkEntry(self, font=self.font, textvariable=self.modifier)
        self.EnterNumDice = ctk.CTkEntry(self, font=self.font, textvariable=self.num_dice)

        # label widgets
        self.Header = ctk.CTkLabel(self, font=self.header_font, text="Dice Roller")
        self.ModLabel = ctk.CTkLabel(self, font=self.font, text="Modifier:")
        self.NumDiceLabel = ctk.CTkLabel(self, font=self.font, text="Number of Dice: ")
        self.AdvantageLabel = ctk.CTkLabel(self, font=self.special_font, text="{False}")
        self.DisadvantageLabel = ctk.CTkLabel(self, font=self.special_font, text="{False}")
        self.Result = ctk.CTkLabel(self, font=self.header_font, text="Result: {}")
        self.LastModifier = ctk.CTkLabel(self, font=self.header_font, text="Modifier: {}")
        self.VantageLabelADV = ctk.CTkLabel(self, font=self.header_font, text="Advantage: {}")
        self.VantageLabelDIS = ctk.CTkLabel(self, font=self.header_font, text="Disadvantage: {}")
        self.RecentRolls = ctk.CTkLabel(self, font=self.font, text="Recent Rolls")
        self.Recent1 = ctk.CTkLabel(self, font=self.font, text="1")
        self.Recent2 = ctk.CTkLabel(self, font=self.font, text="2")
        self.Recent3 = ctk.CTkLabel(self, font=self.font, text="3")
        self.Status = ctk.CTkLabel(self, font=self.special_font, text="Status: {}")

        # radio buttons
        self.Advantage = ctk.CTkButton(self, text="Advantage", width=30, font=self.font, command=self._set_advantage)
        self.Disadvantage = ctk.CTkButton(self, text="Disadvantage", width=30, font=self.font,
                                          command=self._set_disadvantage)

        # placing items
        self.Header.place(x=480, y=0)

        # dice buttons
        self.RollD4.place(x=20, y=100)
        self.RollD6.place(x=20, y=138)
        self.RollD8.place(x=20, y=176)
        self.RollD10.place(x=20, y=214)
        self.RollD12.place(x=20, y=252)
        self.RollD20.place(x=20, y=290)

        # radio group
        self.Advantage.place(x=100, y=100)
        self.Disadvantage.place(x=100, y=138)

        # entry widget
        self.NumDiceLabel.place(x=20, y=15)
        self.EnterNumDice.place(x=130, y=15)
        self.EnterModifier.place(x=100, y=50)
        self.ModLabel.place(x=20, y=50)

        # placing labels
        self.AdvantageLabel.place(x=220, y=100)
        self.DisadvantageLabel.place(x=220, y=138)
        self.Status.place(x=480, y=500)

        self.Result.place(x=480, y=250)
        self.LastModifier.place(x=480, y=300)
        self.VantageLabelADV.place(x=480, y=350)
        self.VantageLabelDIS.place(x=480, y=400)

    def RollD4(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage = self.DiceRoller.RollD4()
        self.Result.configure(text=f"Result: {total}")
        self.LastModifier.configure(text=f"Modifier: {modifier}")
        self.VantageLabelADV.configure(text=f"Advantage: {advantage}")
        self.VantageLabelDIS.configure(text=f"Disadvantage: {disadvantage}")

    def RollD6(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage = self.DiceRoller.RollD6()
        self.Result.configure(text=f"Result: {total}")
        self.LastModifier.configure(text=f"Modifier: {modifier}")
        self.VantageLabelADV.configure(text=f"Advantage: {advantage}")
        self.VantageLabelDIS.configure(text=f"Disadvantage: {disadvantage}")

    def RollD8(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage = self.DiceRoller.RollD8()
        self.Result.configure(text=f"Result: {total}")
        self.LastModifier.configure(text=f"Modifier: {modifier}")
        self.VantageLabelADV.configure(text=f"Advantage: {advantage}")
        self.VantageLabelDIS.configure(text=f"Disadvantage: {disadvantage}")

    def RollD10(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage = self.DiceRoller.RollD10()
        self.Result.configure(text=f"Result: {total}")
        self.LastModifier.configure(text=f"Modifier: {modifier}")
        self.VantageLabelADV.configure(text=f"Advantage: {advantage}")
        self.VantageLabelDIS.configure(text=f"Disadvantage: {disadvantage}")

    def RollD12(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage = self.DiceRoller.RollD12()
        self.Result.configure(text=f"Result: {total}")
        self.LastModifier.configure(text=f"Modifier: {modifier}")
        self.VantageLabelADV.configure(text=f"Advantage: {advantage}")
        self.VantageLabelDIS.configure(text=f"Disadvantage: {disadvantage}")

    def RollD20(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage = self.DiceRoller.RollD20()
        self.Result.configure(text=f"Result: {total}")
        self.LastModifier.configure(text=f"Modifier: {modifier}")
        self.VantageLabelADV.configure(text=f"Advantage: {advantage}")
        self.VantageLabelDIS.configure(text=f"Disadvantage: {disadvantage}")

    def _set_advantage(self):
        if not self.advantage:
            self.advantage = True
            self.disadvantage = False
            self.DiceRoller.advantage = True
            self.DiceRoller.disadvantage = False
            self.AdvantageLabel.configure(text="{True}")
            self.DisadvantageLabel.configure(text="{False}")
            # print(f"Advantage: {self.advantage}")
            # print(f"Disadvantage: {self.disadvantage}")
        else:
            self.advantage = False
            self.DiceRoller.advantage = False
            self.AdvantageLabel.configure(text="{False}")
            pass

    def _set_disadvantage(self):
        if not self.disadvantage:
            self.disadvantage = True
            self.advantage = False
            self.DiceRoller.advantage = True
            self.DiceRoller.disadvantage = False
            self.AdvantageLabel.configure(text="{False}")
            self.DisadvantageLabel.configure(text="{True}")
            # print(f"Advantage: {self.advantage}")
            # print(f"Disadvantage: {self.disadvantage}")
        else:
            self.disadvantage = False
            self.DiceRoller.disadvantage = False
            self.DisadvantageLabel.configure(text="{False}")
            pass

    def _set_num_dice(self):
        storage = self.num_dice.get()
        self.EnterNumDice.delete(0, ctk.END)
        self.num_dice.set(value="1")
        # print(f"Num: {storage}")
        if storage.isdigit():
            storage = int(storage)
            if storage < 0:
                storage = abs(storage)
                if storage > 2 ** 16:
                    storage = 2 ** 16
                    return storage
                else:
                    return storage
            else:
                if storage > 2 ** 16:
                    storage = 2 ** 16
                    return storage
                else:
                    return storage
        else:
            self.Status.configure(text="Status: {Invalid Number of Dice}")

    def _set_modifier(self):
        storage = self.modifier.get()
        self.EnterModifier.delete(0, ctk.END)
        self.modifier.set(value="0")
        # print(f"Mod: {storage}")
        if storage.isdigit():
            storage = int(storage)
            if storage > 2 ** 16:
                return 2 ** 16
            elif storage < (2 ** 16) * -1:
                return (2 ** 16) * -1
            else:
                return storage
        else:
            self.Status.configure(text="Status: {Invalid Modifier}")


if __name__ == '__main__':
    t = ctk.CTk()
    f = DiceRollFrame(master=t)
    t.geometry("1072x603")
    f.pack(fill=ctk.BOTH, expand=True)

    t.mainloop()
