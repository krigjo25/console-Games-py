#   Importing Responsories
import sys, math as m, random as r

#   Importing Customized repository
from lib.dict.game_over import GameOver
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

        #   Ensure the score is greater than the compare score
        if (self.Score > self.CompareScore):
            
            #   Notify the user about the new level
            print(f"[ ! ] Congratulation a new level has been unlocked [ ! ]")
            print("[ ! ] Health Points increased by 1 ! [ ! ]")

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


            return

        #   Increase the score
        self.Score += 1

        #   Notify the user about the score
        print("[ ! ] Score increased by 1 [ ! ]")

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

        #   Returning the values
        return arg

    def IncorrectAnswer(self, e:str):
        self.HP -= 1
        self.CurrentStats()

        print(f"{e}")

    def CurrentStats(self):
        arterise = "*" * 11

        print()
        print(f"{arterise} Current Stats {arterise}")
        
        print(f"HP left\t\t: {self.HP}")
        print(f"Current Level\t: {self.Level}")
        print(f"Current level\t: {self.Level}")
        print(f"Current score\t: {self.Score}")
        print(f"Compare Score\t: {self.Score}/{self.CompareScore} untill next level")
        print()
    
    def QuitGame(self, n:int, answer:str = ""):
        """
            #   Quitting the game
        """
        if self.HP == 0:
            self.CurrentStats()
            return sys.exit(f"{GameOver().roundover(n,answer)}\n")
    
    def CorrectAnswer(self, arg):
        
        print(f"{arg}")

        #   Increasing the score / level
        self.GameLevel()

        