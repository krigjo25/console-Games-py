#   Configuration tests

#   Importing Responsories
import pytest, math as m, test_setup, random as r

test_setup.pytest_environment()

from lib.config.config import GameConfig

#   Configure the testing cases
class MockLogic(GameConfig):
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
        instance = MockLogic(level = player_level)

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

            instance = MockLogic(HP = 0)

            assert instance.quit_game(instance.HP)

    def test_stats(self, capsys):

        #   Randomizing player stats
        player_HP = r.randint(1, 10)
        player_level = r.randint(0, 10)
        player_score = r.randint(0, 10)
        
        #   Initializing instance
        instance = MockLogic(level = player_level, HP=player_HP, score=player_score)
        instance.current_stats()
        
        #   Capture print function
        captured = capsys.readouterr()
        
        expected_output = [
            f"*********** Current Stats ***********\n",
            f"HP\t\t: {instance.HP} [ 💝 ]\n",
            f"Level\t: {instance.player_level} [ 🏅 ]\n",
            f"Score\t: {instance.player_score} [ ⭐ ]\n",
            f"{instance.compare_score - instance.player_score} points to next level [ 🎯 ]\n"
        ]
        #   Testing without any arguments
        assert captured.out == "".join(expected_output)

        instance.current_stats(arg = "[ ⬆️ ] Congratulation a new level has been unlocked [ ⬆️ ]")
        
        expected_output[0] = f"[ ⬆️ ] Congratulation a new level has been unlocked [ ⬆️ ]\n"
        
        #   Capture print function
        captured = capsys.readouterr()

        #   Testing with arguments
        assert captured.out == "".join(expected_output)


    def test_incorrect_answer(self, capsys):
        
        #   Initializing an instance
        instance = MockLogic()
        player_health = instance.HP

        instance.incorrect_answer()

        #   n characters
        max = 30
        min = 15
        
        #   Capture the print functionallity
        captured = capsys.readouterr()

        #   Ensures the length is less than n
        assert len(captured.out) <= max

        #   Ensures the length is greater or equal to 16
        assert len(captured.out) >= min

        #   Ensures that the string is a string
        assert isinstance(captured.out, str)

        #   Ensures that the health point has decresed
        assert instance.HP < player_health

    def test_game_level(self, capsys):

        #   Initializing an instance
        instance = MockLogic()
        player_score = instance.compare_score
        player_level = instance.player_level

        instance = MockLogic(score=player_score)
        instance.game_level()

        player_compare_score = int(round(1.5 * 10 * m.sqrt(instance.player_level)))
        
        #   Testing the Score and level
        assert instance.score == 0
        assert player_compare_score == instance.compare_score
        assert player_level < instance.player_level and instance.player_level == player_level + 1