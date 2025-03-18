#   Importing responsories
import sys
from lib.command_line_tool import CommandlineInterface
from lib.games.integerGames import LittleProfessor, GuessTheNumber, Crocks

def main():

        #   Ensure the arguments is less than two
        try :
            if len(sys.argv) < 2: 
                raise Exception('Usage: python intgame.py -h to view the commands')
        except Exception as e: 
            sys.exit(e)

        cmd = CommandlineInterface()
            
        if cmd.CommandLineOptions().info: 
            return cmd.Porgaminfo()
        
        elif cmd.CommandLineOptions().tlp: 
            return LittleProfessor().run()

        elif cmd.CommandLineOptions().gtn: 
            return GuessTheNumber().run()
        
        elif cmd.CommandLineOptions().crocks: 
            return Crocks().run()

if __name__ == '__main__':
    main()