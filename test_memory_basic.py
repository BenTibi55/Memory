
from pytest import *
from memory_basic import *


def test_create_grid():
    assert len(create_grid(3, 4)) == 3
    assert len(create_grid(6, 2)[0]) == 2


def test_is_a_pair():
    assert is_a_pair([[2, 3, 2], [5, 4, 3]], (0, 1), (1, 2)) == True
    assert is_a_pair([[2, 3, 2], [5, 4, 3]], (1, 1), (1, 2)) == False


def test_remove_pair():
    assert remove_pair([[2, 3, 2], [5, 4, 3]], (0, 1), (1, 2)) == [
        [2, ' ', 2], [5, 4, ' ']]


def test_is_case_filled():
    L = [['a', ' '], ['b', 'c']]
    assert is_case_filled(L, (0, 0)) == True
    assert is_case_filled(L, (0, 1)) == False


def test_is_game_over():
    L = [[' ', ' '], [' ', ' ']]
    M = [[' ', ' '], [' ', 'b']]
    assert is_game_over(L) == True
    assert is_game_over(M) == False


def test_compare_scores():
    assert compare_scores(5, 8) == print('Le joueur 1 a gagné')
    assert compare_scores(8, 5) == print('Le joueur 2 a gagné')
    assert compare_scores(5, 5) == print('Egalité')


def test_compare_scores_ordi():
    assert compare_scores_ordi(8, 5) == print(
        "Le joueur 1 a gagné avec un score de 8 contre un score de 5 pour l'ordinateur !")
    assert compare_scores_ordi(5, 8) == print(
        "L'ordinateur a gagné avec un score de 8 contre un score de 5 pour le joueur 1 !")
    assert compare_scores_ordi(5, 5) == print("Egalité")
