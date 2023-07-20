import tkinter as tk
from tkinter import PhotoImage


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
    fg="navy")
btn.pack()



  


window.mainloop()