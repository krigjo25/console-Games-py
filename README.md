# Game Collections
This project is a suite of console-based educational games developed to demonstrate fundamental game development concepts and logic-based challenges.

## Table of Contents
1. [Overview](#overview)
2. [Games Included](#games-included)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Testing](#testing)
6. [Academic Honesty](#academic-honesty)
7. [License](#license)

## Overview
The suite consists of data-driven integer games designed to boost cognitive skills and reinforce arithmetic proficiency through interactive terminal interfaces. It explores core concepts such as random number generation, input validation, and difficulty scaling.

## Games Included

### 1. Crocks Game
A number comparison challenge where players determine the relationship between two randomly generated integers.
* **Objective**: Guess if the first number is greater than (>), equal to (=), or less than (<) the second number.
* **Mechanics**: Correct guesses increment the score. Reaching specific milestones increases health, level, and difficulty based on the game logic.

### 2. Guess The Number
A classic hidden-number game that challenges players to identify a value within a predefined range.
* **Objective**: Correctly identify the randomly generated number.
* **Mechanics**: Each correct guess earns points. Accumulating points leads to higher levels and increased difficulty, while incorrect guesses result in health loss.

### 3. The Little Professor
An arithmetic trainer that presents players with mathematical equations involving addition, subtraction, or multiplication.
* **Objective**: Calculate the correct result of equations involving two integer operands.
* **Mechanics**: Correct answers increase the score and difficulty. The game reinforces basic arithmetic skills through repetitive practice and escalating challenge levels.

## Installation

1. **Clone the repository**:
   ```sh
   git clone [https://github.com/krigjo25/Console-Games-py.git](https://github.com/krigjo25/Console-Games-py.git)
   cd Console-Games-py
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
To start the application suite, run the main entry point:
```sh
python app.py
```
To view available commands and help options, use:
```sh
python app.py -h
```

## Testing
This project utilizes the pytest framework for quality assurance and automated testing.

* **Run all tests**: 
  ```sh
  pytest testing/
  ```
* **Detailed test output**: 
  ```sh
  pytest test_intgame -s
  ```
* **Test specific classes**: 
  ```sh
  pytest test_intgame -k "classname"
  ```
* **Generate HTML report**: 
  ```sh
  pytest --html=report.htm
  ```

## Academic Honesty
This project includes implementations inspired by CS50P problem sets. Users are reminded to strictly adhere to the Academic Honesty Policy and use this code for educational reference only.

## License
Distributed under the LICENSE file specifications. See the LICENSE file for full details.

---
**Developer**: [krigjo25](https://github.com/krigjo25)
