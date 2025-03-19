#   Utils tools for the games

#   Importing Repositories
import random as r, time as t

from typing import Optional


class ScrabbleUtils():

    """ 
        Calculates scores in the game

    """

    def compute_score(self, word):

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

class TheLittleProffessorUtils():

    def mathOperation(self):
        
        dictionary = {
            0:'+',
            1:'-',
            2:'/',
            3:'*',
            4:'//'}
        
        r.shuffle(dictionary)

        return r.randint(0, len(dictionary)-1)

class EightBallUtils():

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

class ConsoleUtils():

    def type_effect(arg:list, ms:Optional[float] = 700):
        """
        Prints the arguments in the list with a delay of ms

        #   The function takes in two parameters
        #   :arg: string is a required parameter
        #   :ms: float is an optional parameter"""
        for i in range(len(arg)):

            print(arg[i], end="")
            t.sleep(ms)
        