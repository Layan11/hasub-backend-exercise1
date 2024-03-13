
class Game:
    def __init__(self, spaceship, events):
        self.spaceship = spaceship
        self.events = events

    def game(self):
        while self.spaceship.health > 0 and self.spaceship.fuel > 0:
            self.spaceship.launch()
            event = self.spaceship.explore(self.events)
            self.spaceship.handle_events(event)
            self.spaceship.health -= 5
            self.spaceship.fuel -=5

        print("Game ended! Horray!")
