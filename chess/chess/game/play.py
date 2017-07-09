from chess.objects.player import Player
from chess.objects.board import Board


def init_game():
    board = Board()
    board.init_player_pieces('red', 1)
    player_one = Player('red', 1)
    board.init_player_pieces('blue', 2)
    player_two = Player('blue', 2)
    board.print_board()

    import sys

    while True:
        player_one_choice = player_one.turn()
        #if player_one_choice == move
