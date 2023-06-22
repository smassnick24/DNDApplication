from DNDCharacterFrame import DNDCharacterFrame
from CharacterDataHandler import DataHandler
from DiceRollerFrame import DiceRollFrame
import tkinter as tk
import customtkinter as ctk


class DNDApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.CharFrame = DNDCharacterFrame(master=self)
        self.DiceRoller = DiceRollFrame(master=self)

        self.geometry("1422x603")

    def CharFramePack(self):
        print("Control + 1")
        # self.DiceRoller.pack_forget()
        # self.CharFrame.pack(fill=ctk.BOTH, expand=True, sticky=ctk.NW)

    def DiceRollerPack(self):
        print("Control + 2")
        # self.CharFrame.pack_forget()
        # self.DiceRoller.pack(fill=ctk.BOTH, expand=True, sticky=ctk.NW)


if __name__ == '__main__':
    t = DNDApp()
    t.bind("<Control-q>", lambda: t.CharFramePack())
    t.bind("<Control-w>", lambda: t.DiceRollerPack())
    t.mainloop()


