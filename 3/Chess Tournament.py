from random import randint


class Player():
    def __init__(self, name, rank, total_points, id):
        self.name = name
        self.rank = rank
        self.total_points = total_points
        self.id = id


def create_players(num):
    plyrs = []
    for i in range(num):
        name = "player" + str(i + 1)
        rank = randint(1500, 2001)
        plyr = Player(name, rank, 0, i)
        plyrs.append(plyr)
    return plyrs


def play(plyr1, plyr2):
    print("Now playing: " + str(plyr1.name) + " against " + str(plyr2.name))

    plyr1_chances = (1.0 / (1.0 + pow(10, ((plyr1.rank - plyr2.rank) / 400))))
    plyr2_chances = (1.0 / (1.0 + pow(10, ((plyr2.rank - plyr1.rank) / 400))))
    draw_chance = 0.2
    print("THE TOTAL IS: " + str(0.8 * (plyr1_chances + plyr2_chances) + draw_chance))
    #pick one how?
    # then add 1 0 or 0.5 depending on who won
    # update ranks according to elo


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


if __name__ == '__main__':
    plyrs_num = 4
    plyrs = create_players(plyrs_num)
    matches = [x for x in range(round(plyrs_num / 2))],\
              [x for x in range(plyrs_num - 1, round(plyrs_num / 2) - 1, -1)]

    for round in range(plyrs_num - 2):
        for i in range(len(matches[0])):
            play(find_plyr(plyrs, matches[0][i]), find_plyr(plyrs, matches[1][i]))


        next_round(matches)
