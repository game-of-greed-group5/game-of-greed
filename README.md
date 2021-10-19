# Game of Greed

# Description

A Python application using Object Oriented Programming to create a rolling dice game.

# Requirements

python 3.9.7
black
flake
pytest

# Feature Tasks

Lab06:-

[x] Define a GameLogic class in game_of_greed/game_logic.py file.

[x] Handle calculating score for dice roll.

[x] Add calculate_score static method to GameLogic class.

[x] The input to calculate_score is a tuple of integers that represent a dice roll.

[x] The output from calculate_score is an integer representing the roll’s score according to rules of game.

[x] Add roll_dice static method to GameLogic class.

[x] The input to roll_dice is an integer between 1 and 6.

[x] The output of roll_dice is a tuple with random values between 1 and 6.

[x] The length of tuple must match the argument given to roll_dice method.

[x] Define a Banker class.

[x] Add a shelf instance method.

[x] Input to shelf is the amount of points (integer) to add to shelf.

[x] shelf should temporarily store unbanked points.

[x] Add a bank instance method.

[x] bank should add any points on the shelf to total and reset shelf to 0.

[x] bank output should be the amount of points added to [x] total from shelf.

[x] Add a clear_shelf instance method.

[x] clear_shelf should remove all unbanked points.

lab07:-

[x] Application should implement all features from previous version

[x] Application should simulate rolling between 1 and 6 dice

[x] Application should allow user to set aside dice each roll

[x] Application should allow “banking” current score or rolling again.

[x] Application should keep track of total score

[x] Application should keep track of current round

[x] Application should have automated tests to ensure proper operation

lab08:-
[x] Application should implement features from versions 1 and 2

[x] Should handle setting aside scoring dice and continuing turn with remaining dice.

[x] Should handle when cheating occurs

[x] Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.

[x] Handle zilch

[x] If you have questions refer to game rules, the online game or ask the client (aka Instructor)

# Get Started

```
python

poetry install

poetry shell

pytest

```

# Developer

Faisal Kushha,

Mohammad Silwadi ,

Ehab Ahmad,

Suzan Hiary.

## [Pull Request Link: Lab06](https://github.com/game-of-greed-group5/game-of-greed/pull/1)

## [Pull Request Link: Lab07](https://github.com/game-of-greed-group5/game-of-greed/pull/2)

## [Pull Request Link: Lab08](https://github.com/game-of-greed-group5/game-of-greed/pull/3)
