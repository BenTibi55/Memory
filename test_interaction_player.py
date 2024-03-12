from pytest import *
import builtins
import interaction_player
from interaction_player import *
import random


def test_ask_size(monkeypatch):
    monkeypatch.setattr(builtins, "input", mock_input_return)
    assert ask_size() in [(i, j) for i in range(2, 11) for j in range(2, 11)]


def mock_input_return(x):
    # renvoie une commande au hasard
    commandes = [i for i in range(2, 11)]
    return random.choice(commandes)


def test_positions_possibles():
    assert positions_possibles([["3", "3", '5'], [" ", "5", ' ']]) == [
        (0, 0), (0, 1), (0, 2), (1, 1)]


def mock_input_return_choose_case(grid):
    # renvoie une position de case possible au hasard

    return 2


# print(mock_input_return_choose_case([["3", "3", '5'], [" ", "5", ' ']]))

grid = [["3", "3", '5'], [" ", "5", ' ']]


def test_choose_case(monkeypatch):
    monkeypatch.setattr(builtins, "input",
                        lambda x: mock_input_return_choose_case(grid))
    assert choose_case([["3", "3", '5'], [" ", "5", ' ']]) in [
        (0, 0), (0, 1), (0, 2), (1, 1)]


# print(test_interaction_player(monkeypatch))


# print(choose_case([["3", "3", '5'], [" ", "5", ' ']]))
