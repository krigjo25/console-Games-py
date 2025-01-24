
#   Importing Responsories
import random as r

class GameOver():

    def roundover(self, n, answer):

        array = ['<', '>', '=']

        if answer == n:

            dictionary = {
                            1:f'What a humble answer !', 
                            2:f'{answer} is equal to {n}',
                            3:f'How is 10 + 10 equal to 11 + 11?\nBecause it\'s twenty too',
                            4:f'*What does 1 plus 1 equal? a Dinner for 2', 5:""}

        elif answer != n:

            dictionary = {
                            1:f'{answer} is not equal to {n}',
                            2:f'{answer} is not equal to {n}',
                            3:f'{answer} is not equal to {n}',
                            4:f'{answer} is not equal to {n}',
                            5:f'{answer} is not equal to {n}'}

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        string = dictionary.get(x)

        return string