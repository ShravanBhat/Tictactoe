import unittest
import sys
sys.path.insert(0, '../')
import tictactoe_final
from io import StringIO


class TestTictactoc(unittest.TestCase):
    #check if correct letter is assigned to players or not
    def test_choose_letter(self):
        oi=__builtins__.input
        __builtins__.input=lambda _:'O'
        self.assertEqual(tictactoe_final.choose_letter("Shravan"), ('o', 'x'))
        __builtins__.input=oi

    #check if False is returned or not in case any position in grid is empty    
    def test_is_draw(self):
        grid=[" " for x in range(10)]
        self.assertEqual(tictactoe_final.is_grid_full(grid), False)

    #Check if is_winner returns true if any winning conditions is met
    def test_is_winner(self):
        grid=[" " for x in range(10)]
        grid[1]=grid[2]=grid[3]='X'
        self.assertEqual(tictactoe_final.is_winner(grid,"X"), True)

    #Check if is_winner returns False if no winning conditions is met
    def test_is_not_winner(self):
        grid=[" " for x in range(10)]
        grid[4]=grid[5]=grid[7]='O'
        self.assertEqual(tictactoe_final.is_winner(grid,"O"), False)

if __name__ == '__main__':
    unittest.main()