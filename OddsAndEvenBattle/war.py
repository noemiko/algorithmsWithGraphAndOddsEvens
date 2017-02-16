
# This is odds and evens battle
# odds and evens fight using their binary representation
# battle result dependence of number of points
# positive odd get one point for every 1 bit, but negative odds subtract one
# positive even get one point for every 0 bit, but negative evens subtract one
# side with larger number of points win

from random import randint


class War:

    def __init__(self):
        pass

    # start point
    def calculate_battle(self, battlefield_configuration):
        splitted_enemies = self.split_odd_even(battlefield_configuration)

        even_binnary = self.convert_to_binary(splitted_enemies['even'])
        odd_binnary = self.convert_to_binary(splitted_enemies['odd'])

        odds_points = self.count_battle_points(even_binnary, '1')
        evens_points = self.count_battle_points(odd_binnary, '0')

        winner = self.calculate_winner(odds_points, evens_points)
        return winner

    def split_odd_even(self, data):
        even = [num for num in data if num % 2 == 0]
        odd = [num for num in data if num % 2 != 0]
        return {"even": even, "odd": odd}

    # binary data is array with convert odds or avens
    # win_bit give information which bit give point for this side
    def count_battle_points(self, binary_data, win_bit):
        negative_points, positive_points = 0, 0
        for number in binary_data:
            is_negative = False
            for char in number:
                if char == '-':
                    is_negative = True
                elif char == win_bit:

                    if is_negative:
                        negative_points += 1
                    else:
                        positive_points += 1

        return {'positive': negative_points, 'negative': positive_points}

    def convert_to_binary(self, battlefield_configuration):
        return [('{0:0b}'.format(x)) for x in battlefield_configuration]

    def calculate_winner(self, odds_points, evens_points):

        odds_summary = odds_points['positive'] - odds_points['negative']
        evens_summary = evens_points['positive'] - evens_points['negative']

        winner_points = odds_summary - evens_summary
        if winner_points > 0:
            return 'odds win'
        elif winner_points == 0:
            return 'tie'
        else:
            return 'evens win'


if __name__ == "__main__":

    # generate battlefield configuration
    battlefield_configuration = [randint(-1000, 1000) for _ in range(100)]

    # start War
    war = War()

    # get winner from battle
    print(war.calculate_battle(battlefield_configuration))
