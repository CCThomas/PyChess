# Notes
# - Board will check is move is on the board and if a piece is already there.

from chess.objects import pieces
from chess.test import func


def test_pieces():
    func.start_report('chess.objects.pieces')

    test_piece()
    test_bishop()
    test_king()
    test_knight()
    test_pawn()
    test_queen()
    test_queen()

    func.close_report('chess.objects.pieces')


def test_piece():
    piece = pieces.Piece("orange")

    func.start_test_on('chess.objects.pieces.Piece')

    # Test Getters
    func.should_equal('chess.objects.pieces.Piece get_color()', piece.get_color(), 'orange')
    func.should_equal('chess.objects.pieces.Piece get_letter()', piece.get_letter(), None)
    func.should_equal('chess.objects.pieces.Piece convert_letter()', piece.convert_letter(), None)
    func.should_equal('chess.objects.pieces.Piece get_name()', piece.get_name(), 'o--')
    func.should_equal('chess.objects.pieces.Piece get_number()', piece.get_number(), None)
    func.should_equal('chess.objects.pieces.Piece get_position()', piece.get_position(), None)
    # Test Position A and 1
    piece.set_position("A1")
    func.should_equal('chess.objects.pieces.Piece get_letter()', piece.get_letter(), 'A')
    func.should_equal('chess.objects.pieces.Piece convert_letter()', piece.convert_letter(), 1)
    func.should_equal('chess.objects.pieces.Piece get_number()', piece.get_number(), '1')
    # Test Position B and 2
    piece.set_position("B2")
    func.should_equal('chess.objects.pieces.Piece get_letter()', piece.get_letter(), 'B')
    func.should_equal('chess.objects.pieces.Piece convert_letter()', piece.convert_letter(), 2)
    func.should_equal('chess.objects.pieces.Piece get_number()', piece.get_number(), '2')
    # Test Position C and 3
    piece.set_position("C3")
    func.should_equal('chess.objects.pieces.Piece get_letter()', piece.get_letter(), 'C')
    func.should_equal('chess.objects.pieces.Piece convert_letter()', piece.convert_letter(), 3)
    func.should_equal('chess.objects.pieces.Piece get_number()', piece.get_number(), '3')
    # Test Position D and 4
    piece.set_position("D4")
    func.should_equal('chess.objects.pieces.Piece get_letter()', piece.get_letter(), 'D')
    func.should_equal('chess.objects.pieces.Piece convert_letter()', piece.convert_letter(), 4)
    func.should_equal('chess.objects.pieces.Piece get_number()', piece.get_number(), '4')
    # Test Position E and 5
    piece.set_position("E5")
    func.should_equal('chess.objects.pieces.Piece get_letter()', piece.get_letter(), 'E')
    func.should_equal('chess.objects.pieces.Piece convert_letter()', piece.convert_letter(), 5)
    func.should_equal('chess.objects.pieces.Piece get_number()', piece.get_number(), '5')
    # Test Position F and 6
    piece.set_position("F6")
    func.should_equal('chess.objects.pieces.Piece get_letter()', piece.get_letter(), 'F')
    func.should_equal('chess.objects.pieces.Piece convert_letter()', piece.convert_letter(), 6)
    func.should_equal('chess.objects.pieces.Piece get_number()', piece.get_number(), '6')
    # Test Position G and 7
    piece.set_position("G7")
    func.should_equal('chess.objects.pieces.Piece get_letter()', piece.get_letter(), 'G')
    func.should_equal('chess.objects.pieces.Piece convert_letter()', piece.convert_letter(), 7)
    func.should_equal('chess.objects.pieces.Piece get_number()', piece.get_number(), '7')
    # Test Position H and 8
    piece.set_position("H8")
    func.should_equal('chess.objects.pieces.Piece get_letter()', piece.get_letter(), 'H')
    func.should_equal('chess.objects.pieces.Piece convert_letter()', piece.convert_letter(), 8)
    func.should_equal('chess.objects.pieces.Piece get_number()', piece.get_number(), '8')

    func.print_and_restart_tracker()


def test_bishop():
    bishop = pieces.Bishop("orange")

    func.start_test_on('chess.objects.pieces.Bishop')
    bishop.set_position('D5')

    # Check Valid moves
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("A2")', bishop.is_move_valid("A2"), True)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("B3")', bishop.is_move_valid("B3"), True)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("B7")', bishop.is_move_valid("B7"), True)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("E4")', bishop.is_move_valid("E4"), True)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("F7")', bishop.is_move_valid("F7"), True)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("G2")', bishop.is_move_valid("G2"), True)
    # Check InValid Moves
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("B2")', bishop.is_move_valid("B2"), False)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("B6")', bishop.is_move_valid("B6"), False)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("D2")', bishop.is_move_valid("D2"), False)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("D7")', bishop.is_move_valid("D7"), False)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("F5")', bishop.is_move_valid("F5"), False)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("F7")', bishop.is_move_valid("F8"), False)
    func.should_equal('chess.objects.pieces.Bishop is_move_valid("H3")', bishop.is_move_valid("H3"), False)

    func.print_and_restart_tracker()


def test_king():
    king = pieces.King("orange")

    func.start_test_on('chess.objects.pieces.King')
    king.set_position('D5')

    # Check Valid moves
    func.should_equal('chess.objects.pieces.King is_move_valid("C4")', king.is_move_valid("C4"), True)
    func.should_equal('chess.objects.pieces.King is_move_valid("C5")', king.is_move_valid("C5"), True)
    func.should_equal('chess.objects.pieces.King is_move_valid("C6")', king.is_move_valid("C6"), True)
    func.should_equal('chess.objects.pieces.King is_move_valid("D4")', king.is_move_valid("D4"), True)
    func.should_equal('chess.objects.pieces.King is_move_valid("D6")', king.is_move_valid("D6"), True)
    func.should_equal('chess.objects.pieces.King is_move_valid("E4")', king.is_move_valid("E4"), True)
    func.should_equal('chess.objects.pieces.King is_move_valid("E5")', king.is_move_valid("E5"), True)
    func.should_equal('chess.objects.pieces.King is_move_valid("E6")', king.is_move_valid("E6"), True)
    # Check InValid Moves
    func.should_equal('chess.objects.pieces.King is_move_valid("A5")', king.is_move_valid("A5"), False)
    func.should_equal('chess.objects.pieces.King is_move_valid("B2")', king.is_move_valid("B2"), False)
    func.should_equal('chess.objects.pieces.King is_move_valid("C7")', king.is_move_valid("C7"), False)
    func.should_equal('chess.objects.pieces.King is_move_valid("D3")', king.is_move_valid("D3"), False)
    func.should_equal('chess.objects.pieces.King is_move_valid("E1")', king.is_move_valid("E1"), False)
    func.should_equal('chess.objects.pieces.King is_move_valid("F5")', king.is_move_valid("F5"), False)
    func.should_equal('chess.objects.pieces.King is_move_valid("G8")', king.is_move_valid("G8"), False)
    func.should_equal('chess.objects.pieces.King is_move_valid("H4")', king.is_move_valid("H4"), False)

    func.print_and_restart_tracker()


def test_knight():
    knight = pieces.Knight("orange")

    func.start_test_on('chess.objects.pieces.Knight')
    knight.set_position('D5')

    # Check Valid moves
    func.should_equal('chess.objects.pieces.Knight is_move_valid("B4")', knight.is_move_valid("B4"), True)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("B6")', knight.is_move_valid("B6"), True)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("C3")', knight.is_move_valid("C3"), True)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("C7")', knight.is_move_valid("C7"), True)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("E3")', knight.is_move_valid("E3"), True)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("E7")', knight.is_move_valid("E7"), True)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("F4")', knight.is_move_valid("F4"), True)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("F6")', knight.is_move_valid("F6"), True)
    # Check InValid Moves
    func.should_equal('chess.objects.pieces.Knight is_move_valid("B3")', knight.is_move_valid("B3"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("B5")', knight.is_move_valid("B5"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("B7")', knight.is_move_valid("B7"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("C4")', knight.is_move_valid("C4"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("C5")', knight.is_move_valid("C5"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("C6")', knight.is_move_valid("C6"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("D3")', knight.is_move_valid("D3"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("D4")', knight.is_move_valid("D4"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("D6")', knight.is_move_valid("D6"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("D7")', knight.is_move_valid("D7"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("E4")', knight.is_move_valid("E4"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("E5")', knight.is_move_valid("E5"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("E6")', knight.is_move_valid("E6"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("F3")', knight.is_move_valid("F3"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("F5")', knight.is_move_valid("F5"), False)
    func.should_equal('chess.objects.pieces.Knight is_move_valid("F7")', knight.is_move_valid("F7"), False)

    func.print_and_restart_tracker()


def test_pawn():
    pawn_one = pieces.Pawn("orange", 1)
    pawn_two = pieces.Pawn("orange", 2)

    func.start_test_on('chess.objects.pieces.Pawn')
    pawn_one.set_position('B2')
    pawn_two.set_position('B7')

    # Check Valid moves for Pawn One
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("B3")', pawn_one.is_move_valid("B3"), True)
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("B4") First', pawn_one.is_move_valid("B4"), True)
    pawn_one.set_position('B3')
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("B4") Second', pawn_one.is_move_valid("B4"), True)
    # Check Valid moves for Pawn Two
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("B6")', pawn_two.is_move_valid("B6"), True)
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("B5") First', pawn_two.is_move_valid("B5"), True)
    pawn_two.set_position('B6')
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("B5") Second', pawn_two.is_move_valid("B5"), True)

    # Reset Pawn
    pawn_one.set_position(None)
    pawn_two.set_position(None)
    pawn_one.set_position('B2')
    pawn_two.set_position('B7')

    # Check InValid Moves for Pawn One
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("A2")', pawn_one.is_move_valid("A2"), False)
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("A3")', pawn_one.is_move_valid("A3"), False)
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("B1")', pawn_one.is_move_valid("B1"), False)
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("B5") First', pawn_one.is_move_valid("B5"), False)
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("C2")', pawn_one.is_move_valid("C2"), False)
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("C3")', pawn_one.is_move_valid("C3"), False)
    pawn_one.set_position('B3')
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("B5") Second', pawn_one.is_move_valid("B5"), False)
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("B6")', pawn_one.is_move_valid("B6"), False)
    func.should_equal('chess.objects.pieces.Pawn One is_move_valid("C7")', pawn_one.is_move_valid("C7"), False)

    # Check InValid Moves for Pawn Two
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("A6")', pawn_two.is_move_valid("A6"), False)
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("A7")', pawn_two.is_move_valid("A7"), False)
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("B4") First', pawn_two.is_move_valid("B4"), False)
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("B8")', pawn_two.is_move_valid("B8"), False)
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("C6")', pawn_two.is_move_valid("C6"), False)
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("C7")', pawn_two.is_move_valid("C7"), False)
    pawn_two.set_position('B6')
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("B4") Second', pawn_two.is_move_valid("B4"), False)
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("B3")', pawn_two.is_move_valid("B3"), False)
    func.should_equal('chess.objects.pieces.Pawn Two is_move_valid("A5")', pawn_two.is_move_valid("A5"), False)

    func.print_and_restart_tracker()


def test_queen():
    queen = pieces.Queen("orange")

    func.start_test_on('chess.objects.pieces.Queen')
    queen.set_position('D5')

    # Check Valid moves
    func.should_equal('chess.objects.pieces.Queen is_move_valid("A2")', queen.is_move_valid("A2"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("A5")', queen.is_move_valid("A5"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("B3")', queen.is_move_valid("B3"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("B5")', queen.is_move_valid("B5"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("B7")', queen.is_move_valid("B7"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("D1")', queen.is_move_valid("D1"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("D3")', queen.is_move_valid("D3"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("D6")', queen.is_move_valid("D6"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("D8")', queen.is_move_valid("D8"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("E4")', queen.is_move_valid("E4"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("E5")', queen.is_move_valid("E5"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("F7")', queen.is_move_valid("F7"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("G2")', queen.is_move_valid("G2"), True)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("H5")', queen.is_move_valid("H5"), True)



    # Check InValid Moves
    func.should_equal('chess.objects.pieces.Queen is_move_valid("A4")', queen.is_move_valid("A4"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("B2")', queen.is_move_valid("B2"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("B6")', queen.is_move_valid("B6"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("B8")', queen.is_move_valid("B8"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("C2")', queen.is_move_valid("C2"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("E7")', queen.is_move_valid("E7"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("F7")', queen.is_move_valid("F8"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("F2")', queen.is_move_valid("F2"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("G4")', queen.is_move_valid("G4"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("H3")', queen.is_move_valid("H3"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("H6")', queen.is_move_valid("H6"), False)
    func.should_equal('chess.objects.pieces.Queen is_move_valid("H8")', queen.is_move_valid("H8"), False)

    func.print_and_restart_tracker()


def test_rook():
    rook = pieces.Rook("orange")

    func.start_test_on('chess.objects.pieces.Rook')
    rook.set_position('D5')

    # Check Valid moves
    func.should_equal('chess.objects.pieces.Rook is_move_valid("A5")', rook.is_move_valid("A5"), True)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("B5")', rook.is_move_valid("B5"), True)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("D1")', rook.is_move_valid("D1"), True)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("D3")', rook.is_move_valid("D3"), True)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("D6")', rook.is_move_valid("D6"), True)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("D8")', rook.is_move_valid("D8"), True)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("E5")', rook.is_move_valid("E5"), True)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("H5")', rook.is_move_valid("H5"), True)
    # Check InValid Moves
    func.should_equal('chess.objects.pieces.Rook is_move_valid("A4")', rook.is_move_valid("A4"), False)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("B8")', rook.is_move_valid("B8"), False)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("C2")', rook.is_move_valid("C2"), False)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("C6")', rook.is_move_valid("C6"), False)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("E7")', rook.is_move_valid("E7"), False)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("F2")', rook.is_move_valid("F2"), False)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("G4")', rook.is_move_valid("G4"), False)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("H6")', rook.is_move_valid("H6"), False)
    func.should_equal('chess.objects.pieces.Rook is_move_valid("H8")', rook.is_move_valid("H8"), False)

    func.print_and_restart_tracker()