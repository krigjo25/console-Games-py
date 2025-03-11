#   Application's Configuration's file
#   Importing Responsories
import sys, math as m, random as r
from typing import Optional

#   Importing Customized repository
from intgames.lib.debug.logger import ConfigurationWatcher
from lib.dict.game_over import GameOver
from lib.utils.tools import ConsoleTools

logger = ConfigurationWatcher()
logger = logger.FileHandler()

class GameConfig():

    """
        #   Game Configuration
        #   This class contains the configuration of the game
        #   The game has the following attributes:
        #   - Level,            Score
        #   - Health Points,    Compare
        #   - Total Score

    """
    
    def __init__(self, level:int = 1, score:int = 0, HP:int = 0, compare:int = 0):

        self.HP = HP
        self.level = level
        self.score = score
        self.logger = logger
        self.console = ConsoleTools()
        
        self.CompareScore = int(round(1.5 * 10 * m.sqrt(self.Level))) if int(round(1.5 * 10 * m.sqrt(self.Level))) > 0 else int(round(1.5 * 10 * m.sqrt(self.Level+1)))
    
    #  Game Properties
    @property
    def Level(self): return self.level
    
    @property
    def Score(self): return self.score
    
    @property
    def HealthPoints(self): return self.HP

    @property
    def Compare(self): return self.CompareScore
    
    
    #   Property setters
    @Level.setter
    def Level(self, level):
        if self.Score >= self.CompareScore:

            self.level = level
    
    @Score.setter
    def Score(self, score):
        self.score = score
    
    @HealthPoints.setter
    def HealthPoints(self, HP):
        self.HP = HP

    @Compare.setter
    def Compare(self, compare):
        self.CompareScore = compare

    def GameLevel(self):

        '''
            #   Increasing the game level of the game
            #   The level has to be greater than 1
        '''

        messages = []
        
        
        #   Ensure the score is greater than the compare score
        if (self.Score > self.CompareScore):

            #   Append the messages
            messages.append("[ ! ] Congratulation a new level has been unlocked [ ! ]")
            messages.append("[ ! ] Health Points increased by 1 ! [ ! ]")

            #   Notify the user about the new level
            self.console.print(messages)

            #   Reset the score
            self.Score = 0

            #   Increase the level
            self.Level += 1

            #   Increase the Health Points
            self.HP += 1 

            #   Increase the compare score
            self.CompareScore = int(round(1.5 * 10 * m.sqrt(self.Level)))

            #   Display the current stats
            self.CurrentStats()

        else:

            #   Append the message
            messages.append("[ ! ] Score increased by 1 [ ! ]")

            #   Increase the score
            self.Score += 1

            #   Notify the user about the score
            self.console.print(messages)

        #   Log the events
        self.logger.info(f"{self.__class__.__name__}: GameLevel : \t lvl : {self.Level} Current Score: {self.Score } / {self.CompareScore}")

    def GenerateIntegers(self, lvl:int):

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

    def TLPAlgorithm(self, lvl:int):

        """
            #   Generating the game Algorithm for the game which is level based
        """
        #   Generating integers
        x = self.GenerateIntegers(lvl)
        y = self.GenerateIntegers(lvl)

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

    def IncorrectAnswer(self, e:str):
        
        """
            When the user inputs an incorrect answer

                #   Decreasing the health points
                #   Displaying the current Stats
        """
        old_hp = self.HP
        self.HP -= 1

        #   Log the events
        self.logger.info(f"{self.__class__.__name__}: GameLevel : \t HP : {self.HP} - {old_hp}")


        self.console.print(f"{e}")


    def CurrentStats(self):
        arterise = "*" * 11

        stats = [
            f"{arterise} Current Stats {arterise}",
            f"HP left\t\t: {self.HP}",
            f"Current Level\t: {self.Level}",
            f"Current level\t: {self.Level}",
            f"Current score\t: {self.Score}",
            f"Compare Score\t: {self.Score}/{self.CompareScore} untill next level"

        ]
        self.console.print(stats)
    
    def QuitGame(self, n:int, answer:Optional[str]):
        """
            #   Quitting the game
        """
        if self.HP == 0:
            self.CurrentStats()

        self.logger.info(f"{self.__class__.__name__}: QuitGame : \t HP: {self.HP} Current Score: {self.Score } / {self.CompareScore}")
        return sys.exit(f"{GameOver().roundover(n,answer)}\n")
    
    def CorrectAnswer(self, arg):
        
        self.console.print(arg)

        #   Increasing the score / level
        self.GameLevel()

        