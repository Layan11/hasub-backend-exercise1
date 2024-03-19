

class Backend:
    def __init__(self):
        self.alive = 100
        self.read_records = 0

    def update_alive_rabbits(self):
        # should read 10 records from json, after each new added 10 records from sensor into db

        print("in update rabbitttttttttttttttt")
        self.read_records += 10

