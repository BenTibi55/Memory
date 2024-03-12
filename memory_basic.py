import random
import copy
import playsound


def create_grid(hauteur, longueur):
    # Prend en argument deux entier et renvoie un tableau (une liste de listes)
    # Elle est de la hauteur du premier entier et de la longueur du deuxième entier
    # La grille est ensuite remplie par les différentes paires (des entiers entre 1 hauteur*longueur/2)
    game_grid = []
    nbr_paires = (int(hauteur)*int(longueur))//2
    list_nbrs = []
    for i in range(0, int(hauteur)):
        game_grid.append([0]*int(longueur))
    for i in range(1, nbr_paires+1):
        list_nbrs.append(i)
        list_nbrs.append(i)
    for i in range(0, len(list_nbrs)):
        k = 0
        while k == 0:
            m = (random.randint(0, hauteur-1))
            n = (random.randint(0, longueur-1))
            if game_grid[m][n] == 0:
                game_grid[m][n] = list_nbrs[i]
                k = 1
    L = []
    for i in range(len(game_grid)):
        M = []
        for j in range(len(game_grid[0])):
            M.append(str(game_grid[i][j]))
        L.append(M)
    return (L)


def is_a_pair(grid, pos1, pos2):
    # renvoie le booléen qui décrit si les deux cases de la grille en arguments forment une paire ou non
    (x1, y1) = pos1
    (x2, y2) = pos2
    if grid[x1][y1] == grid[x2][y2]:
        playsound.playsound("musique/paire.mp3", block=False)
        return True
    return False


def remove_pair(grid, pos1, pos2):
    # retire une paire de la grille lorsqu'elle a été trouvée
    (x1, y1) = pos1
    (x2, y2) = pos2
    grille = copy.deepcopy(grid)
    if is_a_pair(grid, pos1, pos2):
        grille[x1][y1] = ' '
        grille[x2][y2] = ' '
    return grille


def is_case_filled(grid, pos):
    # Retourne True si la case est non vide ie si la paire correspondante à la case à la position pos n'a pas été trouvée
    x, y = pos
    if grid[x][y] == ' ':
        return (False)
    else:
        return (True)


def is_game_over(grid):
    # Retourne True lorque la partie est terminée ie lorsque toutes les tuiles ont été retournées
    L = len(grid)
    l = len(grid[0])
    for i in range(0, L):
        for j in range(0, l):
            if grid[i][j] != ' ':
                return (False)
    return (True)


def compare_scores(score1, score2):
    # Compare le score de 2 joueurs et retourne le nom du gagnant s'il existe
    if score1 > score2:
        print("Le joueur 1 a gagné avec un score de ", score1,
              " contre un score de : ", score2, " pour le joueur 2 !")
        playsound.playsound("musique/win.mp3", block=False)
    elif score1 < score2:
        print("Le joueur 2 a gagné avec un score de ", score2,
              " contre un score de : ", score1, " pour le joueur 1 !")
        playsound.playsound("musique/win.mp3", block=False)
    else:
        print("Egalité !")


def compare_scores_ordi(score1, score2):
    # Compare le score du joueur (score1) et de l'ordinateur (score2) et retourne le nom du gagnant s'il existe
    if score1 > score2:
        print("Le joueur 1 a gagné avec un score de ", score1,
              " contre un score de : ", score2, " pour l'ordinateur' !")
    elif score1 < score2:
        playsound.playsound("musique/LoseSoundEffect.mp3", block=False)
        print("L'ordinateur a gagné avec un score de ", score2,
              " contre un score de ", score1, " pour le joueur 1 !")
    else:
        print("Egalité")
