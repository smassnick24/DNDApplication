import tkinter as tk

root = tk.Tk()

# Create a Canvas widget
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Vertical Scrollbar widget
scrollbar_y = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar_y.set)

# Create a Horizontal Scrollbar widget
scrollbar_x = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
canvas.configure(xscrollcommand=scrollbar_x.set)

# Create a Frame to hold the content
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Add content to the Frame
for i in range(50):
    tk.Label(frame, text=f"Label {i}").pack()

# Configure the Canvas to resize with the window
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()