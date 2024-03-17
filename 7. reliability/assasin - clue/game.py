import random
from player import Player


# This is the game class, and it has all the operations that can be done in the game
class Game:
    def __init__(self, plyrs_num):
        self.plyrs_num = plyrs_num
        self.plyrs = None
        # initiates the places and weapons from corresponding text files
        try:
            self.places = open("places", "r").readlines()
        except IOError:
            print(f"Could not read file 'places'")
        try:
            self.weapons = open("weapons", "r").readlines()
        except IOError:
            print(f"Could not read file 'weapons'")

    def get_plyr(self, plyr_name):
        for plyr in self.plyrs:
            if plyr.name == plyr_name:
                return plyr

    # a function that creates 'players_num' number of players with only one assasin
    def create_players(self):
        plyrs = []
        assasin_flag = False

        for i in range(self.plyrs_num):
            name = "player" + str(i + 1)
            favorite_weapons = random.choices(self.weapons, k=random.randint(1, len(self.weapons)))
            assasin = random.getrandbits(1)
            if assasin and not assasin_flag:
                assasin_flag = True
            elif assasin and assasin_flag:
                assasin = False
            plyr = Player(name, [], favorite_weapons, assasin)
            plyrs.append(plyr)

        self.plyrs = plyrs

    # a function that makes each player visit random place (1-3 places)
    def visit_places(self):
        num_to_visit = random.randint(1, 3)
        visited = random.choices(self.places, k=num_to_visit)
        for plyr in self.plyrs:
            plyr.last_visited.extend(visited)

    # returns the assasin from all the players
    def get_assasin(self):
        for plyr in self.plyrs:
            if not plyr.innocent:
                return plyr

    # this function chooses the murder place and murder weapon, for the assasin who commits the murder
    def murder(self):
        assasin = self.get_assasin()
        murder_place = random.choice(assasin.last_visited)
        murder_weapon = random.choice(assasin.favorite_weapons)
        print(f"A murder has happened in {murder_place}, and the murder weapon is {murder_weapon}")

    # returns all the remaining players who are still alive, besides the given current player
    def get_remaining_plyr_names(self, curr_plyr):
        plyr_names = []
        for plyr in self.plyrs:
            if not plyr.dead and plyr.name != curr_plyr.name:
                plyr_names.append(plyr.name)
        return plyr_names

    # this function gives each living player the option to choose two players to suspect
    def suspect(self):
        for plyr in self.plyrs:
            print(f"Current player: {plyr.name}")
            current_plyrs = self.get_remaining_plyr_names(plyr)
            suspects = []
            print(f"Choose two players you suspect to be the possible murderer, "
                                   f"the current players are: {current_plyrs}")
            for i in range(2):
                # check validity of input, keep asking for input until it is valid
                while True:
                    try:
                        choice = input(print("Choose a suspect: "))
                        if choice not in current_plyrs:
                            raise AttributeError
                    except AttributeError:
                        print(f'Input {choice} is not valid, choose again')
                        continue
                    else:
                        suspects.append(choice)
                        break

            for suspect in suspects:
                curr_suspect = self.get_plyr(suspect)
                if len(curr_suspect.last_visited) > 1:
                    random_places = random.choices(curr_suspect.last_visited, k=2)
                    random_weapon = random.choices(curr_suspect.favorite_weapons, k=1)
                    print(f"For the suspect {suspect}, his randomly 2 visited places are {random_places}, "
                          f"and a random of his favorite weapons is {random_weapon}")
                else:
                    random_weapon = random.choices(curr_suspect.favorite_weapons, k=1)
                    print(f"For the suspect {suspect}, his randomly visited places are {curr_suspect.last_visited}, "
                          f"and a random of his favorite weapons is {random_weapon}")

    # gives every player the option to accuse another player that they think is the assasin
    def accuse(self):
        for plyr in self.plyrs:
            if plyr.innocent:
                current_plyrs = self.get_remaining_plyr_names(plyr)
                print(f"Current player: {plyr.name}")
                while True:
                    # using try and exception to validate the input, keep asking for input until it is valid
                    try:
                        accused = input(print(f"What player would you like to accuse of murder? "
                                                  f"the current players are: {current_plyrs}"))
                        if accused not in current_plyrs:
                            raise AttributeError()
                    except AttributeError:
                        print(f'Input {accused} is not valid, choose again')
                        continue
                    else:
                        break
            # if the accused is the actual assasin the player who accused him wins,
            # otherwise they die and leave the game
            assasin = self.get_assasin()
            if accused == assasin.name:
                print(f"{plyr.name} has won! They have accused the actual murderer who is {assasin.name}. "
                      f"Game over.")
                return True
            else:
                print(f"You have guessed wrong, {accused} is not the murderer, "
                      f"you have been eliminated from the game.")
                plyr.dead = True
        return False

    # returns the number of alive players in the game
    def number_of_alive_plyrs(self):
        alive = 0
        for plyr in self.plyrs:
            if not plyr.dead:
                alive += 1
        return alive

    # this function executes all the moves in the game in the correct order, and keeps playing until there is a winner
    def play(self):
        self.create_players()
        winner = False
        remaining_plyrs = self.number_of_alive_plyrs()
        while not winner and remaining_plyrs > 2:
            self.visit_places()
            self.murder()
            self.suspect()
            winner = self.accuse()
            remaining_plyrs = self.number_of_alive_plyrs()

        if not winner:
            print("The murderer has won! No player was able to reveal him. Game over.")
