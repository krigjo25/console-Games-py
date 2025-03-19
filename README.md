#  Game Collections
This project comprises a collection of simple, console-based games, written in Python.
The project functions to demostrates and explores fundamental concepts in game development.

Users of this code are reminded to respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.<br>

A preview of [CS50P's Problem set 4 | Guessing Game](https://cs50.harvard.edu/python/2022/psets/4/game/).<br>
A preview of [CS50P's Problem set 4 | Little Proffessor](https://cs50.harvard.edu/python/2022/psets/4/professor/).<br>


## Games included
1. **Crocks Game** 
-  TThis number comparion game tasks the player with determining the relationship between a given number and a target number.
-  The player s challenged to guess whether the given number is greater than, equal to or less than the target number.

2. **Guess The Number** 
- This number-guessing game challenges, the player to guess a randomly generated number within a predefined range.
- The game provides feedback to assist the player and increases in difficulty after each correct guess

3. **The Little Proffessor** 
- This game presents the player with simple arithmetic challenges, involving two integer operands.
- The player must calculate the correct result and input the answer
- Designed to reinforce basic arithmetic skills, the game increases in difficulty after each correct answer

### Crocks Game
Originally implemented as an assignment at Get Academy using [JavaScript](), later translated into [C# Version](https://github.com/krigjo25/console-games-cs/blob/master/lib/Crocks.cs) and Python

Users of this code are reminded to respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.<br>


#### Game rules
- For every round the game will generate two random numbers.
-   If the key are correctly the computer will generate an answer. There will be an increament of a socre by 1. 
-   When the user has x score the computer will increase health, level & Difficulty based on its algorithm.
-   In this game there is only three characters which is allowed to use to make your guess (`=`, `>`, `<`)

#### Game Goal
- Your objective is to guess if the first number is (greater than, equal to, or less than) the second number.

####  Usage
```sh
USAGE : In your terminal, type app.py -h to view the commands available for the game
```


### Guess the number
The initial implementation of this application was developed for a CS50P assignment.
Subsequently a C# version was also implemented as an assignment at Get Academy [C# version](https://github.com/krigjo25/console-games-cs/blob/master/lib/GuessTheNumber.cs).

#### Game rules
- The game begins with the comupter generating a random number within a defined range.
- Player's objective is to guess the generated number.
- A correct guess earns the player a point. The difficulty, the player's level, and health points increases after a specific number of points are earned.
- An incorrect guess leads to the player losing a health point.


### The Little proffesor
The initial implementation of this application was developed for a CS50P assignment.<br>
Users of this code are reminded to respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

The program utilizes the following mathematical operators
-   Addition, 
-   Substraction,
-   Multiplication

#### Game rules
- The game begins with the comupter generating a random number within a defined range. The game generates two random integers within a specified range.
- A correct equation earns the player a point. The difficulty, the player's level, and health points increases after a specific number of points are earned.
- An incorrect equation leads to the player losing a health point.


Thanks for reading, and have a glorious day,
@krigjo25

## Installation
1. Clone the repository:
```sh
# Using SSh 
ssh git@github.com:krigjo25/Console-Games-py.git

# Using git bash
git clone https://github.com/krigjo25/Console-Games-py.git

# Using Github Cli
gh repo clone Console-Games-py
```

2. Navigate to the project directory
```sh
cd Console-Games-py
```

3. Install the requirements
```sh
pip install -r requirements.txt
```

4. Run the file
```sh
python app.py
```

## Testing Framework / Data Sets
The project uses the testing framework <strong>pytest</strong>.

```sh
USEAGE : Type in your terminal pytest <strong>testing/</strong> In order to test the whole dictionary

USEAGE : Type in your terminal pytest <strong>test_intgame -s</strong> to see a more detailed test.

USEAGE : Type in your terminal pytest <strong>test_intgame -k "classname"</strong>, in order to test the classes
USEAGE : Type in your terminal pytest pytest --html=report.htm
```

## Credentials

### LICENSE
See the [LICENSE](./LICENSE) file for details.

### Contact
For any questions or suggestions, please open an issue or contact the me at [e-mail](mailto:krigjo25@outlook.com).

#### Responsories

-   [pytest - by pytest team](https://github.com/pytest-dev/pytest)
-   [random - by Python developer team]()
-   [requests - by Kenneth Reitz](https://requests.readthedocs.io/en/latest/)<nt>


## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a glorious rest of the day,
@krigjo25
