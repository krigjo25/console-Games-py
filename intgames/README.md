# Integer Console games
Is a collection of simple console-based games written in PY.
The project is designed to demostrate basic game development conseps and provide a fun way to practive Python programming.
The games is written and created by [krigjo25](), Some of the games are created as assignments from xCS50 Introduction to Python at Harvard X program Others are created on a free will as converted from a language to another.

## Games included
1. **The Little Proffessor** - A game where the player gets two ints to calculate and type in the answer.
2. **Guess The Number** - A game where the player tries to guess a randomly generated number within a specified range.

## Features
* Multiple games in one project
* Dynamically difficulty adjustment based on player performance.
* Simple and intuitive conse-based user interface.
* Possibility to extend with new games.

##   Requirements
The requirements can be found at requirements.txt

###  Running the games
1. Open the Terminal
2. python path/to/file.py
3. Press Enter to run the project

### Playing the games
* Follow the on screen instruction to play each game.
* Use specified keys to make your guesses
* More details will be specified in [game rules](##Rules)

## Game rules

### Guess the number

* The computer generates a random number within a specified range.
* You will have to guess the number.
* If you guess correctly, You'll gain a point after few points the level, health points and difficulty will increase.
* If you guess incorrectly, You'll loose a Health Point.

Based on level the difficulty may vary, but the user gets a hint if the user types in a less or greater than answer.
```sh
USAGE : In your terminal, type __main__.py -h to view the commands available for the game
```

### The Little proffesor

Originally this game was created as an
assignment at CS50P - Introduction to Python Programming.

 Mathimatical operators used in the program 

-   Additions, 
-   Substractions,
-   Multiply
<!-- ( `dividision` (floor, reminder), `power of` and `binary numbers`,) -->

* The game generates two random integers within a specified range.
* Your objective is to calculate the two prompted numbers, and send the answer as an input to the question
* If you guess correctly, You'll gain a point after few points the level will increase.
* If you guess incorrectly, You'll loose a Health Point.
```sh
USAGE : In your terminal, type __main__.py -h to view the commands available for the game
```
 
## Testing Framework / Data Sets
This project uses the testing framework <strong>pytest</strong>.

```sh
USEAGE : Type in your terminal pytest <strong>testing/</strong> In order to test the whole dictionary

USEAGE : Type in your terminal pytest <strong>test_intgame -s</strong> to see a more detailed test.

USEAGE : Type in your terminal pytest <strong>test_intgame -k "classname"</strong>, in order to test the classes
```