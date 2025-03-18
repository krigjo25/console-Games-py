import time as t
from typing import Optional

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
        