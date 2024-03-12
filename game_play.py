from game_modes import *
from memory_basic import *
from affiche_grid import *
from themes import *
from jeu_solo import *
from jeu_a_2 import *


def str_to_theme(theme):
    if theme == "Drapeaux":
        return Drapeaux
    if theme == "Pokémons":
        return Pokemon
    if theme == "Animaux":
        return Animaux


def game(n, m, mode_jeu, theme):
    if mode_jeu == 'jeu 1v1':
        return jeu_a_deux(n, m, str_to_theme(theme))
    elif mode_jeu == 'jeu solo':
        return jeu_solo(n, m, str_to_theme(theme))
