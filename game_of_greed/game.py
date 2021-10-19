from game_of_greed.game_logic import GameLogic, Banker


class Game:

    def __init__(self):
        self.count = 0
        self.bank = 0
        self.score = 0
        self.result = 0
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

        if start_game.lower() == "n":
            print('OK. Maybe another time')
            start = False

        while start:
            """
             If the user choose to play he will continue by choosing from the promoted numbers. After he get the result he could continue by roll again or go to bank and check his balance or quit the game.
            """
            if start_game.lower() == "y":

                print(f'Starting round {self.count}')
                print(f'Rolling {dice} dice...')
                rolling = roller(dice)
                roll_numbers = ""
                for num_dice in rolling:
                    roll_numbers = roll_numbers + str(num_dice) + " "
                print(f'*** {roll_numbers}***')
                print('Enter dice to keep, or (q)uit:')

                user_response = input('> ')
            if user_response == 'q':
                print(f'Thanks for playing. You earned {self.bank} points')
                break

            elif user_response != 'b':
                total = []
                credit = list(user_response)
                for i in credit:
                    total.append(int(i))
                self.score = GameLogic.calculate_score(tuple(total))
                self.result = GameLogic.calculate_score(tuple(total))
                new_dice = dice - len(credit)
                self.count_number = credit

                print(
                    f'You have {self.result} unbanked points and {new_dice} dice remaining')
                print(f'(r)oll again, (b)ank your points or (q)uit:')
                user_response = input('> ')
            """
           If the user go the bank he will check his points in the round and total of points he have.
            """
            if user_response == "b":
                self.bank = self.bank + self.score
                print(
                    f'You banked {self.result} points in round {self.count}')
                self.count += 1
                print(f'Total score is {self.bank} points')
                self.result = 0
            """
           If the user roll again he will continue to play with the game based on the game rules, so the number of dice will reduced based on what he choose in the previous round.
            """
            if user_response == "r":
                dice = dice - len(credit)
                print(f'Rolling {dice} dice...')
                rolling = roller(dice)
                roll_numbers = ""
                for num_dice in rolling:
                    roll_numbers = roll_numbers + str(num_dice) + " "
                print(f'*** {roll_numbers}***')
                print('Enter dice to keep, or (q)uit:')

                user_response = input('> ')


if __name__ == '__main__':
    print('Working')
    gaming = Game()
    gaming.play()
