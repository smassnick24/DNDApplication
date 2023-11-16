import tkinter as tk
import customtkinter as ctk
import DatabaseLookup as dbl


class DatabaseLookupFrame(ctk.CTkScrollableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.font = ctk.CTkFont(family="Rockwell", size=14)
        self.special_font = ctk.CTkFont(family="Rockwell", size=18)
        self.header_font = ctk.CTkFont(family="Rockwell", size=28)

        # text box for text dump
        self.text_dump = ctk.CTkTextbox(self, font=self.font)

        # query
        self.query_var = ctk.StringVar(value="fireball")
        self.query_entry = ctk.CTkEntry(self, font=self.font)

        # packing widgets
        self.query_entry.grid()
        self.text_dump.grid()
