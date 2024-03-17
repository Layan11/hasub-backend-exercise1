import game

if __name__ == '__main__':
    # get the number of players, and validate the input. Keep asking for input until it is valid.
    while True:
        try:
            players_num = int(input(print("Please enter the number of players: ")))

        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            break
    # create a game instance and use the play method to start playing
    game = game.Game(players_num)
    game.play()
