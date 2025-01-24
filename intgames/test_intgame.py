#   Importing Responsories
import pytest

#   Importing local libraries
from pylib.gamecollection import IntegerGames as ig

# Configure the testing cases
class TestConfigurations():
  pass

# Testing the game level function
class TestGameLevel(TestConfigurations):

  # Testing the game level
  def test_gamelvl(self):
    
    # Conduct a integer test
    assert ig.GameLevel(ig , 1) == 1
    assert ig.GameLevel(ig , 2) == 2
    assert ig.GameLevel(ig , 3) == 3
    assert ig.GameLevel(ig , 4) == 4
    assert ig.GameLevel(ig , 5) == 5

    return print("\n\nFinished assertion testing")

  def test_exceptions(self):

    #   Initialize a test for exceptions
    with pytest.raises(SystemExit) as e:

      assert ig.GameLevel(ig, 0) == str(e.value)
      assert ig.GameLevel(ig, -1) == str(e.value)

    return print("\nException test finished")