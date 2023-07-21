import tkinter as tk
from tkinter import PhotoImage
def btn_click():
    new_window = tk.Tk()
    new_window.title("New window")
    new_window.iconbitmap("pop_ice_spring_dessert_sweet_popsicle_icon_255192.ico")
    new_window.geometry("800x600")
    l = tk.Label(new_window,
             text="hello world",
             font="times 20",
             fg="yellow",
             bg="black")
    l.pack(side="top")

window =tk.Tk()
window.title("yoyo window")
window.iconbitmap("pop_ice_spring_dessert_sweet_popsicle_icon_255192.ico")
window.geometry("600x800")
#window.resizable(False,False)
window.minsize(200,100)
window.maxsize(900,700)

btn =tk.Button(
    window,
    text="click me",
    width=10,
    height=5,
    bg="cyan",
    fg="navy",
    command=btn_click)



e = tk.Entry(window,
             width=20)

btn.pack()
#l.pack()
e.pack()

window.mainloop()