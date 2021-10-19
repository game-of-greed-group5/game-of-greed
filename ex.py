# from game_of_greed.game_logic import Banker, GameLogic
# from collections import Counter


# class Game:

#     def __init__(self):
#         self.count = 0
#         self.bank = 0
#         self.score = 0
#         self.result = 0
#         self.input_num = []
#         self.redice = 0

#     def play(self, roller=None):
#         roller = roller or GameLogic.roll_dice
#         dice = 6
#         print('Welcome to Game of Greed')
#         print('(y)es to play or (n)o to decline')
#         self.count += 1
#         start_game = input('> ')
#         start = True
#         f_res = 'no'
#         if start_game.lower() == 'n':
#             print('OK. Maybe another time')
#             start = False
#         while start:

#             if start_game.lower() == 'y' and type(f_res) == str:
#                 print(f'Starting round {self.count}')
#                 print('Rolling {} dice...'.format(6))
#                 roll = roller(dice)
#                 if GameLogic.calculate_score(tuple(roll)) == 0:
#                     f_res = '1'
#                     #dice = 6
#                     print('****************************************')
#                     print('**        Zilch!!! Round over         **')
#                     print('****************************************')
#                     print('You banked 0 points in round {}'.format(self.count))
#                     print('Total score is 0 points')

#                 roll_str = ""
#                 for num in roll:
#                     roll_str += str(num) + " "
#                 print(f"*** {roll_str}***")
#                 print('Enter dice to keep, or (q)uit:')
#                 respone = input('> ')
#             if respone == 'q' or self.count == 100:
#                 print('Thanks for playing. You earned {} points'.format(self.bank))
#                 break
#             elif respone != 'b':
#                 f_res = 1
#                 p = list(respone)
#                 data = [int(char) for char in p if char.isdigit()]
#                 self.score = GameLogic.calculate_score(tuple(data))
#                 self.result = GameLogic.calculate_score(tuple(data))
#                 dice_one = dice-len(data)
#                 self.input_num = data
#                 if GameLogic.validate_keepers(tuple(roll), tuple(data)) == False:
#                     print('Cheater!!! Or possibly made a typo...')
#                     roll = roller(dice)
#                     if GameLogic.calculate_score(roll) == 0:
#                         f_res = '1'
#                         dice = 6
#                         print('****************************************')
#                         print('**        Zilch!!! Round over         **')
#                         print('****************************************')
#                         print('You banked 0 points in round {}'.format(self.count))
#                         print('Total score is 0 points')
#                         self.count += 1
#                         continue

#                     roll_str = ""
#                     for num in roll:
#                         roll_str += str(num) + " "
#                     print(f"*** {roll_str}***")
#                     print('Enter dice to keep, or (q)uit:')
#                     respone = input('> ')
#                     p = list(respone)
#                     data = [int(char) for char in p if char.isdigit()]
#                     self.score = GameLogic.calculate_score(tuple(data))
#                     self.result = GameLogic.calculate_score(tuple(data))
#                     dice_one = dice-len(data)
#                     self.input_num = data
#                 if GameLogic.calculate_score(roll) == 0:
#                     f_res = '1'
#                     dice = 6
#                     print('****************************************')
#                     print('**        Zilch!!! Round over         **')
#                     print('****************************************')
#                     print('You banked 0 points in round {}'.format(self.count))
#                     print('Total score is 0 points')
#                     self.count += 1
#                     continue

#                 data_count = Counter(data)
#                 data_count_most = data_count.most_common()
#                 if len(data_count_most) == 3 and list(data_count.values())[0] == 2:
#                     self.redice = 6
#                 print('You have {} unbanked points and {} dice remaining'.format(
#                     self.result, dice_one))
#                 print('(r)oll again, (b)ank your points or (q)uit:')
#                 respone = input('> ')

#             if respone == 'b':
#                 self.bank += self.score
#                 print('You banked {} points in round {}'.format(
#                     self.result, self.count))
#                 self.count += 1
#                 print('Total score is {} points'.format(self.bank))
#                 self.result = 0
#                 f_res = "1"
#             if respone == 'r':
#                 dice = dice-len(p)
#                 if self.redice == 6:
#                     dice = 6
#                 print('Rolling {} dice...'.format(dice))
#                 roll = roller(dice)

#                 roll_str = ""
#                 for num in roll:
#                     roll_str += str(num) + " "
#                 print(f"*** {roll_str}***")
#                 if GameLogic.calculate_score(roll) == 0:
#                     f_res = '1'
#                     dice = 6
#                     print('****************************************')
#                     print('**        Zilch!!! Round over         **')
#                     print('****************************************')
#                     print('You banked 0 points in round {}'.format(self.count))
#                     print('Total score is 0 points')
#                     self.count += 1
#                     continue
#                 print('Enter dice to keep, or (q)uit:')
#                 f_res = 1
#                 respone = input('> ')


# if __name__ == '__main__':
#     x = Game()
#     x.play()
