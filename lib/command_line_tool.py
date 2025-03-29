#   Importing responsories
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, ArgumentError


class CommandlineInterface():

    '''
        The command line Interface
    '''
    version = "0.0.1"
    author = "krigjo25"
    name = "GameCollection"
    description = "Collection of Integer Games"

    def CommandLineOptions(self):

        '''Constructing the argparser'''
        #   Creating a argumentParser
        parser  = ArgumentParser(prog = self.name, formatter_class= ArgumentDefaultsHelpFormatter, description= self.description, epilog= f"{self.version} - by {self.author}")

        
        #   Initializing The helper interface
        parser.add_argument('-i', '--info', dest = 'info', help = '%(prog)s info Center', action='store_true')
        parser.add_argument('-gtn', '--guessthenumber', dest = 'gtn', help ='urls to check', action='store_true')
        parser.add_argument('-tlp', '--proffessor', dest = 'tlp', help ='The mathematical game The Little Proffessor', action='store_true')
        parser.add_argument('-crc', '--crocks', dest = 'crocks', help ='Crockodile game ->', action='store_true')
        

        #   Initializing the parser
        cmd = parser.parse_args(sys.argv[1:])
        
        try :

            if not cmd:
                raise Exception("Command not found")

        except (ArgumentError, Exception) as e: 
            sys.exit(e)

        return cmd
    
    def Porgaminfo(self):
         msg = f"""
            Purpose of the program:
                Developing the skills with-in Command Line Interface using Python

            Program name : {self.name}
            Version : {self.version}
            Description : {self.description}

            Libraries used in the project :
            pytest - pytest - by pytest team
            sys - Python built-in responsories
            random - Python built-in responsories
            argparse - Python command line tool responsories\n
            Thanks for experiencing this program,
            I wish you a bug free day,
            @krigjo25"""

         return sys.exit(msg)