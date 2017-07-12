
from chess.objects import board
from chess.test import func


def test_board():
    func.start_report('chess.objects.board')

    my_board = board.Board()

    my_board.init_player_pieces('red', 1)
    my_board.init_player_pieces('blue', 2)

    my_board.print_board()

    func.close_report('chess.objects.board')
