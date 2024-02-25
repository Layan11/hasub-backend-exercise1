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
    print(str(plyr1 + 1) + " against " + str(plyr2 + 1))

def next_round(matches):
    for i in range(len(matches[1]) - 1):
        matches[1][i], matches[1][i + 1] = matches[1][i + 1], matches[1][i]
    matches[0][-1], matches[1][-1] = matches[1][-1], matches[0][-1]
    for i in range(len(matches[0]) - 1, 1, -1):
        matches[0][i], matches[0][i - 1] = matches[0][i - 1], matches[0][i]


if __name__ == '__main__':
    plyrs_num = 4
    plyrs = create_players(plyrs_num)
    matches = [x for x in range(round(plyrs_num / 2))],\
              [x for x in range(plyrs_num - 1, round(plyrs_num / 2) - 1, -1)]

    for round in range(plyrs_num - 2):
        for i in range(len(matches[0])):
            play(matches[0][i], matches[1][i])


        next_round(matches)
