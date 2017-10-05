# PyConsole
Python 3 Chess Application

## Version 0.3.0
Click [here](RELEASE-NOTES.md) for details.

## Run Application
> \> python3 __main__.py

## Chess Rules
### End Of Game
* Win
  * Capture the King.
  * If the King is captured, Game Over!
* Draw
  * Agreement
### Basics
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
### Special Rules
* Promote the Pawn
  * If a pawn manages to make it to the other side of the board, it can be replaced with a friendly piece captured by the enemy team
* En Passant
  * This occurs if a pawn moves two squares, landing adjacent to an enemy spawn.
  * On the opposing player's turn, they are allowed to capture the pawn as if it only moved one square
* Castle
  * The King may move two squares to it's side, place a rook in the square it would normally move to.
  * For this move to happen, the following rules must apply
    * It must be both the King's and Rook's first move
    * There cannot be a piece between the King and Rook
    * The King cannot be, nor pass through check

## Future Features & TODO
* Change how the moves function works
  * Return dict saying what move is being done
    * Regular Move
    * Special Move
* Implement Special Moves
  * Castling
  * En Passant
  * Promote the Pawn
* Check(mate)
  * Do not allow King to stay in Check
  * Do not allow King to move into Check
* New Game
  * Fix: Pieces on field are not removed.
* Control Player's Turns
* Save and Load Game Functions
* Improve the Worth System of pieces beyond only counting the piece. 
  * I.E. Count combination of Pieces, not just the individual.

## License
This project is licensed under the terms of the MIT license.
> [license](LICENSE.md)
