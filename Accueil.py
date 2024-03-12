from tkinter import *
from interface_selection import *


def new():
    root.destroy()
    open_select_window()


root = Tk()
root.title("Accueil Memory")
image1 = PhotoImage(file="Memorics.png")
cnv3 = Canvas(root, height=500, width=500, bg="red")
cnv3.pack(side=TOP)
cnv3.create_image((250, 250), image=image1)
button = Button(root, text="play", bg="grey",
                activeforeground="yellow", activebackground="red", command=new, font="Arial 30")
button.pack(side=BOTTOM, fill=X)

root.mainloop()
