from DNDCharacterFrame import DNDCharacterFrame
from CharacterDataHandler import DataHandler
from DiceRollerFrame import DiceRollFrame
import tkinter as tk
import customtkinter as ctk


class DNDApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.header_font = ctk.CTkFont(family="Rockwell", size=28)
        #self.attributes('-fullscreen', True)
        self.geometry("500x500")

        self.welcome_frame = ctk.CTkFrame(master=self)
        self.CharFrame = DNDCharacterFrame(master=self)
        self.DiceRoller = DiceRollFrame(master=self)

        self.welcome = ctk.CTkLabel(master=self.welcome_frame, text="DND AIO", font=self.header_font)

        self.welcome.pack()

        self.welcome_frame.pack(fill=ctk.BOTH, expand=True)

    def CharFramePack(self, event):
        print("Event Triggered")
        self.welcome_frame.pack_forget()
        self.DiceRoller.pack_forget()
        self.CharFrame.pack(fill=ctk.BOTH, expand=True)
        self.geometry("1350x820")

    def DiceRollerPack(self, event):
        print("Event Triggered")
        self.welcome_frame.pack_forget()
        self.CharFrame.pack_forget()
        self.DiceRoller.pack(fill=ctk.BOTH, expand=True)
        self.geometry("1422x603")

    def quit_pressed(self, event):
        self.quit()


if __name__ == '__main__':
    t = DNDApp()
    t.bind("<Control-q>", t.CharFramePack)
    t.bind("<Control-w>", t.DiceRollerPack)
    t.bind("<Control-s>", t.CharFrame.save)
    t.bind("<Control-KeyPress-1>", t.quit_pressed)
    t.CharFrame.STREntry.bind("<KeyRelease>", t.CharFrame.save)
    t.CharFrame.DEXEntry.bind("<KeyRelease>", t.CharFrame.save)
    t.CharFrame.CONEntry.bind("<KeyRelease>", t.CharFrame.save)
    t.CharFrame.INTEntry.bind("<KeyRelease>", t.CharFrame.save)
    t.CharFrame.WISEntry.bind("<KeyRelease>", t.CharFrame.save)
    t.CharFrame.CHAEntry.bind("<KeyRelease>", t.CharFrame.save)
    t.mainloop()
