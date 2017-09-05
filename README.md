# PyChess
Python 3 Chess Application
[Spritesheet](https://www.raywenderlich.com/1223/python-tutorial-how-to-generate-game-tiles-with-python-imaging-library)

## Version 0.1.0
Can Play rough version of Game

## Run Application
Navigate to parent directory
> \> python3 chess

## Contributing
1. Branch from Master
2. Make changes
3. Write test for changes (if possible)
4. Update Version Number
   1. Look [here](http://semver.org/) for help
5. Update Readme and other .md
6. Merge Branch with Master

### Style Guide
[PEP 8](https://www.python.org/dev/peps/pep-0008/)<br/>

### Chess Rules
#### End Of Game
* Win 
  * Capture the King.
  * If the King is captured, Game Over!
* Draw
  * Agreement
#### Basics
There are six different pieces in Chess, and can move as follows
* King
  * The King can move one square in any direction
* Queen
  * The Queen can move as many squares, in any single direction, as long there is no piece blocks that path.
* Bishop
  * The bishop can move as many squares, in a diagonal path, as long as there is no piece blocks that path.
* Knight
  * The knight can move two squares in one direction, then one square at a 90 degree angle to that second square.
  * Unlike other pieces, the Knight can jump other pieces that are in it's path.
* Rook
  * The rook can move as many squares, forwards, backwards, or sideways, as long as there is no piece blocking that path.
* Pawn
  * The pawn can move forward one square.
  * It can only attack the square that is in the forward-diagonal position to it's location
  * If a pawn encounters a piece in the square in front of it, it can no longer move.
  * On a pawns first move, it can move two squares forwards instead of one, as long as it does not inferior with the previous rule.
#### Special Rules
* Promote the Pawn
  * If a pawn manages to make it to the other side of the board, it can be replaced with a friendly piece captured by the enemy team
* en passant
  * This occurs if a pawn moves two squares, landing adjacent to an enemy spawn.
  * On the opposing player's turn, they are allowed to capture the pawn as if it only moved one square
* Castle
  * The King may move two squares to it's side, place a rook in the square it would normally move to.
  * For this move to happen, the following rules must apply
    * It must be both the King's and Rook's first move
    * There cannot be a piece between the King and Rook
    * The King cannot be, nor pass through check

### Features

#### TODO
General
* Draw Board
* Movement for Chess Pieces
* Implement Special Moves
* Calculate Check
* Chess Pieces Worth

#### Future
General
* Add new Games
  * Checkers

GUI
* Draw all objects
* Can move objects with mouse
* Board shows you where each piece can move, on hover
* Add Language Support
  * Due to Terminal Complications, Language support will not be implemented until GUI Version

AI
* Create AI to play against
* Add Difficulty to AI (Optional)


## License
This project is licensed under the terms of the MIT license.
> [license](LICENSE.md)
