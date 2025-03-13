
#   Importing Responsories
import random as r

class GameOver():

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