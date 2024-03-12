# MemoriCS



## Description

MemoriCS permet 3 modes de jeu : 
jeu solo, jeu en 1 contre 1, jeu contre l'ordinateur.
Différents thèmes sont également proposés à l'utilisateur tout comme un nombre de paires au choix de l'utiliateur (2 à 50 paires).

Thèmes proposés : 
- Nombres
- Drapeaux
- Pokemon

Le programme indique le gagnant avec son score (nombre de coups pour gagner pour le jeu en solo et nombre de paires obtenu par joueur pour les 2 autres modes de jeux)

## Installation

Pour joueur au memoriCS, il suffit de cloner le répertoire dans un terminal, d'installer le module playsound sur l'ordinateur à l'aide de la commande dans Visual Studio Code: 
pip install playsound==1.2.2
Il est aussi possible d'installer playsound à l'aide de Windows Powershell.

Pour jouer sans l'interface graphique, il suffit d'exécuter le fichier game_modes.py
Lorsqu'un joueur trouve une paire, il peut rejouer.

Pour jouer avec l'interface graphique, il faut exécuter le fichier Accueil.py
Lorsqu'un joueur trouve une paire, il ne rejoue pas.

# Structure

- Accueil.py : permet de lancer le jeu interface graphique

- game_modes.py : permet de lancer le jeu sans interface graphique, 3 modes possibles

- memory_basic.py : contient les fonctions de base du MVP (création de la grille sous forme de liste de listes, test des paires, comparaison des scores ...)

- affiche_grid.py : fonctions permettant d'afficher la grille sous forme de chaîne de caractères dans le terminal python (face cachée, une case révélée, deux cases révélées)

- interaction_player.py : fonctions permettant au joueur de faire des choix de jeu (taille, choix d'une case)

- gameplay_argparse.py : fichier qui permet de lancer le jeu directement depuis le terminal

- themes.py : contient les dictionnaires avec les images associées à chaque thème, ainsi qu'une fonction qui sélectionne aléatoirement les images qui seront dans la grille pour une partie

- interface_selection.py : permet de sélectionner la taille de la grille, le mode de jeu et le thème pour le jeu avec interface graphique

## Bon jeu