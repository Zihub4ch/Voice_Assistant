import tkinter as tk
from random import randint, choice
from tkinter import messagebox

window = tk.Tk()

window.resizable(width = False, height = False)

window.title("Голосовой помощник")

window.geometry("1024x720")

window["bg"] = "black"

activate = tk.Label(window, text = "Включить голосового помощника", font = ("Arial Bold", 15), fg = "orange", bg = "black")
activate.place(x = 360, y = 30)

Entertext = tk.Entry(fg = "black", width = 50)
Entertext.place(x = 360, y = 480)

window.mainloop()