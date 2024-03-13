import game
import spaceship


url = "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=xml"

if __name__ == "__main__":
    events_list = ["Asteroid Field", "Space Pirates", "Alien Diplomacy", "Black Hole"]
    my_spaceship = spaceship.Spaceship("MySpaceship", 200, 100)
    game = game.Game(my_spaceship, events_list)
    game.game()
