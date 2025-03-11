import time as t
class ConsoleTools(object):

    def print(arg: list, ms:float):
        """
        Prints the arguments in the list with a delay of ms

        #   The function takes in two parameters
        #   :arg: list
        #   :ms: float
        
        """

        for i in arg:

            print(i)
            t.sleep(ms)