#   Game Collection

#   Importing Responsories
import time as t, random as r

#   Importing Customized repository
from lib.config.config import GameConfig
from lib.debug.logger import GameWatcher

#   Initializing the Logger
logger = GameWatcher()
logger.file_handler()

# Refactoring the code
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

        self.HP = 3
        n = [self.generate_integers(self.player_level), self.generate_integers(self.player_level)]

        while True:

            self.quit_game(n, answer)

            answer = str(input(f'Is {n[0][0]} >=< {n[1][0]}? :\t'))

            #   Ensure that the user does not input any characters which are not allowed
            try :

                #   Ensure that the user has inputted the correct answer
                if answer not in ['>', '<', '=']:
                    raise ValueError('Invalid input')

            except (ValueError, TypeError, Exception) as e: 

                self.incorrect_answer(e)
                
            if n[0][0] > n[1][0] and answer == '>':

                self.correct_answer(f"Correct answer")

                #   Generating new integers
                n = [self.generate_integers(self.player_level), self.generate_integers(self.player_level)]

            #   Evaulate the answer and ensure that the user has the correct answer
            elif n[0][0] < n[1][0] and answer == '<':
            
                self.correct_answer()
                n = [self.generate_integers(self.player_level), self.generate_integers(self.player_level)]

            #   Evaulate the answer and ensure that the user has the correct answer
            elif n[0][0] == n[1][0] and answer == '=':

                self.correct_answer("Correct answer")
                n = [self.generate_integers(self.player_level), self.generate_integers(self.player_level)]

            #   Otherwise the user has the wrong answer
            else:
                self.incorrect_answer(f"Incorrect answer :\n")

class GuessTheNumber(GameConfig):
    """
        Guess The Number Game

        The user has to guess the number that the computer has generated.
        The user has to guess the number within the range of 1- x.
        if the user's health points are zero, the game will end.

    """
    def __init__(self):
        super().__init__()
        self.logger = logger
        self.logger.warn(f"{self.__class__.__name__} has been initialized")

    def run(self):

        self.player_hp = 9
        start = t.perf_counter()
        n = self.generate_integers(self.level)

        while True:

            self.quit_game(self.HP)
            self.logger.info(f"{self.__class__.__name__} Generated number : {n[0]} Text : {n[1]}")
            answer = input(f'{n[1]}')

            try :

                #   Ensure that the user has inputted a number
                if not answer.isnumeric(): 
                    raise ValueError("Input is not a number")

            except (ValueError, TypeError, Exception) as e: 
                
                #   Decrease the self.HP by one and notify the user about the incorrect answer
                self.incorrect_answer(e)

            else:

                #   Assign an integer
                answer = int(answer)

                if answer == n[0]: 
                        
                        #   Notify the user about the correct answer
                        arg = ["Correct answer"]
                        self.correct_answer(arg)

                        #   Generating new integers
                        n = self.generate_integers(self.level)
        
                else:

                    #   Notify the user about the incorrect answer and decrease the self.HP by one
                    self.incorrect_answer('Too low, guess higher') if n[0] > int(answer) else self.incorrect_answer('Too high, guess lower')

            self.logger.info(f"{self.__class__.__name__} Level : {self.level} Score : {self.score} / {self.compare_score}Time : {t.perf_counter() - start} seconds ")

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

            n = self.the_little_professor_algorithm(self.player_level)

            self.quit_game(n[0], answer)

            answer = input(f'{n[1]} = :')

            try :

                #   Ensure the variable contains an integer
                if not answer.isnumeric(): 
                    raise ValueError("The input is not a number")

            except (ValueError, Exception) as e:

                self.incorrect_answer(e)

            self.correct_answer(f"Correct answer") if int(answer) == n[0] else self.incorrect_answer(f"EEE")

            #   Breaking out of the loop
            if self.player_level == 10:
                return print(f"Score : {self.player_score}\nLevels completed : {self.player_level}")
