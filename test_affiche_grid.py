from affiche_grid import *

grid = [[" "," "," "," "],["5","5","5"," "],["6","7","8","9"]]
def test_grid_to_string_with_size():
    a=""""
=== === === === 
| | | | | | | | 
=== === === === 
|5| |5| |5| | | 
=== === === === 
|6| |7| |8| |9| 
=== === === === 

"""
    assert grid_to_string_with_size(grid,3,4)== a[2:-1]
    
def test_affiche_grid_cache():
    a=""""
=== === === === 
| | | | | | | | 
=== === === === 
|X| |X| |X| | | 
=== === === === 
|X| |X| |X| |X| 
=== === === === 

"""
    assert affiche_grid_cache(grid) == a[2:-1]
    
def test_affiche_1case():
    a=""""
=== === === === 
| | | | | | | | 
=== === === === 
|X| |X| |X| | | 
=== === === === 
|X| |X| |X| |9| 
=== === === === 

"""
    assert affiche_1case(grid,(2,3)) == a[2:-1]
    

def test_affiche_2case():
    a=""""
=== === === === 
| | | | | | | | 
=== === === === 
|X| |X| |5| | | 
=== === === === 
|X| |X| |X| |9| 
=== === === === 

"""
    assert affiche_2case(grid,(2,3),(1,2)) == a[2:-1]
    


    
