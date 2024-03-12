# fonction affichage
#affiche_1case(list(grid), int(position))
# prend en arguments la grille de jeu et la position de la case à réveler. Affiche la grille avec cette case uniquement révélée
#affiche_2cases(list(grid), int(position1), int(position2))
# prend en argument la grille de jeu et la position de chacune des deux cases à retourner. Affiche la grille avec ces deux cases uniquement révélées


def grid_to_string_with_size(grid, n, m):
    # affiche la grille de la bonne taille
    # grid est une liste de listes, n et m entiers
    # renvoie une chaîne de caractères
    string_grille = ""
    string_grille += "=== "*m
    string_grille += "\n"
    for k in range(n):
        for i in range(m):
            string_grille += "|"+str(grid[k][i])+"| "
        string_grille += "\n"
        string_grille += "=== "*m
        string_grille += "\n"
    return string_grille


def affiche_grid_cache(grid):
    # affiche la grille que verront les joueurs, avec des croix et des cases vides (les croix sont les cartes face cachée)
    # prend en argument une liste de listes et renvoie une chaîne de caractères
    n = len(grid)
    m = len(grid[0])
    L = []
    for i in range(n):
        M = []
        for j in range(m):
            if grid[i][j] == " ":
                M.append(" ")
            else:
                M.append("X")
        L.append(M)
    return grid_to_string_with_size(L, n, m)


def affiche_1case(grid, pos1):
    # pos1 est un tuple
    # prend en arguments la grille de jeu (liste de listes) et la position de la case à révéler.
    # renvoie la grille de jeu (chaîne de caractères)
    n = len(grid)
    m = len(grid[0])
    L = []
    for i in range(0, n):
        M = []
        for j in range(0, m):
            if (i, j) == pos1:
                M.append(grid[i][j])  # affiche la carte à révéler
            elif grid[i][j] == " ":
                M.append(" ")  # espace dans les cases vides
            else:
                M.append("X")  # x pour les cartes face cachée
        L.append(M)
    return grid_to_string_with_size(L, n, m)


def affiche_2case(grid, pos1, pos2):
    # pos1 et pos2 sont des tuples
    # prend en argument la grille (liste de listes) et la position de chacune des deux cases à retourner.
    # Affiche la grille (chaîne de caractères) avec ces deux cases uniquement révélées
    n = len(grid)
    m = len(grid[0])
    L = []
    for i in range(0, n):
        M = []
        for j in range(0, m):
            if (i, j) == pos1 or (i, j) == pos2:
                M.append(grid[i][j])
            elif grid[i][j] == " ":
                M.append(" ")
            else:
                M.append("X")
        L.append(M)
    return grid_to_string_with_size(L, n, m)
