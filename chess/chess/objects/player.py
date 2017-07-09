from chess.io import output


class Player:

    turn_choice = ['move', 'quit']

    def __init__(self, color, number):
        output.run_log("write", "Player Created")
        self.color = color
        self.number = number

    def turn(self):
        output.run_log("write", "Player " + self.number + "'s Turn")
        while True:
            player_input = input("Player " + self.number + ": ")
            if self.turn_choice.contains(player_input):
                player_input = input("Piece to move (ex: rr): ")
                output.run_log("write", "Player chooses" + player_input)
                return player_input
            print("Player Choices...")
            for choice in self.turn_choice:
                print(choice)