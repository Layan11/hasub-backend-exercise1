import random
from random import randint


class Pokemon:
    last_used_idx = 0

    def __init__(self, name, level, strength, speed, type, life):
        self.name = name + str(Pokemon.last_used_idx)
        self.level = level
        self.strength = strength
        self.speed = speed
        self.type = type
        self.life = life
        Pokemon.last_used_idx += 1


class Player:
    def __init__(self, name, pokemons):
        self.name = name
        self.pokemons = pokemons


def generate_5_pokemons(player_name):
    pokemons = []
    types = ["fire", "water", "earth", "wind"]
    for i in range(5):
        name = player_name + "pokemon_"
        level = randint(0, 101)
        strength = randint(0, 11)
        speed = randint(0, 6)
        type = random.choice(types)
        pokemon = Pokemon(name, level, strength, speed, type, 120)
        pokemons.append(pokemon)
    return pokemons


def choose_random(pokemons):
    life = 0
    while life <= 0:
        pokemon = random.choice(pokemons)
        life = pokemon.life
    return pokemon


def check_for_winner(player1, player2):
    has_pokemons = False
    for pokemon in player1.pokemons:
        if pokemon.life > 0:
            has_pokemons = True
    for pokemon in player2.pokemons:
        if pokemon.life > 0:
            if has_pokemons == True:
                return None, None
            else:
                return player2.name, player1.name
    return player1.name, player2.name


def attack_order(player1, player2):
    rand = randint(1, 21)
    if rand + player1.speed > rand + player2.speed:
        return player1, player2
    return player2, player1


def turn_to_index(type):
    if type == "fire":
        return 0
    elif type == "water":
        return 1
    elif type == "earth":
        return 2
    else:
        return 3


def calculate_damage(attacker, opponent):
    damage_table = [[None, "fire", "earth", "fire"],
                    ["water", None, "water", "wind"],
                    ["earth", "water", None, "earth"],
                    ["fire", "wind", "earth", None]]

    if attacker.type == opponent.type or damage_table[turn_to_index(opponent.type)][turn_to_index(attacker.type)] == opponent.type:
        damage = randint(1, 21) + attacker.strength
    else:
        damage = 2 * (randint(1, 21) + attacker.strength)
    return damage


def death_update(curr_player1, curr_player2):
    if curr_player1.life <= 0:
        print(curr_player1.name + " has died.")
        curr_player1 = choose_random(player1.pokemons)
        print(curr_player1.name + " has joined the fight.")
    if curr_player2.life <= 0:
        print(curr_player2.name + " has died.")
        curr_player2 = choose_random(player2.pokemons)
        print(curr_player2.name + " has joined the fight.")
    return curr_player1, curr_player2


def attack(curr_player1, curr_player2):
    attacker, opponent = attack_order(curr_player1, curr_player2)
    damage = calculate_damage(attacker, opponent)
    opponent.life -= damage
    print(attacker.name + " attacks " + opponent.name + ". deals " + str(damage) + " damage. "
          + opponent.name + " now has " + str(opponent.life) + " amount of life after the attack.")


def create_players():
    player1 = Player("player1", generate_5_pokemons("player1"))
    player2 = Player("player2", generate_5_pokemons("player2"))
    return player1, player2


if __name__ == '__main__':
    player1, player2 = create_players()
    curr_player1 = choose_random(player1.pokemons)
    print(curr_player1.name + " has joined the fight.")
    curr_player2 = choose_random(player2.pokemons)
    print(curr_player2.name + " has joined the fight.")
    win = False
    while not win:
        curr_player1, curr_player2 = death_update(curr_player1, curr_player2)
        while curr_player1.life > 0 and curr_player2.life > 0:
            attack(curr_player1, curr_player2)

        winner, loser = check_for_winner(player1, player2)
        if winner:
            win = True
    print("The winner is: " + winner + "! \nThe loser is: " + loser + ".")