from game_modes import *
from pytest import *
import builtins
import game_modes
from interaction_player import *
import random


def test_choix_debut_ordi():
    grid = [['2', '4', '5', '7'], ['7', '6', '6', '3'],
            ['8', '4', '1', '8'], ['1', '2', '5', '3']]
    memoire = []
    for i in range(0, 4):
        memoire.append([" "]*4)
    memoire[0][3] = grid[0][3]
    memoire[1][0] = grid[1][0]
    memoire[0][0] = grid[0][0]
    memoire[0][0] = grid[2][3]
    memoire[0][0] = grid[3][0]
    assert choix_debut_ordi(grid, memoire) == ((0, 3), (1, 0))
    memoire[0][3] = " "
    assert choix_debut_ordi(grid, memoire) == ((-1, -1), (-1, -1))


def test_choix_intermediaire_ordi():
    grid = [['2', '4', '5', '7'], ['7', '6', '6', '3'],
            ['8', '4', '1', '8'], ['1', '2', '5', '3']]
    memoire = []
    pos1 = (0, 3)
    for i in range(0, 4):
        memoire.append([" "]*4)
    memoire[0][3] = grid[0][3]
    memoire[1][0] = grid[1][0]
    memoire[0][0] = grid[0][0]
    memoire[0][0] = grid[2][3]
    memoire[0][0] = grid[3][0]
    assert choix_intermediaire_ordi(grid, memoire, pos1) == ((0, 3), (1, 0))
    memoire[0][3] = " "
    assert choix_intermediaire_ordi(grid, memoire, pos1) == ((0, 3), (-1, -1))


'''def mock_input_return2(x):
    # renvoie une commande au hasard
    choix = [1, 2, 3]
    return random.choice(choix)'''


'''def test_choose_mode(monkeypatch):
    monkeypatch.setattr(builtins, "input", mock_input_return2)
    assert choose_mode() in [1, 2, 3]'''
