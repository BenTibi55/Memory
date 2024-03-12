from tkinter import *
from game_play import *


def open_select_window():
    w = Tk()
    w.title("MemoriCS")
    n = IntVar(w)
    n.set(2)
    m = IntVar(w)
    m.set(2)
    mode_jeu = StringVar(w)
    mode_jeu.set("jeu solo")
    theme = StringVar(w)
    theme.set("animaux")
    label1 = Label(w, text="nombre de lignes")
    label2 = Label(w, text='Choix du mode de jeu')
    label3 = Label(w, text='Thème')
    spinbox1 = Spinbox(w, textvariable=n, from_=2, to=10, increment=2)
    spinbox2 = Spinbox(
        w, values=['jeu solo', 'jeu 1v1'])
    spinbox3 = Spinbox(w, values=['Animaux', 'Drapeaux', 'Pokémons'])

    def appel_jeu():
        N = int(spinbox1.get())
        M = int(spinbox1.get())
        Mode = spinbox2.get()
        Theme = spinbox3.get()
        w.destroy()
        (game(N, M, Mode, Theme))

    button1 = Button(w, text='PLAY', command=appel_jeu)
    button2 = Button(w,
                     text="QUIT",
                     command=quit)
    label1.grid(row=0, column=0)
    spinbox1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    spinbox2.grid(row=3, column=0)
    label3.grid(row=4, column=0)
    spinbox3.grid(row=5, column=0)
    button1.grid(row=8, column=0)
    button2.grid(row=9, column=0)
    w.mainloop()
