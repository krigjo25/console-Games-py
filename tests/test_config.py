#   Importing Responsories
import pytest, math as m

#   Importing local libraries
from lib.config.config import GameConfig

#   Configure the testing cases
class MockGameLogic(GameConfig):
  def __init__(self, score = 0, HP = 3, level = 1):
     super().__init__(score, HP, level)

     self.level = level
     self.score = score
     self.hp = HP

#   Testing the game level function
class TestIntegerGeneration():
  
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
     
    #   Initialize an instance
    player_level = 1
    instance = MockGameLogic(level = player_level)

    result = instance.the_little_professor_algorithm(player_level)
    self.check_instance(result)
    #   Calculate the expected upper bound
    #expected_upper_bound = int(round)

  def test_crocks_game(self):
     pass
