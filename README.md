# Lab: 06 : Game of Greed 1


# Description

A Python application using Object Oriented Programming.

# Requirements

python 3.9.7
black
flake
pytest

# Feature Tasks

[x] Define a GameLogic class in game_of_greed/game_logic.py file.
[x] Handle calculating score for dice roll
[x] Add calculate_score static method to GameLogic class.
[x] The input to calculate_score is a tuple of integers that represent a dice roll.
[x] The output from calculate_score is an integer representing the roll’s score according to rules of game.
[x] Add roll_dice static method to GameLogic class.
[x] The input to roll_dice is an integer between 1 and 6.
[x] The output of roll_dice is a tuple with random values between 1 and 6.
[x] The length of tuple must match the argument given to roll_dice method.
[x] Define a Banker class
[x] Add a shelf instance method
[x] Input to shelf is the amount of points (integer) to add to shelf.
[x] shelf should temporarily store unbanked points.
[x] Add a bank instance method
[x] bank should add any points on the shelf to total and reset shelf to 0.
[x] bank output should be the amount of points added to [x] total from shelf.
[x] Add a clear_shelf instance method
[x] clear_shelf should remove all unbanked points.

# Get Started

```python
poetry install
poetry shell
pytest
```

# Developer

Faisal Kushha
Mohammad Silwadi        
Ehab Ahmad
Suzan Hiary


##  [Pull Request Link](https://github.com/game-of-greed-group5/game-of-greed/pull/1)

