#   Application Entry

#   Importing responsories
import sys

#   Custom dependencies
from lib.command_line_tool import CommandlineInterface
from lib.games.integerGames import LittleProfessor, GuessTheNumber, Crocks

def main():

        help = "-h for available client commands"
        
        try :
            #   Ensure the arguments is less than two
            if len(sys.argv) < 2: 
                raise Exception(f'USEAGE: python app.py, {help}')
            
        except Exception as e: 
            sys.exit(e)

        #   Initialize an instance of CommandlineInterface
        instance = CommandlineInterface()

        if instance.CommandLineOptions().info: 
            return instance.Porgaminfo()
        
        elif instance.CommandLineOptions().tlp: 
            return LittleProfessor().run()

        elif instance.CommandLineOptions().gtn: 
            return GuessTheNumber().run()
        
        elif instance.CommandLineOptions().crocks: 
            return Crocks().run()
        
        else:
            print(f'404 : Command Not Found, {help}')

if __name__ == '__main__':
    main()