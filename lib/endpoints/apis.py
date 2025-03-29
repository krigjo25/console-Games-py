# APIS Integrated in this application

# Python Repositories
import os, sys, random as r, requests as req

from dotenv import load_dotenv

#   Loading Environment Variables
load_dotenv()

class APIService():

    #   API-Ninja
    def check_word(self, word):

        """
            #   API by API-Ninja
            # Using an api to check if the word exist in the online dictionary.
        """
        parse = f'{os.getenv('Ninja-WORD')+ str(word)}'
        response = req.get(parse, headers={'X-Api-Key': os.getenv('Ninja-KEY')})
        json = response.json()
        
        try:

            if response.status_code != req.codes.ok:
                raise Exception(f"Something went wrong with the connection to Ninja API: {response.status_code}")

        except Exception as e : return sys.exit(e)

        return bool(json['valid'])

    def generate_random_word(self):

        '''
            #   API by API-Ninja
            #   API to choose a randomly generated word
        '''
        response = req.get(os.getenv('Ninja-RANDOM'), headers={"X-Api-Key": os.getenv('Ninja-KEY')})
        json = response.json()

        try:

            if response.status_code != req.codes.ok: raise Exception(f"Something went wrong with the connection to Ninja API: {response.status_code}")
        except Exception as e : return sys.exit(e)

        #   Clear some space
        del parse, response

        return json['word'][0]

    def word_definition(self, word):

        """
            #   API by API-Ninja
            # Using an api to check wether the word exist or not.
        """

        response = req.get(os.getenv('Ninja-API-WORD') + word, headers={'X-Api-Key': os.getenv("Ninja-API-Key")})
        json = response.json()

        try:
            if response.status_code != req.codes.ok: raise Exception(response.status_code)

        except Exception as e: return e

        for i, j in dict(json).items(): 
            if "valid" in i :  
                return True
        
        return False

    def generate_random_names(self, total):
        """
            Generates only firstnames
            API by RandomUserGenerator.me
        """

        #   Send a request to the API
        response = req.get(os.getenv('RANDOM-USER') + total)
        json = response.json()

        try:
            if response.status_code != req.codes.ok:
                raise Exception(response.status_code)

        except Exception as e: 
            return sys.exit(e)

        for i in json['results']:
            return i['name']['first']

