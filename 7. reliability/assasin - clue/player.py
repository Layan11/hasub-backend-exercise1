

# a class for the player, it has all the attributes the player has in the game
class Player:
    def __init__(self, name, last_visited, favorite_weapons, innocent):
        self.name = name
        self.last_visited = last_visited
        self.favorite_weapons = favorite_weapons
        self.innocent = innocent
        self.dead = False
