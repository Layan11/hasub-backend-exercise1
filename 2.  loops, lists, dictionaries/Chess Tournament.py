from random import randint, random, choice


class Player():
    def __init__(self, name, rank, id):
        self.name = name
        self.rank = rank
        self.total_points = 0
        self.id = id


def create_players(num):
    plyrs = []
    for i in range(num):
        name = "player" + str(i + 1)
        rank = randint(1500, 2001)
        plyr = Player(name, rank, i)
        plyrs.append(plyr)
    return plyrs


def play(plyr1, plyr2):
    print("Now playing: " + str(plyr1.name) + " against " + str(plyr2.name))

    plyr1_chances = (1.0 / (1.0 + pow(10, ((plyr1.rank - plyr2.rank) / 400))))
    plyr2_chances = (1.0 / (1.0 + pow(10, ((plyr2.rank - plyr1.rank) / 400))))
    winner = choice([plyr1_chances, plyr2_chances])
    print("Winner in this round is: ")
    if winner == plyr1_chances:
        plyr1.total_points += 1
        plyr2.total_points -= 1
        print(str(plyr1.name))
    else:
        plyr2.total_points += 1
        plyr1.total_points -= 1
        print(str(plyr2.name))


def next_round(matches):
    for i in range(len(matches[1]) - 1):
        matches[1][i], matches[1][i + 1] = matches[1][i + 1], matches[1][i]
    matches[0][-1], matches[1][-1] = matches[1][-1], matches[0][-1]
    for i in range(len(matches[0]) - 1, 1, -1):
        matches[0][i], matches[0][i - 1] = matches[0][i - 1], matches[0][i]


def find_plyr(plyrs, num):
    name = "player" + str(num + 1)
    for plyr in plyrs:
        if plyr.name == name:
            return plyr


def create_match_arrays(plyrs_num):
    matches = [x for x in range(round(plyrs_num / 2))], \
              [x for x in range(plyrs_num - 1, round(plyrs_num / 2) - 1, -1)]
    return matches


def print_winner(plyrs):
    max = 0
    winner_name = ""
    for plyr in plyrs:
        if plyr.total_points > max:
            max = plyr.total_points
            winner_name = plyr.name
    print("The winner of the whole tournament is: " + str(winner_name))


def print_sorted_by_rank(plyrs):
    dict = {}
    ranks = []
    sorted_names = []
    for plyr in plyrs:
        dict[plyr.rank] = plyr
        ranks.append(plyr.rank)
    ranks.sort()
    for rank in ranks:
        sorted_names.append(dict[rank].name)
    print("The players in ascending order by ranks are: ")
    print(sorted_names)


def calc_elo_rank(rank):
    # lets pretend this is how you calculate the elo rank
    elo_rank = 1.2 * rank
    return elo_rank


def print_by_elo_rank_desc(plyrs):
    dict = {}
    elo_ranks = []
    sorted_names = []
    for plyr in plyrs:
        rank = calc_elo_rank(plyr.rank)
        elo_ranks.append(rank)
        dict[rank] = plyr
    elo_ranks.sort(reverse = True)
    for rank in elo_ranks:
        sorted_names.append(dict[rank].name)
    print("The players in descending order by their elo ranks are:  ")
    print(sorted_names)


if __name__ == '__main__':
    plyrs_num = 4
    plyrs = create_players(plyrs_num)
    matches = create_match_arrays(plyrs_num)

    for round in range(plyrs_num - 2):
        for i in range(len(matches[0])):
            play(find_plyr(plyrs, matches[0][i]), find_plyr(plyrs, matches[1][i]))

        next_round(matches)
    print_winner(plyrs)
    print_sorted_by_rank(plyrs)
    print_by_elo_rank_desc(plyrs)
