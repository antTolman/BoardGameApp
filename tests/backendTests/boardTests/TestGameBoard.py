import unittest
from backend.boards.board import GameBoard
from backend.games.assests.Move import PlayerMove


def createBoard(height, width):
    board = GameBoard(height, width)
    board.initBoard()
    return board


class TestGameBoard(unittest.TestCase):
    height = 4
    width = 5

    def test_init_board(self):
        board = createBoard(self.height, self.width)
        self.assertEqual(board.getBoard(), [[0] * self.width] * self.height)

    def test_init_board_swapped_height_width(self):
        board = createBoard(self.height, self.width)
        self.assertNotEqual(board.getBoard(), [[0] * self.height] * self.width)

    def test_valid_move_out_of_bounds_rows(self):
        board = createBoard(self.height, self.width)
        negative_row_move = PlayerMove((0, 0), (-1, 0), None)
        self.assertFalse(board.isValidMove(negative_row_move),
                         "Input of a negative row end point position was accepted as a valid move")
        out_of_bounds_row = (PlayerMove((0, 0), (4, 0), None))
        self.assertFalse(board.isValidMove(out_of_bounds_row),
                         "Input of an out of bound row end point position was accepted as a valid move")

    def test_valid_move_out_of_bounds_columns(self):
        board = createBoard(self.height, self.width)
        negative_column_move = PlayerMove((0, 0), (0, -1), None)
        self.assertFalse(board.isValidMove(negative_column_move),
                         "Input of a negative column end point position was accepted as a valid move")
        out_of_bounds_cols = (PlayerMove((0, 0), (5, 0), None))
        self.assertFalse(board.isValidMove(out_of_bounds_cols),
                         "Input of an out of bound column end point position was accepted as a valid move")

    def test_valid_moves(self):
        board = createBoard(self.height, self.width)
        valid_move = PlayerMove((0, 0), (1, 1), None)
        self.assertTrue(board.isValidMove(valid_move),
                        "Input of a valid move was deemed invalid")

    def test_invalid_start(self):
        board = createBoard(self.height, self.width)
        invalid_start = PlayerMove((-1, 0), (1, 1), None)
        self.assertFalse(board.isValidMove(invalid_start),
                         "Start position of " + str(invalid_start.getStart()) + " was considered valid")
        invalid_start = PlayerMove((0, -1), (1, 1), None)
        self.assertFalse(board.isValidMove(invalid_start),
                         "Start position of " + str(invalid_start.getStart()) + " was considered valid")
        invalid_start = PlayerMove((4, 0), (1, 1), None)
        self.assertFalse(board.isValidMove(invalid_start),
                         "Start position of " + str(invalid_start.getStart()) + " was considered valid")
        invalid_start = PlayerMove((0, 5), (1, 1), None)
        self.assertFalse(board.isValidMove(invalid_start),
                         "Start position of " + str(invalid_start.getStart()) + " was considered valid")

    def test_board_size(self):
        board = createBoard(self.height, self.width)
        self.assertEqual(board.getBoardSize(), (self.height, self.width))
        self.assertNotEqual(board.getBoardSize(), (self.width, self.height))

    def test_reset_base_board(self):
        board = createBoard(self.height, self.width)
        board.getBoard()[0][0] = 1
        board.resetBoard()
        self.assertEqual(board.getBoard(), [[0] * self.width] * self.height)

if __name__ == '__main__':
    unittest.main()
