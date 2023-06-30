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

    def CharFramePack(self, event):
        print("Event Triggered")
        self.DiceRoller.pack_forget()
        self.CharFrame.pack(fill=ctk.BOTH, expand=True)
        self.geometry("1080x720")

    def DiceRollerPack(self, event):
        print("Event Triggered")
        self.CharFrame.pack_forget()
        self.DiceRoller.pack(fill=ctk.BOTH, expand=True)
        self.geometry("1422x603")


if __name__ == '__main__':
    t = DNDApp()
    t.bind("<Control-q>", t.CharFramePack)
    t.bind("<Control-w>", t.DiceRollerPack)
    t.mainloop()


