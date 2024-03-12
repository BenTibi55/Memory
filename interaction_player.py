import random
import builtins
from memory_basic import *


def ask_size():
    # demander à l'utilisateur les dimensions de sa grille
    print("Choisir des dimensions dont le produit donne un nombre pair")
    hauteur = int(input("Donner la hauteur de la grille entre 2 et 10 : "))
    longueur = int(input("Donner la longueur de la grille entre 2 et 10 : "))
    dimension = [i for i in range(2, 11)]
    while hauteur not in dimension or longueur not in dimension or hauteur*longueur % 2 == 1:
        print("Erreur - Choisir des dimensions dont le produit donne un nombre pair")
        hauteur = int(input("Donner la hauteur de la grille entre 2 et 10 : "))
        longueur = int(
            input("Donner la longueur de la grille entre 2 et 10 : "))
    return (hauteur, longueur)


def positions_possibles(grid):
    # donne une liste de coordonnées possibles à choisir pour les joueurs
    positions_possibles = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # positions possibles en mode "python", commence à 0
            if is_case_filled(grid, (i, j)):
                positions_possibles.append((i, j))
    return positions_possibles


def choose_case(grid):
    # renvoie la position dans la liste de liste des cases d'une carte à retourner choisie par le joueur
    # positions en mode "joueur" (commence à 1) ; renvoie des positions en mode  (commence à 0)
    x = input("Entrez la ligne de la case à retourner  : ")
    y = input("Entrez la colonne de la case à retourner  : ")
    while (int(x)-1, int(y)-1) not in positions_possibles(grid):
        x = input(
            'Erreur - entrez la ligne de la case à retourner  : ')
        y = input("Erreur - entrez la colonne de la case à retourner  : ")
    return (int(x)-1, int(y)-1)
