import unittest
import tictactoe as ttt


class TestTicTacToe(unittest.TestCase):

    def test_initial_state(self):
        board = ttt.initial_state()
        self.assertEqual(len(board), 3)
        self.assertTrue(all(len(row) == 3 for row in board))
        self.assertTrue(all(cell == ttt.EMPTY for row in board for cell in row))

    def test_player(self):
        board = ttt.initial_state()
        self.assertEqual(ttt.player(board), ttt.X)

        board = [[ttt.X, ttt.O, ttt.X],
                 [ttt.O, ttt.X, ttt.EMPTY],
                 [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]]
        self.assertEqual(ttt.player(board), ttt.O)

    def test_actions(self):
        board = ttt.initial_state()
        actions = ttt.actions(board)
        self.assertEqual(len(actions), 9)
        self.assertIn((0, 0), actions)

    def test_result(self):
        board = ttt.initial_state()
        new_board = ttt.result(board, (1, 1))
        self.assertEqual(new_board[1][1], ttt.X)
        self.assertEqual(board[1][1], ttt.EMPTY)  # original board remains unchanged

        with self.assertRaises(ValueError):
            ttt.result(board, (3, 3))  # Invalid position

    def test_winner(self):
        board = [
            [ttt.X, ttt.X, ttt.X],
            [ttt.O, ttt.O, ttt.EMPTY],
            [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
        ]
        self.assertEqual(ttt.winner(board), ttt.X)

        board = [
            [ttt.O, ttt.X, ttt.X],
            [ttt.O, ttt.EMPTY, ttt.X],
            [ttt.O, ttt.EMPTY, ttt.EMPTY]
        ]
        self.assertEqual(ttt.winner(board), ttt.O)

        board = ttt.initial_state()
        self.assertIsNone(ttt.winner(board))

    def test_terminal(self):
        board = [
            [ttt.X, ttt.O, ttt.X],
            [ttt.X, ttt.O, ttt.O],
            [ttt.O, ttt.X, ttt.X]
        ]
        self.assertTrue(ttt.terminal(board))

        board = ttt.initial_state()
        self.assertFalse(ttt.terminal(board))

    def test_utility(self):
        board = [
            [ttt.X, ttt.X, ttt.X],
            [ttt.O, ttt.O, ttt.EMPTY],
            [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
        ]
        self.assertEqual(ttt.utility(board), 1)

        board = [
            [ttt.O, ttt.O, ttt.O],
            [ttt.X, ttt.X, ttt.EMPTY],
            [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
        ]
        self.assertEqual(ttt.utility(board), -1)

        board = [
            [ttt.X, ttt.O, ttt.X],
            [ttt.O, ttt.O, ttt.X],
            [ttt.X, ttt.X, ttt.O]
        ]
        self.assertEqual(ttt.utility(board), 0)

    def test_minimax_terminal(self):
        board = [
            [ttt.X, ttt.X, ttt.X],
            [ttt.O, ttt.O, ttt.EMPTY],
            [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
        ]
        self.assertIsNone(ttt.minimax(board))

    def test_minimax_optimal(self):
        board = ttt.initial_state()
        action = ttt.minimax(board)
        self.assertIn(action, ttt.actions(board))  # Deve ser uma jogada válida


if __name__ == '__main__':
    unittest.main()
