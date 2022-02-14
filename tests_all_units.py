import unittest
import tictactoe_final

class TestTictactoc(unittest.TestCase):
    
    def test_choose_letter(self):
        oi=__builtins__.input
        __builtins__.input=lambda _:'O'
        self.assertEqual(tictactoe_final.choose_letter("aa"), ('o', 'x'))
        __builtins__.input=oi
        
    def test_is_draw(self):
        grid=[" " for x in range(10)]
        self.assertEqual(tictactoe_final.is_grid_full(grid), False)

    def test_is_winner(self):
        grid=[" " for x in range(10)]
        grid[1]=grid[2]=grid[3]='X'
        self.assertEqual(tictactoe_final.is_winner(grid,"X"), True)

    def test_is_not_winner(self):
        grid=[" " for x in range(10)]
        grid[4]=grid[5]=grid[7]='O'
        self.assertEqual(tictactoe_final.is_winner(grid,"O"), False)

if __name__ == '__main__':
    unittest.main()