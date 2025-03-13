#   Application's Configuration's file
#   Importing Responsories
import sys, math as m, random as r
from typing import Optional

#   Importing Customized repository
from lib.dict.game_over import GameOver
from lib.utils.tools import ConsoleUtils
from lib.debug.logger import ConfigurationWatcher

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
    
    def __init__(self, score:int  = 0, HP:int = 3, level:Optional[int] = 1):

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
        self.score = score
    
    @player_hp.setter
    def player_hp(self, HP):
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
        if (self.player_score >= self.compare_score):

            #   Append the messages
            messages.append("[ ! ] Congratulation a new level has been unlocked [ ! ]")
            messages.append("[ ! ] Health Points increased by 1 ! [ ! ]")



            #   Reset the score
            self.player_score = 0

            #   Increase the level
            self.player_level += 1

            #   Increase the Health Points
            self.HP += 1 

            #   Increase the compare score
            self.compare_score = int(round(1.5 * 10 * m.sqrt(self.player_level)))

            #   Display the current stats
            self.current_stats()

        else:

            #   Append the message
            messages.append("[ ! ] Score increased by 1 [ ! ]")

            #   Increase the score
            self.player_score += 1


    def generate_integers(self, lvl:int):

        """
            #   Basic algorithm for generating random integers
            #   The integers are generated based on the level of the game
            #   The level of the game is passed as an argument

            param: lvl : int : The level of the game
            return: list : The list contains the generated integer and a string
        """
        match lvl:

            case 1: 
                return [r.randint(0, 10), 'Guess a number between (1-10) :']

            case 2: 
                return [r.randint(0, 20), 'Guess a number between (1-20) :']

            case 3: 
                return [r.randint(0, 30), 'Guess a number between (1-30) :']

            case 4: 
                return [r.randint(0, 40), 'Guess a number between (1-40) :']

            case 5: 
                return [r.randint(0, 50), 'Guess a number between (1-50) :']

            case 6: 
                return [r.randint(0, 60), 'Guess a number between (1-60) :']
            
            case 7: 
                return [r.randint(0, 70), 'Guess a number between (1-70) :']
            
            case 8: 
                return [r.randint(0, 80), 'Guess a number between (1-80) :']
            
            case 9: 
                return [r.randint(0, 90), 'Guess a number between (1-90) :']
            
            case 10: 
                return [r.randint(0, 100), 'Guess a number between (1-100) :']
            
            case _:
                return [r.randint(0, 500), 'Guess a number between (1-500) :']

    def the_little_professor_algorithm(self, lvl:int):

        """
            #   Generating the game Algorithm for the game which is level based
        """
        #   Generating integers
        x = self.generate_integers(lvl)
        y = self.generate_integers(lvl)

        match lvl:

            case 5:
                n = abs(x[0] - y[0])
                txt = f"{x[0]} - {y[0]}="
            
            case 6:
                n = abs(x[0] * y[0])
                txt = f"{x[0]} * {y[0]}="

            case _:
                n = abs(x[0] + y[0])
                txt = f"{x[0]} + {y[0]}="

        #   Initializing a list
        arg = []

        arg.append(n)
        arg.append(txt)

        #   Log the events
        self.logger.info(f"{self.__class__.__name__}: TLPAlgorithm : \t Returned argument : {arg}")

        return arg

    def current_stats(self, arg:tuple = None):
        arterise = "*" * 11

        stats = [
            f"{arterise} Current Stats {arterise}",
            f"HP left\t\t: {self.HP}",
            f"Current Level\t: {self.player_level}",
            f"Current level\t: {self.player_level}",
            f"Current score\t: {self.player_score}",
            f"Compare Score\t: {self.player_score}/{self.compare_score} untill next level"
        ]
        
        if arg:
            for i in arg:
                stats.append(i)
        
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
            return sys.exit(f"{GameOver().roundover()}\n")

    def incorrect_answer(self):
        
        """
            When the user inputs an incorrect answer

                #   Decreasing the health points
                #   Displaying the current Stats
        """
        old_hp = self.HP
        self.HP -= 1

        #   Log the events
        self.logger.info(f"{self.__class__.__name__}: GameLevel : \t HP : {self.HP} - {old_hp}")

        print(GameOver().roundover())

    def correct_answer(self, arg):
        
        for i in range(len(arg)):
            print(arg[i])

        #   Increasing the score / level
        self.game_level()

        