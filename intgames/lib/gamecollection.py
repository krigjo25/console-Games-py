#   Importing Responsories
import sys, time as t

from lib.dict.game_over import GameOver
from lib.config.config import GameConfig

#   Initializing the Logger
logger = GameConfig().logger
logger = logger.FileHandler()

# Refactoring the code
class LittleProfessor(GameConfig):

    """
        The Little Professor Game
        The user has to solve the mathematical equation that the computer has generated.
        The user has to solve the equation within the range of 1- x.
        if the user's health points are zero, the game will end.
    """

    def __init__(self):
        self.logger = logger

    def run(self): 

         #   Initializing Game Configurations
        self.HP = 3
        answer = ""

        while True:

            #   Initializing the game
            n = self.TLPAlgorithm(self.Level)

            #   Ensure that the user has zero health points left
            self.QuitGame(n[0], answer)

            #   Prompting the user for the output
            answer = input(f'{n[1]} = :')

            try :

                #   Ensure the variable contains an integer
                if not answer.isnumeric(): 
                    raise ValueError("The input is not a number")

            except (ValueError, Exception) as e:

                #   Decrease self.HP by one and notify the user about the incorrect answer
                self.IncorrectAnswer(e)

            self.CorrectAnswer(f"Correct answer") if int(answer) == n[0] else self.IncorrectAnswer(f"EEE")

            #   Breaking out of the loop
            if self.Level == 10:
                
                return print(f"Score : {self.Score}\nLevels completed : {self.Level}")

class GuessTheNumber(GameConfig):
    """
        Classic Guess the number game

        The user has to guess the number that the computer has generated.
        The user has to guess the number within the range of 1- x.
        if the user's health points are zero, the game will end.

    """
    def __init__(self):
        self.logger = logger

    def run(self):

        #   Game Configurations
        self.HP = 9
        
        n = self.GenerateIntegers(self.Level)

        self.logger.info(f"{self.__class__.__name__}: The game has started !")

        #   Start the timer
        start = t.perf_counter()

        while True:

            #   Ensure that the user has zero health points left
            self.QuitGame(self.HP)

            #   Prompting the user
            answer = input(f'{n[1]} ')

            try :

                #   Ensure that the user has inputted a number
                if not answer.isnumeric(): 
                    raise ValueError("The input is not a number")
                

            except (ValueError, TypeError, Exception) as e: 
                
                #   Decrease the self.HP by one and notify the user about the incorrect answer
                self.IncorrectAnswer(e)

                self.logger.warn(f"{self.__class__.__name__}: {e}")
                

            if int(answer) == n[0]: 
                    
                    #   Notify the user about the correct answer
                    self.CorrectAnswer(f"Correct answer")

                    #   Generating new integers
                    n = self.GenerateIntegers(self.Level)
    
            else:

                #   Notify the user about the incorrect answer and decrease the self.HP by one
                self.IncorrectAnswer('Too low, guess higher') if n[0] > int(answer) else self.IncorrectAnswer('Too high, guess lower')

                self.logger.warn(f"{self.__class__.__name__}:")

            period = t.perf_counter() - start

            self.logger.info(f"{self.__class__.__name__}: GameLevel : \t lvl : {self.Level} Current Score: {self.Score } / {self.CompareScore},  {period}")

class Crocks(GameConfig):
    """
        Crockodile Game
        The user has to guess whether the number is greater or less than the other number,
        or equal to the other number else the user's health points will decrease.
        if the user's health points are zero, the game will end.

    """
    def __init__(self):
        self.logger = logger
    
    def run(self):

        #   Game Configurations

        #   Initializing the game
        self.HP = 3
        n = [self.GenerateIntegers(self.Level), self.GenerateIntegers(self.Level)]

        while True:

            #   Prompting the user
            answer = str(input(f'Is {n[0][0]} >=< {n[1][0]}? :\t'))

            #   Ensure that the user does not input any characters which are not allowed
            try :

                #   Ensure that the user has zero health points left
                if self.HP == 0: 
                    self.QuitGame(n, answer)

                #   Ensure that the user has inputted the correct answer
                if answer not in ['>', '<', '=']:
                    raise ValueError('Invalid input')

            except (ValueError, TypeError, Exception) as e: 
                
                #   Decrease the self.HP by one
                self.HP -= 1

                #   Notify the user about the incorrect answer
                self.IncorrectAnswer(e)

            #   Evaulate the answer and ensure that the user has the correct answer
            if n[0][0] > n[1][0] and answer == '>':
            
                #  Increasing the score
                self.Score += 1

                #   Notify the user about the correct answer
                self.CorrectAnswer(f"Correct answer")

                #   Generating new integers
                n = [self.GenerateIntegers(self.Level), self.GenerateIntegers(self.Level)]

            #   Evaulate the answer and ensure that the user has the correct answer
            elif n[0][0] < n[1][0] and answer == '<':
            
                #  Increasing the score
                self.Score += 1

                #   Notify the user about the correct answer
                self.CorrectAnswer()

                #   Generating new integers
                n = [self.GenerateIntegers(self.Level), self.GenerateIntegers(self.Level)]

            #   Evaulate the answer and ensure that the user has the correct answer
            elif n[0][0] == n[1][0] and answer == '=':
            
                #  Increasing the score
                self.Score += 1

                #   Notify the user about the correct answer
                self.CorrectAnswer("Correct answer")

                #   Generating new integers
                n = [self.GenerateIntegers(self.Level), self.GenerateIntegers(self.Level)]

            #   Otherwise the user has the wrong answer
            else:

                #   Decrease the self.HP by one
                self.IncorrectAnswer(f"Incorrect answer :\n")
