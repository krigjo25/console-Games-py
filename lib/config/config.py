#   Application's Configuration's file

#   Importing Responsories
import sys, math as m, random as r, regex as re

from typing import Optional

#   Importing Customized repository
from lib.dictionaries.game_dictionaries import GameOver
from lib.debug.logger import ConfigurationWatcher
from lib.utils.game_utils import TheLittleProffessorUtils, ConsoleUtils

#   Initializing the logger
logger = ConfigurationWatcher()
logger.file_handler()

class GameConfig():

    """
        #   Game Configuration
        #   This class contains the configuration of the game
        #   The game has the following attributes:
        #   - Level,            Score
        #   - Health Points,    Compare
        #   - Total Score

    """
    
    def __init__(self, score:Optional[int]  = 0, HP:Optional[int] = 3, level:Optional[int] = 1):

        self.HP = HP
        self.level = level
        self.score = score
        self.logger = logger
        self.console = ConsoleUtils()
        
        self.compare_score = int(round(1.5 * 10 * m.sqrt(self.player_level))) if int(round(1.5 * 10 * m.sqrt(self.player_level))) > 0 else int(round(1.5 * 10 * m.sqrt(self.player_level+1)))
    
    #  Game Properties
    @property
    def player_level(self): return self.level
    
    @property
    def player_score(self): return self.score
    
    @property
    def player_hp(self): return self.HP

    @property
    def computer_comparison(self): return self.compare_score
    
    
    #   Property setters
    @player_level.setter
    def player_level(self, level):
        if self.player_score >= self.compare_score:

            self.level = level
    
    @player_score.setter
    def player_score(self, score):
        try:
            if not str(score).isalnum():
                raise Exception("Score can not be a string")
        except Exception as e:
            sys.exit(e)
        
        self.score = score
        
    @player_hp.setter
    def player_hp(self, HP):
        if HP > 0:
            self.HP = HP

    @computer_comparison.setter
    def computer_comparison(self, compare):
        self.compare_score = compare

    def game_level(self):

        '''
            #   Increasing the game level of the game
            #   The level has to be greater than 1
        '''

        messages = []
        
        #   Ensure the score is greater than the compare score
        if (self.score >= self.compare_score):

            #   Reset the score
            self.score = 0

            #   Increase the level
            self.level += 1

            #   Increase the Health Points
            self.HP += 1 

            #   Increase the compare score
            self.compare_score = int(round(1.5 * 10 * m.sqrt(self.player_level)))

            #   Display the current stats
            self.current_stats(arg = "[ ⬆️ ] Congratulation a new level has been unlocked [ ⬆️ ]")

        else:

            #   Append the message
            messages.append("[ ⭐ ] Score increased by 1 [ ⭐ ]")

            #   Increase the score
            self.score += 1
        
        for i in range(len(messages)):
            print(messages[i])

    def generate_integers(self, lvl:int):

        """
            #   Basic algorithm for generating random integers
            #   The integers are generated based on the level of the game
            #   The level of the game is passed as an argument

            param: lvl : int : The level of the game
            return: list : The list contains the generated integer and a string
        """

        #   Algorithm to increase the difficulty
        n = r.randint(0, int(round(1.5 * 10 * m.sqrt(self.player_level))))

        return n

    def the_little_professor_algorithm(self, lvl:int):

        """
            #   Generating the game Algorithm for the game which is level based
        """

        #   Initialize an instance
        instance = TheLittleProffessorUtils()

        #   Generating integers
        x = self.generate_integers(lvl)
        y = self.generate_integers(lvl)

        #   Generating the math operator ( Chance based )
        operator = instance.mathOperation()

        arg = []

        self.logger.info(f"{self.__class__.__name__}: TLPAlgorithm : \t Returned argument : {x} {operator} {y}")


        #   Matching Mathematic operator
        match operator:

            case '-':
                arg.append(abs(x - y))

            case '*':
                arg.append(abs(x * y))

            case '/':
                arg.append(abs(x / y))
            
            case '//':
                arg.append(abs(x // y))

            case '%':
                arg.append(abs(x % y))

            case _:
                arg.append(abs(x + y))
            
        arg.append(f"{x} {operator} {y}=")

        return arg

    def current_stats(self, arg:Optional[tuple] = None):
        arterise = "*" * 11
        if not arg:

            stats = [
                f"{arterise} Current Stats {arterise}",
                f"HP\t\t: {self.HP} [ 💝 ]",
                f"Level\t: {self.player_level} [ 🏅 ]",
                f"Score\t: {self.player_score} [ ⭐ ]",
                f"{self.compare_score - self.player_score} points to next level [ 🎯 ]"
            ]
        else:
            stats = [
                f"{arg}",
                f"HP\t\t: {self.HP} [ 💝 ]",
                f"Level\t: {self.player_level} [ 🏅 ]",
                f"Score\t: {self.player_score} [ ⭐ ]",
                f"{self.compare_score - self.player_score} points to next level [ 🎯 ]"
            ]
        
        stats = tuple(stats)

        #   Notify the user about the stats and given arg
        for i in range(len(stats)):
            print(stats[i])

    def quit_game(self, n:int):
        """
            #   Quitting the game
        """
        if self.HP == 0:
            self.current_stats()
            return sys.exit(f"{GameOver().game_over}\n")

    def incorrect_answer(self, arg:Optional[str] = None):
        
        """
            When the user inputs an incorrect answer

                #   Decreasing the health points
                #   Displaying the current Stats
        """
        old_hp = self.HP
        self.HP -= 1

        #   Log the events
        self.logger.info(f"{self.__class__.__name__}: GameLevel : \t HP : {self.HP} - {old_hp}")

        if not arg:
            arg = GameOver().roundover_incorrect()

        print(arg)

    def correct_answer(self, arg):
        
        if not arg:
            arg = GameOver().roundover_victorious()

        print(arg)

        #   Increasing the score / level
        self.game_level()

        