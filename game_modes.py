from affiche_grid import *
from interaction_player import *
from memory_basic import *
import random
import playsound
import time


def jeu_joueur_1(grid, score):
    score1 = score
    print("Au tour du joueur 1")
    x, y = choose_case(grid)
    print(affiche_1case(grid, (x, y)))
    u, v = choose_case(grid)
    while u == x and v == y:  # vérification que la 2ème position n'est pas la même que la 1ère
        print("Veuillez choisir une autre case ")
        u, v = choose_case(grid)
    print(affiche_2case(grid, (x, y), (u, v)))
    if is_a_pair(grid, (x, y), (u, v)):
        playsound.playsound("musique/paire.mp3")
        grid = remove_pair(grid, (x, y), (u, v))
        score1 += 1
        print("Le joueur 1 a trouvé une paire")
        return (score1, grid)
    else:
        print("Ce n'est pas une paire ")
        return (score1, grid)


def jeu_joueur_2(grid, score):
    score2 = score
    print("Au tour du joueur 2")
    x, y = choose_case(grid)
    print(affiche_1case(grid, (x, y)))
    u, v = choose_case(grid)
    while u == x and v == y:  # vérification que la 2ème position n'est pas la même que la 1ère
        print("Veuillez choisir une autre case ")
        u, v = choose_case(grid)
    print(affiche_2case(grid, (x, y), (u, v)))
    if is_a_pair(grid, (x, y), (u, v)):
        playsound.playsound("musique/paire.mp3")
        grid = remove_pair(grid, (x, y), (u, v))
        score2 += 1
        print("Le joueur 2 a trouvé une paire")
        return (score2, grid)
    else:
        print("Ce n'est pas une paire ")
        return (score2, grid)


def game_1v1():
    # Jeu en 1 contre 1, les joueurs rejouent lorsqu'ils ont trouvé une paire
    n, m = ask_size()
    grid = create_grid(n, m)
    print(affiche_grid_cache(grid))
    # Affichage de la grille initiale, tuiles retournées
    score1 = 0
    score2 = 0
    while not is_game_over(grid):
        score, grid = jeu_joueur_1(grid, score1)
        print(affiche_grid_cache(grid))
        # lorsque le joueur 1 a obtenu une paire, il rejoue
        while not is_game_over(grid) and score != score1:
            score1 = score
            score, grid = jeu_joueur_1(grid, score1)
            print(affiche_grid_cache(grid))
        if not is_game_over(grid):
            score, grid = jeu_joueur_2(grid, score2)
            print(affiche_grid_cache(grid))
            # lorsque le joueur 1 a obtenu une paire, il rejoue
            while not is_game_over(grid) and score != score2:
                score2 = score
                score, grid = jeu_joueur_2(grid, score2)
                print(affiche_grid_cache(grid))
    # Affichage du possible gagnant et le score des 2 joueurs
    print(compare_scores(score1, score2))


def game_solo():
    # Jeu en solo
    n, m = ask_size()
    grid = create_grid(n, m)
    print(affiche_grid_cache(grid))
    score = 0
    while not is_game_over(grid):
        x, y = choose_case(grid)
        print(affiche_1case(grid, (x, y)))
        u, v = choose_case(grid)
        while u == x and v == y:  # vérification que la 2ème position n'est pas la même que la 1ère
            print("Veuillez choisir une autre carte ")
            u, v = choose_case(grid)
        print(affiche_2case(grid, (x, y), (u, v)))
        if is_a_pair(grid, (x, y), (u, v)):
            playsound.playsound("musique/paire.mp3")
            grid = remove_pair(grid, (x, y), (u, v))
            score += 1
            print("Vous avez trouvé une paire ")
        else:
            print("Ce n'est pas une paire ")
        print(affiche_grid_cache(grid))
    playsound.playsound("musique/win.mp3")
    print("Félicitations, vous avez gagné en "+str(score)+" coups!")


def choix_debut_ordi(grid, memoire):
    # recherche si une paire n'aurait pas déjà été révélée au cours du jeu
    # l'ordinateur vérifie dans sa mémoire si une valeur apparaît deux fois : si oui il sélectionne d'office ces deux cases là.
    # si il y a deux paires, la boucle est faite de telle façon que seule la première trouvée aura ses indices retournés par la fonction.
    pos1 = (-1, -1)            # initialisation de pos1
    pos2 = (-1, -1)            # initialisation de pos2
    # création d'une liste vide qui sera utilisée pour déterminer si une valeur apparaît deux fois dans la grille.
    listing = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if memoire[i][j] != " ":
                # remplissage de la liste avec les cases déjà apparues au cours du jeu.
                listing.append(memoire[i][j])
    for k in range(0, len(listing)):
        # compteur donne le nombre de fois que la valeur apparaît dans la liste
        compteur = listing.count(listing[k])
        # si une valeur apparaît deux fois (présence d'une paire dans la mémoire).
        if compteur == 2:
            # on parcours la grille pour retrouver la position des deux cases
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if memoire[i][j] == listing[k] and compteur == 2:
                        # on stocke les coordonnées de la première case
                        pos1 = (i, j)
                        # afin de ne pas repasser dans le if mais bien aller dans le elif ensuite
                        compteur = compteur-1
                    elif memoire[i][j] == listing[k] and compteur == 1:
                        # on stocke les coordonnées de la deuxième case
                        pos2 = (i, j)
                        # retourne directe pour éviter les conflits avec une éventuelle deuxièeme paire
                        return (pos1, pos2)
    # si aucune paire n'est trouvée, on renvoie (-1,-1) pour pos1 et pos2
    return (pos1, pos2)


def choix_intermediaire_ordi(grid, memoire, pos1):
    # après avoir retourné une première case, l'ordinateur vérifie dans la mémoire si la deuxième case correspondante n'aurait pas déjà été révélée
    # si oui c'est celle-ci qu'il choisira de retourner en deuxième case
    pos2 = (-1, -1)            # initialisation de pos2
    # création d'une liste vide qui sera utilisée pour déterminer si une valeur apparaît deux fois dans la grille.
    listing = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if memoire[i][j] != " ":
                # remplissage de la liste avec les cases déjà apparues au cours du jeu.
                listing.append(memoire[i][j])
    for k in listing:
        # on compte si la valeur trouvée dans la première case apparaît deux fois
        compteur = listing.count(grid[pos1[0]][pos1[1]])
        # si une valeur apparaît deux fois (présence d'une paire dans la mémoire).
        if compteur == 2:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if memoire[i][j] == grid[pos1[0]][pos1[1]] and pos1 != (i, j):
                        # on stocke les coordonnées de la deuxième case
                        pos2 = (i, j)
                        # on peut renvoyer pos1 (inchangé) et pos2 directement
                        return (pos1, pos2)
    # si aucune valeur correspondante n'est trouvée dans la liste on renvoie pos1 inchangé et pos2=(-1,-1)
    return (pos1, pos2)


def tour_joueur_vs_ordi(grid, memoire, score_joueur):
    print(affiche_grid_cache(grid))
    (x, y) = choose_case(grid)
    print(affiche_1case(grid, (x, y)))
    (z, w) = choose_case(grid)
    print(affiche_2case(grid, (x, y), (z, w)))
    if is_a_pair(grid, (x, y), (z, w)):
        score_joueur = score_joueur + 10
        grid = remove_pair(grid, (x, y), (z, w))
        # mise à jour mémoire ordinateur (effacement de la valeur de la paire trouvée)
        memoire[x][y] = " "
        # mise à jour mémoire ordinateur (effacement de la valeur de la paire trouvée)
        memoire[z][w] = " "
        if not is_game_over(grid):
            print("C'est une paire ! Rejouez")
            # itération pour faire rejouer si une paire a été trouvée
            return (tour_joueur_vs_ordi(grid, memoire, score_joueur))
        else:
            # cas où le jeu serait fini (dernière paire trouvée) pour ne pas faire rejouer le joueur (erreur sinon)
            print("C'est une paire !")
    else:
        # mise à jour mémoire de l'ordinateur (ajout de la valeur de la case associée)
        memoire[x][y] = grid[x][y]
        # mise à jour mémoire de l'ordinateur (ajout de la valeur de la case associée)
        memoire[z][w] = grid[z][w]
    return (grid, memoire, score_joueur)


def tour_ordi(grid, memoire, score_ordi):
    hauteur = len(grid)
    longueur = len(grid[0])
    print(affiche_grid_cache(grid))
    time.sleep(3)
    # premier choix ordi (recherche d'une paire déjà révélée)
    pos1, pos2 = choix_debut_ordi(grid, memoire)
    # ie pos1==pos2==(-1,-1) (si pas de paire trouvée en mémoire), on choisit aléatoirement la case 1 à retourner
    if pos1 == pos2:
        pos1 = random.randint(
            0, int(hauteur-1)), random.randint(0, int(longueur-1))
        while pos1 not in positions_possibles(grid):
            pos1 = (random.randint(0, int(hauteur-1)),
                    random.randint(0, int(longueur-1)))
        print(affiche_1case(grid, pos1))
        time.sleep(3)
        # ajout de la case retournée à la mémoire
        memoire[pos1[0]][pos1[1]] = grid[pos1[0]][pos1[1]]
        # recherche de la case correspondante dans la mémoire
        pos1, pos2 = choix_intermediaire_ordi(grid, memoire, pos1)
        # si cette case est inconnue, on choisi au hasard la deuxième case
        if pos2 == (-1, -1):
            while pos2 not in positions_possibles(grid) or pos1 == pos2:
                pos2 = (random.randint(0, int(hauteur-1)),
                        random.randint(0, int(longueur-1)))
        print(affiche_2case(grid, pos1, pos2))
        time.sleep(3)
    else:                                          # cas où une paire avait été trouvée en mémoire à la ligne 73
        print(affiche_1case(grid, pos1))
        time.sleep(3)
        print(affiche_2case(grid, pos1, pos2))
        time.sleep(3)
    if is_a_pair(grid, pos1, pos2):
        playsound.playsound("musique/paire.mp3")
        score_ordi = score_ordi + 10
        grid = remove_pair(grid, pos1, pos2)
        # mise à jour mémoire ordinateur (effacement de la valeur de la paire trouvée)
        memoire[pos1[0]][pos1[1]] = " "
        # mise à jour mémoire ordinateur (effacement de la valeur de la paire trouvée)
        memoire[pos2[0]][pos2[1]] = " "
        if not is_game_over(grid):
            print("C'est une paire ! L'ordinateur rejoue !")
            # itération pour faire rejouer si une paire a été trouvée
            return (tour_ordi(grid, memoire, score_ordi))
        else:
            print("C'est une paire !")
    else:
        # mise à jour mémoire de l'ordinateur (ajout de la valeur de la case associée)
        memoire[pos1[0]][pos1[1]] = grid[pos1[0]][pos1[1]]
        # mise à jour mémoire de l'ordinateur (ajout de la valeur de la case associée)
        memoire[pos2[0]][pos2[1]] = grid[pos2[0]][pos2[1]]
    return (grid, memoire, score_ordi)


def game_play_ordi():
    (hauteur, longueur) = ask_size()
    grid = create_grid(hauteur, longueur)
    score_ordi = 0
    score_joueur = 0
    memoire = []
    for i in range(0, int(hauteur)):
        memoire.append([" "]*int(longueur))
    while is_game_over(grid) == False:
        print("Tour du joueur")
        grid, memoire, score_joueur = tour_joueur_vs_ordi(
            grid, memoire, score_joueur)
        if is_game_over(grid):
            break
        time.sleep(3)
        print("Tour de l'ordinateur")
        grid, memoire, score_ordi = tour_ordi(grid, memoire, score_ordi)
        time.sleep(3)
    compare_scores_ordi(score_joueur, score_ordi)


def choose_mode():
    mode = int(input(
        "Choisir un mode de jeu : 1 (game 1v1) - 2 (game 1 joueur) ; 3 (game contre ordi)"))
    while mode not in [1, 2, 3]:
        mode = int(input(
            "Choisir un mode de jeu : 1 (game 1v1) - 2 (game 1 joueur) ; 3 (game contre ordi)"))
    if mode == 1:
        game_1v1()
    if mode == 2:
        game_solo()
    if mode == 3:
        game_play_ordi()
    return choose_mode()


if __name__ == '__main__':
    choose_mode()
    exit(1)
