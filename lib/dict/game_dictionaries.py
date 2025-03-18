#   Game Over Dictionaries

#   Importing Responsories
import random as r, sys
from os import getenv
from dotenv import load_dotenv

#   Loading Environment Variables
load_dotenv()

#   Custom libraries
from lib.utils.db import SQLite
from lib.endpoints.apis import GenerateNames, NinjaAPI


class GameOver():

    '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for Emoji game
    '''
    #   arg Game Dictionaries

    def roundover(self):

        dictionary = {
                        1:f'What a humble answer !', 
                        2:f'How is 10 + 10 equal to 11 + 11?\nBecause it\'s twenty too',
                        3:f'*What does 1 plus 1 equal? a Dinner for 2',
                        4:f'Incorrect answer',}

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        string = dictionary.get(x)

        return string
    
    def Computer(self, arg):

        #   Initializing variables
        bot = 'The Computer'
        string = "Python won\n"

        if arg == '\U0001FAA8':

            dictionary = {
                            1:f'Python won\nThat moment, when you realize stone doesn\'t play along with Scissors',
                            2:f'Congratulations, this game were Rock Hard !',
                            3:f'It were crushing days for the scissors',
                            4:f'Player Says : look behind you. **running away **.',
                            5:""
}
        elif arg == '\U0001F4C4':

            dictionary = {
                            1:f'{bot} sent your stone to North-Korea !',
                            2:f'You recieved a new stone as a christmas :gift:',
                            3:f'You have been mumified by {bot}',
                            4:""
}

        else:
        
            dictionary = {
                            1:f'Noone : \"\"\n{bot} : Oh snap',
                            2:f'The paper were succsessfully cut in two by {bot} ',
                            3:f'{bot} flexed with his scissors, you lost',
                            4: ""
}

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))
        string += dictionary.get(x)

        return dictionary.get(x)

    def Player(self, arg, arg1):

        #   Initializing variables
        bot = 'Computer'
        string = "Player won\n"

        if arg == '\U0001FAA8':

            dictionary = {
                            1:f'{bot} had the idea of using a {arg1} against your {arg}, {bot} thought the {arg1} were strong enough to cut thorugh your {arg}, lets do a wii-match',
                            2:f'A thoughtful choice',
                            3:f'You just had a {arg}, while {bot} had the thought of {arg1} would be a grate choice.',
                            4:f'OH SNAP, you just scared {bot}, he never returned to the battle field.',
                            5:""
                    }

        elif arg == '\U0001F4C4':

            dictionary = {
                            1:f'{bot} threw {arg1} at you, but you grabbed it with his {arg}, and wrapped it into a 📦 \n you gave a 📦 to {bot}, how considerate of you !',
                            2:f'You wrappend {bot}\'s {arg1} into a 🎁 and sent it to the North-Pole, Santa were stoned for the Christmas ',
                            3:f'You made a mumified version of {bot}',
                            4:""
                    }

        else:
        
            dictionary = {
                            1:f'Noone : \'\'\n{bot} : Oh snap',
                            2:f'You succsessfully cut the {arg1} with a {arg}',
                            3:f'you showed of with his ✂️ which he thought were a knife, but the goal were reached, {bot} ran.',
                            4:""
                    }

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))
        string += dictionary.get(x)
        return dictionary.get(x)

    def PhilisophicalAnswer(self):

            dictionary = {
                        1:'Just allow it to be what it is, and attract the solution',
                        2:'Surrender the value to life, be integerious with the intentions. No more to do.',
                        3:'What are you really, deep down?',
                        4:'Just let it go, its not your challenge to resolve',
                        5:'Allow the challenge to be what it is, contemplate, ',
                        6:'Visualize the question, and the answer will arrive.',
                        7:'If an human is a genious, then The best answers always comes from with-in, just believe in your self enough.',
                        8:'As Socrates once said, you already know the answer of the question, as the idea of the question arised.',
                        9:'Would you be able to let it go?',
                        10:'A Question does not arise with out it\'s answer, so place your attention on where the question has arised',
                        11:'From where does the question actually arise? Your mind or heart?',
                        12:'Life is just like one of the elements on earth, just flow with it',
                        13:'Einstein said once "if the world were ending, and i had one hour to solve a problem " i would use 50 minutes to think about the issue, then use the 10 last minutes to solve the issue".',
                        14:'As the thought araises from with-in it can only be answered from with-in',
                        15:'Answers comes from with-in your self.'}

            #   Randomize the dictionary
            x = r.randrange(1,len(dictionary))

            return dictionary.get(x)

    def DumbFacts(self):

        dictionary = {
                        1:'Thoughts are like a librarynth, you will be lost',
                        2:'Dear lost boy, thoughts are like a labarynth you won\'t find the exit, when you take the wrong turn',
                        3:'When you search after an answer with why, it\'s like searching for something which doesn\'t exists.',
                        4:'life is why',
                        5:'Things tends to be what it is, neither less or more, but equal to what it is.',
                        6:'The opposite sides of a die will always add up to seven.',
                        7:'The King of Hearts is the only king in a deck of cards without a mustache.',
                        8:'There is always an answer with-in, just compenplate on it',
                        9:'Alaska is the only state whose name is on one row on a keyboard.',
                        10:'A "jiffy" is about one trillionth of a second.',
                        11:'The ocean is blue',
                        12:'Mulan has the highest kill-count of any Disney character.',
                        13:'The infinity sign is called a lemniscate.',
                        14:'why do you ask me?. ',
                        15:"..."

}

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        return dictionary.get(x)

    def RandomCorrectAnswer(): pass
    def RandomIncorrectAnswer(): pass
    def RandomTowaTieAnswer(): pass

class ScrabbleGame():

    """ 
        Calculates scores in the game

    """

    def ComputeScore(self, word):

        #   Initializing variables
        result = 0

        #   Initializing arrays
        alpha = [   'a', 'b', 'c', 'd',
                    'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x',
                    'y', 'z']

        POINTS = [  1, 3, 3, 2,
                    1, 4, 2, 4, 
                    1, 8, 5, 1,
                    3, 1, 1, 3,
                    10, 1, 1, 1,
                    1, 4, 4, 8,
                    4, 10]

        for i in str(word).lower(): 
            for j in alpha:

                if i == j:
                    result += POINTS[alpha.index(i)]

        #   Clear memories
        del alpha, POINTS, word

        return result

class FrequentlyAskedQuestion():

        def WordGames(self, arg):
    
            if str(arg).lower() == 'jumble':
                return sys.exit(
                                """ 
                                    Frequently Asked Questions : Jumble
                                    USEAGE : python wordgames.py -j\n
                                    1.\n
                                    USEAGE : ctrl + c to exit the game
                                """)

            elif str(arg).lower() == 'eightball':
                return sys.exit(""" 
                    Frequently Asked Questions : Eightball
                    USEAGE : python wordgames.py -e\n
                    1. Type in a sentence and the eightball will reply\n
                    USEAGE : ctrl + c to exit the game
                """)

            elif str(arg).lower() == 'scrabble':
                return sys.exit(""" 
                                    Frequently Asked Questions : Scrabble
                                    USEAGE : python wordgames.py -s\n
                                    1. Type in how many human will play (int)
                                    2.  Type in how many bots will play (int)
                                    3. Select name for the human players (alpha)
                                    4. Every participants types in a word (alpha)
                                    5. wait for the program to calculate the result\n
                                    USEAGE : ctrl + c to exit the game
                                    """)

            elif str(arg).lower() == 'rsp':
                return sys.exit(""" 
                                    Frequently Asked Questions : Rock Scissor'n Paper
                                    USEAGE : python wordgames.py -rsp\n
                                    1. Select name for the human players
                                    2. Type in a word (rock, scissor or paper)
                                    5. wait for the program to calculate the result\n
                                    USEAGE : ctrl + c to exit the game
                                    """)
    
            else : return sys.exit('List of available games :\nJumble\nRock Scissors\'n Paper (n)\nScrabble\nEightball\nEnd Of List\n')
