from random import randint
from collections import Counter
"""
GameLogic class Handle calculating score for dice roll and Handle rolling dice
"""
class GameLogic:
    """ 
    calculate_score static method 
    The input to calculate_score is a tuple of integers that represent a dice roll.
    The output from calculate_score is an integer 
    representing the roll’s score according to rules of game.
    """
    @staticmethod
    def calculate_score(num):
        game_rules = {
        (1,1): 100,
        (1,2): 200,
        (1, 3): 1000,
        (1, 4): 2000,
        (1, 5): 3000,
        (1, 6): 4000,
        (2,1): 0,
        (2, 2): 0,
        (2, 3): 200,
        (2, 4): 400,
        (2, 5): 600,
        (2, 6): 800,
        (3,1): 0,
        (3, 2): 0,
        (3, 3): 300,
        (3, 4): 600,
        (3, 5): 900,
        (3, 6): 1200,
        (4,1): 0,
        (4, 2): 0,
        (4, 3): 400,
        (4, 4): 800,
        (4, 5): 1200,
        (4, 6): 1600,
        (5,1): 50,
        (5, 2): 100,
        (5, 3): 500,
        (5, 4): 1000,
        (5, 5): 1500,
        (5, 6): 2000,
        (6,1): 0,
        (6, 2): 0,
        (6, 3): 600,
        (6, 4): 1200,
        (6, 5): 1800,
        (6, 6): 2400,
        (1, 2, 3, 4, 5, 6): 1500,
        (2, 2, 3, 3, 4, 6): 0,
        (2, 2, 3, 3, 6, 6): 1500,
        (1, 1, 1, 2, 2, 2): 1200,
            } 
        
        score = 0 
        dice_counter = Counter(num) 

        new_list = dice_counter.most_common()

        if len(num) == 6 and len(new_list)== 6:
                score = 1500

        elif len(num) == 6 and len(new_list)== 3 and list(dice_counter.values())[0] ==2:
            score = 1500

        else:
          for i in new_list:
             score = score + game_rules.get(i,0)
        return score 
    """ 
    Add roll_dice static method to GameLogic class.
    The input to roll_dice is an integer between 1 and 6.
    The output of roll_dice is a tuple with random values between 1 and 6.
    The length of tuple must match the argument given to roll_dice method.
    """    
    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(0,num_dice))

"""
Banker class Handle shelf, bank and clear_shelf instance method
"""     
class Banker:
    def __init__(self):
        self.balance=0
        self.shelved=0
    """ 
    Input to shelf is the amount of points (integer) to add to shelf.
    shelf should temporarily store unbanked points.
    """
    def shelf(self,value):
        self.shelved = value
    """ 
    bank should add any points on the shelf to total and reset shelf to 0.
    bank output should be the amount of points added to total from shelf.
    """ 
    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
    """
    clear_shelf should remove all unbanked points
    """ 
    def clear_shelf(self):
        self.shelved=0
if __name__ == '__main__':
    print('work')
    x = GameLogic()