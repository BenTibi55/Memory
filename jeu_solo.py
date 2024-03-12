from random import shuffle
from tkinter import *
from PIL import Image
import time
from themes import *
from math import *
import playsound


def jeu_solo(NB_LINES, NB_COLS, THEME):

    start = time.time()
    playsound.playsound("musique/musiquejeu.mp3", block=False)

    # grandeur caractéristique du jeu
    TAILLE_IMG = 100
    ESAPCE = 0
    SIDE = TAILLE_IMG+ESAPCE

    LARG_MAIN = SIDE*NB_COLS
    HAUT_MAIN = SIDE*NB_LINES
    X0 = Y0 = SIDE//2
    THEME = THEME
    NB_PAIRES = NB_COLS*NB_LINES/2
    # Pour voir si on a gagné

    def test(B):
        T = [[-1 for k in range(NB_COLS)] for i in range(NB_LINES)]
        return T == B

    # cases à trouver
    IMG = random_theme(THEME, NB_PAIRES)

    # genere un tableau aléatoire avec des chiffres appareillés

    def board(nb_cols, nb_lines):
        G = []
        n = nb_lines*nb_cols//2  # donne le chiffre maximale des paires
        L = []
        for k in range(1, n+1):
            L.append(k)
            L.append(k)
        shuffle(L)

        k = 0
        for i in range(nb_lines):
            M = []
            for j in range(nb_cols):
                M.append(L[k])
                k += 1
            G.append(M)
        return (G)

    # fonction play

    # crée une fonction qui prend la valeur maximale d'une liste:

    def max(L):
        m = L[0][0]
        for k in range(len(L)):
            for j in range(len(L[k])):
                if L[k][j] > m:
                    m = L[k][j]
        return m

    def play():
        move = [None, None]
        # fonction qui permet de récupérer les coordonées de la case sur laquelle je clique et qui en révèle la case cachée puis la recouvre au bout de 1 sec

        def clic(event):
            if move[0] == None:
                x = event.x
                y = event.y
                ligne = y//SIDE + 1
                colonne = x//SIDE + 1

                centre = (X0+(colonne-1)*SIDE, Y0+(ligne-1)*SIDE)
                cnv.after(
                    0, lambda x=ids_cover[ligne-1][colonne-1]: cnv.delete(x))

                # on enregistre ces informations
                move[0] = [centre, ligne-1, colonne-1]

            else:
                if move[1] == None and move[0] != None:
                    x = event.x
                    y = event.y
                    ligne = y//SIDE + 1
                    colonne = x//SIDE + 1
                    if (ligne, colonne) != (move[0][1]+1, move[0][2]+1):
                        # on regarde à quel chiffre mélangé les images révelées correspondent
                        a = B[move[0][1]][move[0][2]]
                        b = B[ligne-1][colonne-1]
                        m = max(ids_cover)
                        centre = (X0+(colonne-1)*SIDE, Y0+(ligne-1)*SIDE)
                        cnv.after(
                            0, lambda x=ids_cover[ligne-1][colonne-1]: cnv.delete(x))
                        if a != b:
                            cnv.after(
                                1000, lambda x=ids_cover[ligne-1][colonne-1]: cnv.create_image(centre, image=face_retournee))
                            ids_cover[ligne-1][colonne-1] = m+1
                            cnv.after(1000, lambda x=ids_cover[ligne-1][colonne-1]: cnv.create_image(
                                move[0][0], image=face_retournee))
                            ids_cover[move[0][1]][move[0][2]] = m+2
                            playsound.playsound(
                                "musique/swing.mp3", block=False)
                        if a == b:
                            B[move[0][1]][move[0][2]], B[ligne-1][colonne-1] = - \
                                1, -1  # on marque le fait qu'on a trouvé la paire
                            playsound.playsound(
                                "musique/paire.mp3", block=False)

                            if test(B) == True:
                                print("vous avez gagné")
                                playsound.playsound(
                                    "musique/win.mp3", block=False)
                                end = time.time()
                                print("vous avez mis ", end-start, " secondes")
                                score = floor(end-start)
                                score = str(score)
                                cnv2.after(
                                    0, lambda x=id_attente: cnv2.delete(x))
                                cnv2.after(0, lambda x=ids_cover[ligne-1][colonne-1]: cnv2.create_text(LARG_MAIN/2, 50, width=LARG_MAIN,
                                                                                                       font="Arial 20", text="Votre temps est :"+score+" sec", fill="red"))

                        move[1] = 6

                else:  # il faut faire un clic pour reinitialiser move et pouvoir à nouveau révéler 2 cartes
                    if move[0] != None and move[1] != None:
                        move[1] = None
                        move[0] = None

        # lancement de la fenêtre de jeu
        main = Tk()
        cnv = Canvas(main, width=LARG_MAIN, height=HAUT_MAIN, bg='red')
        cnv.pack()
        cnv2 = Canvas(main, width=LARG_MAIN, height=100, bg='blue')
        cnv2.pack()
        id_attente = cnv2.create_text(LARG_MAIN/2, 50, width=LARG_MAIN,
                                      font="Arial 20", text="Trouvez les paires !")
        ids_cover = [[0 for i in range(NB_COLS)] for j in range(NB_LINES)]
        face_retournee = PhotoImage(file="FaceRetournee.png")
        logos = [PhotoImage(file=s) for s in IMG]
        B = board(NB_LINES, NB_COLS)

        for i in range(NB_LINES):
            for j in range(NB_COLS):
                center = (X0+j*SIDE, Y0+i*SIDE)
                num_image = B[i][j]
                image_cache = logos[num_image-1]
                cnv.create_image(center, image=image_cache)
                id_cover = cnv.create_image(center, image=face_retournee)
                # en i,j on a l'identifiant de la face cachée (cover)
                ids_cover[i][j] = id_cover
                cnv.bind("<Button-1>", clic)

        main.mainloop()

    play()
