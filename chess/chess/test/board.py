
from chess.objects import board
from chess.test import func


def test_board():
    func.start_report('chess.objects.board')

    my_board = board.Board()

    my_board.init_player_pieces('red', 1)
    my_board.init_player_pieces('blue', 2)

    # Test move_piece
    func.should_equal('chess.objects.board.Board my_board.move_piece("rp", "E4", "E4", 1)',
                      my_board.move_piece("rp", "E4", "E4", 1), "No Piece At Location")
    func.should_equal('chess.objects.board.Board my_board.move_piece("rp", "E2", "E4", 2)',
                      my_board.move_piece("rp", "E2", "E4", 2), "Not Player's Piece")
    func.should_equal('chess.objects.board.Board my_board.move_piece("rp", "E1", "E4", 1)',
                      my_board.move_piece("rp", "E1", "E4", 1), "Piece Not At Location")
    func.should_equal('chess.objects.board.Board my_board.move_piece("rp", "E2", "B0", 1)',
                      my_board.move_piece("rp", "E2", "B0", 1), "Location Not On Board")
    func.should_equal('chess.objects.board.Board my_board.move_piece("rp", "E2", "E4", 1)',
                      my_board.move_piece("rp", "E2", "E4", 1), "True")

    func.should_equal('chess.objects.board.Board my_board.move_piece("bb", "C8", "E6", 2)',
                      my_board.move_piece("bb", "C8", "E6", 2), "Path Not Clear")
    func.should_equal('chess.objects.board.Board my_board.move_piece("bK", "D8", "D7", 2)',
                      my_board.move_piece("bK", "D8", "D7", 2), "Destination Is Help By Friendly Piece")
    func.should_equal('chess.objects.board.Board my_board.move_piece("bp", "D7", "E5", 2)',
                      my_board.move_piece("bp", "D7", "E5", 2).split('\n')[0],
                      "This Piece Can Not Make That Move. Valid Moves As Follows")

    func.close_report('chess.objects.board')