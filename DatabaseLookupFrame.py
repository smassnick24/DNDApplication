import tkinter as tk
import customtkinter as ctk
import DatabaseLookup as dbl


class DatabaseLookupFrame(ctk.CTkScrollableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_mode = []

        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.special_font = ctk.CTkFont(family="Rockwell", size=18)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)

        # text box for text dump
        self.text_dump = ctk.CTkTextbox(self, font=self.font)

        # query
        self.query_var = ctk.StringVar(value="fireball")
        self.query_entry = ctk.CTkEntry(self, font=self.font)

        # mode buttons
        self.spell_mode = ctk.CTkButton(self, text="Spell")
        self.class_mode = ctk.CTkButton(self, text="Class")
        self.subclass_mode = ctk.CTkButton(self, text="Subclass")
        self.monster_mode = ctk.CTkButton(self, text="Monster")

        # packing widgets
        self.query_entry.grid(row=0, column=0)
        self.spell_mode.grid(row=1, column=0)
        self.class_mode.grid(row=1, column=1)
        self.subclass_mode.grid(row=1, column=2)
        self.monster_mode.grid(row=1, column=2)
        self.text_dump.grid(row=2, column=0, columnspan=10)

    def change_mode(self, next_mode):
        pass

