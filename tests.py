import tkinter as tk
import customtkinter as ctk

test = ctk.CTk()

wid_var = ctk.StringVar(value="")
wid = ctk.CTkEntry(test, textvariable=wid_var)

wid.pack()


def on_entry_change(event):
    print(f"Entry Modified: {wid_var.get()}")


wid.bind("<KeyRelease>", on_entry_change)

test.mainloop()
