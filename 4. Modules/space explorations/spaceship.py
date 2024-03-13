import random


class Spaceship:
    def __init__(self, name, fuel, health):
        self.name = name
        self.fuel = fuel
        self.health = health

    def __str__(self):
        return f'The spaceship name is: {self.name} ,the health is: {self.health}, the fuel is: {self.fuel}'

    def launch(self):
        print("Launching spaceship into space!!")

    def explore(self, events_list):
        event = random.choice(events_list)
        print(event)
        return event

    def handle_events(self, event):
        if event == "Asteroid Field":
            print("You are entering an asteroid field, would you like to evade it or continue?")

