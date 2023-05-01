import tkinter as tk
import customtkinter
import customtkinter as ctk
from DiceRollerClass import DiceRoller

customtkinter.set_appearance_mode("Light")


class DiceRollFrame(tk.Frame):
    def __init__(self, master=None, dm=False):
        super().__init__(master)
        # house-keeping
        self.master = master
        self.dm = dm
        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.special_font = ctk.CTkFont(family="Rockwell", size=18)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)
        self.DiceRoller = DiceRoller()
        self.modifier = ctk.StringVar(value="0")
        self.num_dice = ctk.StringVar(value="1")
        self.advantage = False
        self.disadvantage = False
        self.count = 0
        self.recent_rolls = []

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
        self.RollD100 = ctk.CTkButton(self, text="Roll D100", font=self.font, width=20, corner_radius=8,
                                      command=self.RollD100)

        # entry widgets
        self.EnterModifier = ctk.CTkEntry(self, font=self.font, textvariable=self.modifier)
        self.EnterNumDice = ctk.CTkEntry(self, font=self.font, textvariable=self.num_dice)

        # label widgets
        self.Header = ctk.CTkLabel(self, font=self.header_font, text="Dice Roller")
        self.ModLabel = ctk.CTkLabel(self, font=self.font, text="Modifier:")
        self.NumDiceLabel = ctk.CTkLabel(self, font=self.font, text="Number of Dice: ")
        self.AdvantageLabel = ctk.CTkLabel(self, font=self.special_font, text="{False}")
        self.DisadvantageLabel = ctk.CTkLabel(self, font=self.special_font, text="{False}")
        self.Result = ctk.CTkLabel(self, width=200, height=75, corner_radius=50, font=self.header_font,
                                   fg_color="#3B8ED0", text_color="white", text="Result: {}")
        self.RecentRolls = ctk.CTkLabel(self, font=self.special_font, text="Recent Rolls")
        self.Recent1 = ctk.CTkLabel(self, font=self.special_font, width=500, corner_radius=25, fg_color="#3B8ED0",
                                    text_color="white",
                                    text="Total: 0, Dice: A x B, Modifier: 0, Advantage: False, Disadvantage: False")
        self.Recent2 = ctk.CTkLabel(self, font=self.special_font, width=500, corner_radius=25, fg_color="#3B8ED0",
                                    text_color="white",
                                    text="Total: 0, Dice: A x B, Modifier: 0, Advantage: False, Disadvantage: False")
        self.Recent3 = ctk.CTkLabel(self, font=self.special_font, width=500, corner_radius=25, fg_color="#3B8ED0",
                                    text_color="white",
                                    text="Total: 0, Dice: A x B, Modifier: 0, Advantage: False, Disadvantage: False")
        self.Recent4 = ctk.CTkLabel(self, font=self.special_font, width=500, corner_radius=25, fg_color="#3B8ED0",
                                    text_color="white",
                                    text="Total: 0, Dice: A x B, Modifier: 0, Advantage: False, Disadvantage: False")
        self.Recent5 = ctk.CTkLabel(self, font=self.special_font, width=500, corner_radius=25, fg_color="#3B8ED0",
                                    text_color="white",
                                    text="Total: 0, Dice: A x B, Modifier: 0, Advantage: False, Disadvantage: False")
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
        if self.dm:
            self.RollD100.place(x=20, y=328)

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

        self.Result.place(x=480, y=100)

        self.RecentRolls.place(x=480, y=210)
        self.Recent1.place(x=480, y=250)
        self.Recent2.place(x=480, y=290)
        self.Recent3.place(x=480, y=330)
        self.Recent4.place(x=480, y=370)
        self.Recent5.place(x=480, y=410)

    def RollD4(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage, info = self.DiceRoller.RollD4()
        self.recent_rolls.append([total, modifier, advantage, disadvantage, info])
        self.Result.configure(text=f"Result: {total}")
        self._update_roll_labels()

    def RollD6(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage, info = self.DiceRoller.RollD6()
        self.recent_rolls.append([total, modifier, advantage, disadvantage, info])
        self.Result.configure(text=f"Result: {total}")
        self._update_roll_labels()

    def RollD8(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage, info = self.DiceRoller.RollD8()
        self.recent_rolls.append([total, modifier, advantage, disadvantage, info])
        self.Result.configure(text=f"Result: {total}")
        self._update_roll_labels()

    def RollD10(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage, info = self.DiceRoller.RollD10()
        self.recent_rolls.append([total, modifier, advantage, disadvantage, info])
        self.Result.configure(text=f"Result: {total}")
        self._update_roll_labels()

    def RollD12(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage, info = self.DiceRoller.RollD12()
        self.recent_rolls.append([total, modifier, advantage, disadvantage, info])
        self.Result.configure(text=f"Result: {total}")
        self._update_roll_labels()

    def RollD20(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage, info = self.DiceRoller.RollD20()
        self.recent_rolls.append([total, modifier, advantage, disadvantage, info])
        self.Result.configure(text=f"Result: {total}")
        self._update_roll_labels()

    def RollD100(self):
        self.DiceRoller.num_dice = self._set_num_dice()
        self.DiceRoller.modifier = self._set_modifier()
        total, modifier, advantage, disadvantage, info = self.DiceRoller.RollD100()
        self.recent_rolls.append([total, modifier, advantage, disadvantage, info])
        self.Result.configure(text=f"Result: {total}")
        self._update_roll_labels()

    def _update_roll_labels(self):
        label_list = [self.Recent1, self.Recent2, self.Recent3, self.Recent4, self.Recent5]
        to_display = self.recent_rolls.pop(len(self.recent_rolls) - 1)
        label_list[self.count % 5].configure(
            text=f"Total: {to_display[0]}, Dice: {to_display[4]}, Modifier: {to_display[1]}, Advantage: {to_display[2]}, Disadvantage: {to_display[3]}")
        self.count += 1

    def _set_advantage(self):
        if not self.advantage:
            self.advantage = True
            self.disadvantage = False
            self.DiceRoller.advantage = True
            self.DiceRoller.disadvantage = False
            self.AdvantageLabel.configure(text="{True}")
            self.DisadvantageLabel.configure(text="{False}")
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
        else:
            self.disadvantage = False
            self.DiceRoller.disadvantage = False
            self.DisadvantageLabel.configure(text="{False}")
            pass

    def _set_num_dice(self):
        storage = self.num_dice.get()
        self.EnterNumDice.delete(0, ctk.END)
        self.num_dice.set(value="1")
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
    t.geometry("1422x603")
    t.iconbitmap("dice-icon.ico")
    t.title("DND Application")
    f.pack(fill=ctk.BOTH, expand=True)

    t.mainloop()
