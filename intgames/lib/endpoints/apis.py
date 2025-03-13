# APIS Integrated in this application

# Python Repositories
import os, sys, random as r, requests as req

from dotenv import load_dotenv

#   Loading Environment Variables
load_dotenv()

class NinjaAPI():

    #   API-Ninja
    def Check(self, word):

        """
            #   API by API-Ninja
            # Using an api to check if the word exist in the online dictionary.
        """
        parse = f'https://api.api-ninjas.com/v1/dictionary?word={str(word)}'
        response = req.get(parse, headers={'X-Api-Key': os.getenv("Ninja-API-Key")})
        json = response.json()
        
        try:

            if response.status_code != req.codes.ok:
                raise Exception(f"Something went wrong with the connection to Ninja API: {response.status_code}")

        except Exception as e : return sys.exit(e)

        #   Clear some space
        del word, parse, response

        return bool(json['valid'])

    def Choice(self):

        '''
            #   API by API-Ninja
            #   API to choose a randomly generated word
        '''

        parse = 'https://api.api-ninjas.com/v1/randomword'
        response = req.get(parse, headers={'X-Api-Key': os.getenv("Ninja-API-Key")})
        json = response.json()

        try:

            if response.status_code != req.codes.ok: raise Exception(f"Something went wrong with the connection to Ninja API: {response.status_code}")
        except Exception as e : return sys.exit(e)

        #   Clear some space
        del parse, response

        return json['word'][0]

    def Definition(self, word):

        """
            #   API by API-Ninja
            # Using an api to check wether the word exist or not.
        """

        parse = f'https://api.api-ninjas.com/v1/dictionary?word={word}'
        response = req.get(parse, headers={'X-Api-Key': os.getenv("Ninja-API-Key")})
        json = response.json()

        try:
            if response.status_code != req.codes.ok: raise Exception(response.status_code)

        except Exception as e: return e
        
        #   Clear some memory
        del word, parse, response

        for i, j in dict(json).items(): 
            if "valid" in i :  
                return True
        
        return False

class GenerateNames():
        def GenerateRandomNames(self, total):

            """
                Generates only firstnames
                API by RandomUserGenerator.me
            """

            parse = f'https://randomuser.me/api/?results={total}'
            response = req.get(parse)
            json = response.json()

            try:
                if response.status_code != req.codes.ok:
                    raise Exception(response.status_code)

            except Exception as e: 
                return sys.exit(e)

            #   Clear memories
            del parse, response

            for i in json['results']:
                return i['name']['first']
