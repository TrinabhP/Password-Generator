import tkinter as tk
import ttkbootstrap as ttk
import random
import string


def generate(symbols=True, uppercase=True, digits=True):
	password = []
	characters = []
	characters.append(string.ascii_lowercase)

	if (uppercase):
		characters.append(string.ascii_uppercase)
	if digits:
		characters.append(string.digits)
	if symbols:
		characters.append(string.punctuation)

	for i in range(entry_int.get()):
		characters = "".join(characters)
		password.append(characters[random.randint(0, len(characters) - 1)])

	output_string.set("".join(password))

# window
window = ttk.Window(themename = 'darkly')
window.title("Password-Generator")
window.geometry('300x150')

# title
title_label = ttk.Label(master = window, text = 'Password Generator', font= ('Segoe UI', 24, 'bold'), style='info.TLabel')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Generate', command = generate, style='info.TButton')
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
	master = window, 
	text = "Password", 
	font = ('Segoe UI', 24), 
	textvariable = output_string)
output_label.pack(pady = 5)

window.mainloop()
