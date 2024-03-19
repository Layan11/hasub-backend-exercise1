
class Events:

    def __init__(self, name):
        self.name = name

    def event_factory(self):
        def asteroid_field():
            print("You are entering an asteroid field!!")

        def space_pirates():
            print("Be careful, there are space pirates in front of you!!")

        def alien_diplomacy():
            print("Alien diplomacy warning!")

        def black_hole():
            print("Attention: you are entering json_funcs black hole! Brace yourself!")

        if self.name == "Asteroid Field":
            return asteroid_field()
        elif self.name == "Space Pirates":
            return space_pirates()
        elif self.name == "Alien Diplomacy":
            return alien_diplomacy()
        elif self.name == "Black Hole":
            return black_hole()
