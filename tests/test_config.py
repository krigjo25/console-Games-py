#   Configuration tests

#   Importing Responsories
import pytest, math as m, test_setup, random as r

test_setup.pytest_environment()

from lib.config. config import GameConfig
from lib.dictionaries.game_dictionaries import GameOver, FrequentlyAskedQuestion
#   Configure the testing cases
class MockGameLogic(GameConfig):
    def __init__(self, score = 0, HP = 3, level = 1):
        super().__init__(score, HP, level)

        self.hp = HP
        self.level = level
        self.score = score

#   Testing the game configuration
class TestIGameConfig():
  
    def check_instance(self, result):

        #   Ensuring that the instance is correctly
        assert isinstance(result, list)
        assert isinstance(result[0], int)
    
    def test_generate_integers(self):

        #   Initialize an instance
        player_level = 1
        instance = MockGameLogic(level = player_level)

        #   Initialize an expected result
        result = instance.generate_integers(player_level)
    
        self.check_instance(result)

        # Calculates the expected upper bound
        expected_upper_bound = int(round(1.5 * 10 * m.sqrt(player_level)))
    
        # Ensuring that the result matches with the upperband
        assert 0 <= result[0] <= expected_upper_bound, \
        f"For default level with player level {player_level}" \
        f"output {result[0]} is out of a range 0 - {expected_upper_bound}"
  
    def test_little_professor_algorithm(self):
        pass

    def test_quit_game(self):
        #   Initialize instance
        with pytest.raises(SystemExit):

            instance = MockGameLogic(HP = 0)

            assert instance.quit_game(instance.HP)

    def test_stats(self, capsys):

        #   Randomizing player stats
        player_HP = r.randint(1, 10)
        player_level = r.randint(0, 10)
        player_score = r.randint(0, 10)
        
        #   Initializing instance
        instance = MockGameLogic(level = player_level, HP=player_HP, score=player_score)
        instance.current_stats()
        
        #   Capture print function
        captured = capsys.readouterr()
        
        expected_output = [
            f"*********** Current Stats ***********\n",
            f"HP left\t\t: {instance.HP}\n",
            f"Current Level\t: {instance.player_level}\n",
            f"Current Score\t: {instance.player_score}\n",
            f"Next level\t: {instance.compare_score - instance.player_score} points until next level\n"]
       
        #   The test
        assert captured.out == "".join(expected_output)

    def test_incorrect_answer(self, capsys):
        
        #   Initializing an instance
        instance = MockGameLogic()
        instance.incorrect_answer()

        #   n characters
        n = 57
        
        #   Capture the print functionallity
        captured = capsys.readouterr()

        #   Ensures the length is less than n
        assert len(captured.out) <= n

        #   Ensures the length is greater or equal to 16
        assert len(captured.out) >= 16

        #   Ensures that the string is a string
        assert isinstance(captured.out, str)

    def test_correct_answer(self):
        
        #   Initializing an instance
        instance = MockGameLogic()

        pass

    def test_game_level(self):

        #   Initializing an instance
        instance = MockGameLogic()
        player_score = instance.player_score

        #   Testing the printed message

        #   Testing the player_score
        assert player_score < instance.player_score

        #   Fetch the player score
        player_score = instance.compare_score
        
        #   Initialize a new instance
        instance = MockGameLogic(score = player_score)
        
        #   Fetch the player level
        player_level = instance.player_level

        #   Increase the score
        instance.game_level()

        #   Ensure the increment of the score.
        assert instance.player_level > player_level

        pass
