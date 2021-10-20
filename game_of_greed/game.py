from game_of_greed.game_logic import GameLogic, Banker
from collections import Counter


class Game:

    def __init__(self):
        self.count = 0
        self.bank = 0
        self.score = 0
        self.result = 0
        self.redice = 0
        self.count_number = []

    def play(self, roller=None):
        """
        First it will promot a welcoming message to the user, then the game will ask the user if he want to play the game or not.
        if the user choose not play, the game will promot a good bye message.
        """
        roller = roller or GameLogic.roll_dice
        dice = 6
        print('Welcome to Game of Greed')
        print('(y)es to play or (n)o to decline')

        self.count += 1
        start_game = input('> ')
        start = True
        f_res = 'no'
        if start_game.lower() == "n":
            print('OK. Maybe another time')
            start = False

        while start:
            """
             If the user choose to play he will continue by choosing from the promoted numbers. After he get the result he could continue by roll again or go to bank and check his balance or quit the game.
            """
            if start_game.lower() == "y" and type(f_res) == str:

                print('Starting round {}'.format(self.count))
                print('Rolling {} dice...'.format(dice))
                rolling = roller(dice)
                if GameLogic.calculate_score(tuple(rolling)) == 0:
                    f_res = '1'
                    print('****************************************')
                    print('**        Zilch!!! Round over         **')
                    print('****************************************')
                    print(
                        'You banked 0 points in round {}'.format(self.count))
                    print('Total score is 0 points')
                roll_numbers = ""
                for num_dice in rolling:
                    roll_numbers = roll_numbers + str(num_dice) + " "
                print('*** {}***'.format(roll_numbers))
                print('Enter dice to keep, or (q)uit:')

                user_response = input('> ')
            if user_response == 'q' or self.count == 100:
                print('Thanks for playing. You earned {} points'.format(self.bank))
                break

            elif user_response != 'b':

                f_res = 1
                credit = list(user_response)
                # for i in credit:
                #     total.append(int(i))
                total = [int(char) for char in credit if char.isdigit()]
                self.score = GameLogic.calculate_score(tuple(total))
                self.result = GameLogic.calculate_score(tuple(total))
                new_dice = dice - len(total)
                self.count_number = total
                # new_dice = dice-len(data)
                # self.input_num = data
                # roll = roller(dice)
                if GameLogic.validate_keepers(tuple(rolling), tuple(total)) == False:
                    print('Cheater!!! Or possibly made a typo...')
                    rolling = roller(dice)
                    if GameLogic.calculate_score(rolling) == 0:
                        f_res = '1'
                        print('****************************************')
                        print('**        Zilch!!! Round over         **')
                        print('****************************************')
                        print('You banked 0 points in round {}'.format(self.count))
                        print('Total score is 0 points')
                        self.count += 1
                        continue

                    roll_numbers = ""
                    for num in rolling:
                        roll_numbers += str(num) + " "
                    print("*** {}***".format(roll_numbers))
                    print('Enter dice to keep, or (q)uit:')
                    respone = input('> ')
                    credit = list(respone)
                    total = [int(char) for char in credit if char.isdigit()]
                    self.score = GameLogic.calculate_score(tuple(total))
                    self.result = GameLogic.calculate_score(tuple(total))
                    new_dice = dice-len(total)
                    self.input_num = total
                if GameLogic.calculate_score(rolling) == 0:
                    f_res = '1'
                    print('****************************************')
                    print('**        Zilch!!! Round over         **')
                    print('****************************************')
                    print('You banked 0 points in round {}'.format(self.count))
                    print('Total score is 0 points')
                    self.count += 1
                    continue

                data_count = Counter(total)
                data_count_most = data_count.most_common()
                if len(data_count_most) == 3 and list(data_count.values())[0] == 2:
                    self.redice = 6
                print(
                    'You have {} unbanked points and {} dice remaining'.format(self.result, new_dice))
                print(f'(r)oll again, (b)ank your points or (q)uit:')
                user_response = input('> ')
            """
           If the user go the bank he will check his points in the round and total of points he have.
            """
            if user_response == "b":
                self.bank = self.bank + self.score
                print(
                    'You banked {} points in round {}'.format(self.result, self.count))
                self.count += 1
                print('Total score is {} points'.format(self.bank))
                self.result = 0
                f_res = "1"
            """
           If the user roll again he will continue to play with the game based on the game rules, so the number of dice will reduced based on what he choose in the previous round.
            """
            if user_response == "r":
                dice = dice - len(credit)
                if self.redice == 6:
                    dice = 6
                print('Rolling {} dice...'.format(dice))
                rolling = roller(dice)
                roll_numbers = ""
                for num_dice in rolling:
                    roll_numbers = roll_numbers + str(num_dice) + " "
                print(f'*** {roll_numbers}***')
                if GameLogic.calculate_score(rolling) == 0:
                    f_res = '1'
                    dice = 6
                    print('****************************************')
                    print('**        Zilch!!! Round over         **')
                    print('****************************************')
                    print('You banked 0 points in round {}'.format(self.count))
                    print('Total score is 0 points')
                    self.count += 1
                    continue

                print('Enter dice to keep, or (q)uit:')
                f_res = 1
                user_response = input('> ')


if __name__ == '__main__':
    print('Working')
    gaming = Game()
    gaming.play()
