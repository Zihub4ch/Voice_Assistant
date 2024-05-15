import tkinter as tk
from random import randint, choice
from tkinter import messagebox

window = tk.Tk()

window.resizable(width = False, height = False)

window.title("Голосовой помощник")

window.geometry("1024x720")

window["bg"] = "black"

activate = tk.Label(window, text = "Включить голосового помощника", font = ("Arial Bold", 15), fg = "orange", bg = "black")
activate.place(x = 385, y = 30)

btn = tk.Button(window, text = "Включить", width = "50", height = "2", fg = "black", bg = "white")
btn.place(x = 360, y = 80)

hot_buttons = tk.Label(window, text = "Ввести горячую клавишу", font = ("Arial Bold", 15), fg = "orange", bg = "black")
hot_buttons.place(x = 420, y = 200)

Entertext = tk.Entry(fg = "black", width = 50)
Entertext.place(x = 385, y = 240)

btn = tk.Button(window, text = "Добавить", width = "50", height = "2", fg = "black", bg = "white")
btn.place(x = 360, y = 280)

list = tk.Label(window, text = "Список горячих клавиш", font = ("Arial Bold", 15), fg = "orange", bg = "black")
list.place(x = 432, y = 360)

btn = tk.Button(window, text = "Открыть", width = "50", height = "2", fg = "black", bg = "white")
btn.place(x = 360, y = 390)

window.mainloop()