from random import shuffle
from tkinter import *
from PIL import Image
import time
from themes import *
from math import *
import playsound


def jeu_a_deux(NB_LINES, NB_COLS, THEME):

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
    # Pour voir si le jeux est fini

    def test(B):
        T = [[-1 for k in range(NB_COLS)] for i in range(NB_LINES)]
        return T == B
    # Pour determiner qui a gagné :

    def vainqueur(L1, L2):
        if L1[0] > L2[0]:
            return 1
        else:
            return 2

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
    # fonction qui renvoie le dernier terme d'une liste (pour id_score et id_joueurs)
    def last(L):
        return L[len(L)-1]

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
                            if joueur[0] % 2 == 0:
                                score_joueur_1[0] = score_joueur_1[0]+1
                            if joueur[0] % 2 != 0:
                                score_joueur_2[0] = score_joueur_2[0]+1

                            if test(B) == True:
                                playsound.playsound(
                                    "musique/win.mp3", block=False)
                                cnv3.after(0, lambda x=last(
                                    id_score): cnv3.delete(x))
                                cnv3.after(0, lambda x=8: cnv3.create_text(
                                    LARG_MAIN/2, 50, text="score : "+str(score_joueur_1[0])+";"+str(score_joueur_2[0]), font="Arial 15"))
                                id_score.append(last(id_score)+1)
                                levainqueur = vainqueur(
                                    score_joueur_1, score_joueur_2)
                                cnv2.after(0, lambda x=8: cnv2.create_text(
                                    LARG_MAIN/2, 50, text="le joueur "+str(levainqueur)+" a gagné", font="Arial 15", fill="red"))
                                cnv2.after(0, lambda x=last(
                                    id_joueur): cnv2.delete(x))
                                return 1

                        joueur[0] = joueur[0]+1

                        move[1] = 6
                        if joueur[0] % 2 == 0:

                            cnv2.after(0, lambda x=last(
                                id_joueur): cnv2.delete(x))
                            id_1 = cnv2.after(0, lambda x=8: cnv2.create_text(
                                LARG_MAIN/2, 50, text="tour du joueur 1", font="Arial 15", fill="red"))
                            id_joueur.append(last(id_joueur)+1)
                        else:

                            cnv2.after(0, lambda x=last(
                                id_joueur): cnv2.delete(x))
                            id_1 = cnv2.after(0, lambda x=8: cnv2.create_text(
                                LARG_MAIN/2, 50, text="tour du joueur 2", font="Arial 15", fill="orange"))
                            id_joueur.append(last(id_joueur)+1)

                else:  # il faut faire un clic pour reinitialiser move et pouvoir à nouveau révéler 2 cartes
                    if move[0] != None and move[1] != None:
                        move[1] = None
                        move[0] = None
                        cnv3.after(0, lambda x=last(
                            id_score): cnv3.delete(x))
                        cnv3.after(0, lambda x=8: cnv3.create_text(
                            LARG_MAIN/2, 50, text="score : "+str(score_joueur_1[0])+";"+str(score_joueur_2[0]), font="Arial 15"))
                        id_score.append(last(id_score)+1)

        # lancement de la fenêtre de jeu
        main = Tk()
        cnv = Canvas(main, width=LARG_MAIN, height=HAUT_MAIN, bg='red')
        cnv.pack()
        cnv2 = Canvas(main, width=LARG_MAIN, height=100, bg='blue')
        cnv2.pack()
        cnv3 = Canvas(main, width=LARG_MAIN, height=100, bg='red')
        cnv3.pack()
        ids_cover = [[0 for i in range(NB_COLS)] for j in range(NB_LINES)]
        face_retournee = PhotoImage(file="FaceRetournee.png")
        logos = [PhotoImage(file=s) for s in IMG]
        B = board(NB_LINES, NB_COLS)
        joueur = [0]
        score_joueur_1 = [0]
        score_joueur_2 = [0]
        id_score = []  # prend les identifiants des textes de scores
        id_joueur = []  # prend les identifiants des textes ou on indique quel joueur doit jouer

        id_joueur1 = cnv2.create_text(
            LARG_MAIN/2, 50, text="tour du joueur 1", font="Arial 15", fill="red")
        id_joueur.append(id_joueur1)
        id_score1 = cnv3.create_text(
            LARG_MAIN/2, 50, text="score : "+str(score_joueur_1[0])+";" + str(score_joueur_2[0]), font="Arial 15", fill="black")
        id_score.append(id_score1)
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
