import random
import matplotlib.pyplot as plt


def probability_of_each(listless):
    probabilities = {}
    for num in range(max(listless)):
        count = 0
        for item in listless:
            if num == item:
                count += 1
        probabilities[num] = count / len(listless)

    return probabilities


players_roster = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]


def sample_runs_3(runs):
    turns_list = []
    for x in range(0, runs):
        player_1 = 3 # each player starts with three chips
        player_2 = 3
        player_3 = 3
        pot_list = []
        turns = 0
        tally = 0

        def roll(roller, left, right):
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)  # establishes random nature of dice rollin'
            dice_3 = random.randint(1, 6)
            dice_list = [dice_1, dice_2, dice_3]
            center = 0
            chances = roller
            if chances > 3:  # prevents an out of bounds error on the list below
                chances = 3
            for dice in dice_list[0:chances]:  # establishes LCR rules
                if dice == 1:
                    right += 1
                    roller -= 1
                if dice == 2:
                    left += 1
                    roller -= 1
                if dice == 3:
                    center += 1
                    roller -= 1
            return roller, left, right, center
        # print('start: [3,3,3]')
        while player_1 != 0 and player_2 != 0 or player_1 and player_3 != 0 or player_2 != 0 and player_3 != 0:  # 'while' stops loop after one player is
            # left with chips
            if player_1 > 0 and player_2 + player_3 != 0:
                player_1, player_2, player_3, pot = roll(player_1, player_2, player_3)  # tally system acts as crude
                # detector of game ending
                # player_tally_list = [player_1, player_2, player_3]
                # print('Player 1: {}'.format(player_tally_list))
                turns += 1
            if player_2 > 0 and player_1 + player_3 != 0:
                player_2, player_3, player_1, pot = roll(player_2, player_3, player_1)
                # player_tally_list = [player_1, player_2, player_3]
                # print('Player 2: {}'.format(player_tally_list))
                turns += 1
            if player_3 > 0 and player_1 + player_2 != 0:
                player_3, player_1, player_2, pot = roll(player_3, player_1, player_2)
                # player_tally_list = [player_1, player_2, player_3]
                # print('Player 3: {}'.format(player_tally_list))
                turns += 1
        turns_list.append(turns)
    average_turns = sum(turns_list) / len(turns_list)
    print(average_turns)
    # print(' ')
    # print(turns_list)

    probs = probability_of_each(turns_list)
    x = []
    y = []
    for i in probs:
        x.append(i)
        y.append(probs[i])

    # print(x)
    # print(y)
    # print(max(x))
    plt.plot(x, y)
    plt.xlabel('Turns')
    plt.ylabel('Probability')
    plt.suptitle('LCR Expected Turns ( Number of Trials:{}; Average Turns: {})'.format(runs, average_turns))
    # plt.axis(0, max(x))
    plt.show()


sample_runs_3(10000)

