# Integer Console games
Is a collection of simple console-based games written in PY.
The project is designed to demostrate basic game development conseps and provide a fun way to practice Python programming.

## Games included
1. **The Little Proffessor** 
- A game where the player gets two ints to calculate and type in the answer.

2. **Guess The Number** 
- A game where the player tries to guess a randomly generated number within a specified range.

3. **Crocks Game** 
-  Gussing game Where the player guess if n is A Greater than, equal to or less than n.

## Features
* Multiple games in one project
* Dynamically difficulty adjustment based on player performance.
* Simple and intuitive conse-based user interface.
* Possibility to extend with new games.


## Guess the number
The application was implemented as a CS50P assignment.<br>
Also C# versions was implemented as an assignment at GetAcademy [C# version](https://github.com/krigjo25/console-games-cs/blob/master/lib/GuessTheNumber.cs)
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

A demo can be watched at [CS50P's Problem set 4 | Guessing Game](https://cs50.harvard.edu/python/2022/psets/4/game/).

### Game rules
* The computer generates a random number within a specified range.
* You will have to guess the number.
* If you guess correctly, You'll gain a point after few points the level, health points and difficulty will increase.
* If you guess incorrectly, You'll loose a Health Point.

Based on level the difficulty may vary, but the user gets a hint if the user types in a less or greater than answer.

###  Usage
```sh
USAGE : In your terminal, type app.py -h to view the commands available for the game
```

## The Little proffesor
The application was implemented as a CS50P assignment.<br>
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

A demo can be watched at [CS50P's Problem set 4 | Little Proffessor](https://cs50.harvard.edu/python/2022/psets/4/professor/)

 Mathimatical operators used in the program 

-   Additions, 
-   Substractions,
-   Multiply
- ~~`dividision` (floor, reminder), ~~
- ~~`power of` ~~
- and ~~`binary numbers`~
### Game rules
- The game generates two random integers within a specified range.
-   If the equation is correct the computer will generate an answer. There will be an increament of a socre by 1. 
-   When the user has x score the computer will increase health, level & Difficulty based on its algorithm.
- If you guess incorrectly, You'll loose a Health Point.

### Game Goal
- Your objective is to calculate the equation, and send the answer as an input to the question

###  Usage
```sh
USAGE : In your terminal, type app.py -h to view the commands available for the game
```

## Crocks Game
The application was implemented as an assignment at GetAcademy and translated into Python [JavaScript Version]() [C# Version](https://github.com/krigjo25/console-games-cs/blob/master/lib/Crocks.cs)<br>

Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

A demo can be watched at ~~[Youtube : Crocks Game]()~~

### Game rules
- For every round the game will generate two random numbers.
-   If the key are correctly the computer will generate an answer. There will be an increament of a socre by 1. 
-   When the user has x score the computer will increase health, level & Difficulty based on its algorithm.
-   In this game there is only three characters which is allowed to use to make your guess (`=`, `>`, `<`)

### Game Goal
- Your objective is to guess if the first number is (greater than, equal to, or less than) the second number.

###  Usage
```sh
USAGE : In your terminal, type app.py -h to view the commands available for the game
```