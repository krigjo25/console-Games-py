#   Importing Responsories
import pytest

#   Importing local libraries
from lib.config.config import GameConfig

# Configure the testing cases
class TestConfigurations():
  pass

# Testing the game level function
class TestGameLevel(TestConfigurations):

  # Testing the game level
  def test_gamelvl(self):
    
    ig = GameConfig
    ig.player_hp = 3
    ig.player_score = 12


    # Conduct a integer test
    assert ig.player_hp  == 3
    assert ig.player_score == 12
  
    return