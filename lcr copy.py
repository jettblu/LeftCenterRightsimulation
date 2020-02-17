# program that simulates the game Left Center Right so as to establish
# the relationship between number of players and average turns till completion
# Number of players and games = input
# graph of players vs. average turns = output

import random
import matplotlib.pyplot as plt


players_roster = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]


def probability_of_each(listless):
    probabilities = {}
    for num in range(max(listless)):
        count = 0
        for item in listless:
            if num == item:
                count += 1
        probabilities[num] = count / len(listless)

    return probabilities


def lcr_sim(players, runs):
        turns_list = []
        # average_turns_list = []
        # players_list = []
        for x in range(0, runs):
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
                return roller, left, right

            players_roster_adjusted = players_roster[0:players]
            length_players_list = len(players_roster_adjusted)
            # print(players_roster_adjusted)
            # print(length_players_list)
            turns = 0
            limiter = 0
            while sum(players_roster_adjusted) != max(players_roster_adjusted):
                for i in range(length_players_list):
                    if players_roster_adjusted[i] > 0 and sum(players_roster_adjusted) - players_roster_adjusted[i] != 0:
                        if i == length_players_list - 1:
                            players_roster_adjusted[i], players_roster_adjusted[i - 1], players_roster_adjusted[
                                limiter] = roll(players_roster_adjusted[i], players_roster_adjusted[i - 1],
                                                players_roster_adjusted[limiter])
                        else:
                            players_roster_adjusted[i], players_roster_adjusted[i - 1], players_roster_adjusted[
                                i + 1] = roll(players_roster_adjusted[i], players_roster_adjusted[i - 1],
                                              players_roster_adjusted[i + 1])
                        turns += 1
                        # print(players_roster_adjusted)
            turns_list.append(turns)
        average_turns = sum(turns_list) / len(turns_list)
        # probs = probability_of_each(turns_list)
        print(average_turns)
        # print(players_roster_adjusted)
        return average_turns
        # plt.axis(0, max(x))
        # print(' ')
        # print(turns_list)

        probs = probability_of_each(turns_list)
        # x = []
        # y = []
        # for i in probs:
        #     x.append(i)
        #     y.append(probs[i])
        #
        # # print(x)
        # # print(y)
        # # print(max(x))
        # plt.plot(x, y)
        # plt.xlabel('Turns')
        # plt.ylabel('Probability')
        # plt.suptitle('LCR Sim. ( Number of Trials:{}; Average Turns: {})'.format(runs, average_turns))
        # plt.axis(0, max(x))
        # plt.show()


def players_avg_turns(most_players, runs):
    x = []
    y = []
    for i in range(3, most_players+1):
        average_turns = lcr_sim(i, runs)
        x.append(i)
        y.append(average_turns)
    # print(x, y)
    plt.plot(x, y)
    plt.xlabel('Players')
    plt.ylabel('Average Turns')
    plt.suptitle('LCR Simulation ({} Trials)'. format(runs))
    plt.show()


players_avg_turns(7, 10000)