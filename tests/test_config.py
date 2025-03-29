#   Configuration tests

#   Importing Responsories
import pytest, math as m, test_setup, random as r

test_setup.pytest_environment()

from lib.config. config import GameConfig

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

    def test_incorrect_answer(self):
        pass

    def test_correct_answer(self):
        pass

    def test_game_level(self):
        pass
