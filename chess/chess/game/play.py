from chess.objects.player import Player
from chess.objects.board import Board

board = None

"""
def move(move_to, player_turn):
    global board
    move_split = move_to.split(' ')
    if board.is_piece_on_board(move_split[1]):
        if move_split[1][0] == board.get_player_color(player_turn)[0]:
            if board.is_reference_on_board(move_split[2]):
                if board.can_piece_make_move(move_split[1], move_split[2]):
                    if board.can_player_move_here(move_split[2]):
                        board.move_piece(move_split[1], move_split[2])
                        return True
                    else:
                        print("Player Can't Move Piece There")
                else:
                    print("Not a Valid Move")
            else:
                print("Move Not On Board")
        else:
            print("Not Your Piece")
    else:
        print("Piece Does Not Exist")
    return False
"""

# move bp A7 A6


def init_game():
    global board
    board = Board()
    board.init_player_pieces('red', 1)
    board.init_player_pieces('blue', 2)

    counter = 0
    previous_command = None
    player_turn = 1
    while True:
        counter = counter + 1
        print("Counter: " + str(counter))
        if previous_command is not None:
            print("Previous Command: " + previous_command)
        board.print_board()
        player_command = input("Player " + str(player_turn) + ":")
        previous_command = player_command
        player_command_split = player_command.split(' ')
        if player_command_split[0] == 'move':
            success = board.move_piece(player_command_split[1], player_command_split[2], player_command_split[3], player_turn)
            if success == "True" and player_turn == 1:
                player_turn = 2
            elif success == "True" and player_turn == 2:
                player_turn = 1
            else:
                print("Message: " + success)
        elif player_command == 'save':
            print("TODO: Implement Save Feature")
        elif player_command == 'quit':
            break
        else:
            print("TODO: Implement ELSE Feature")