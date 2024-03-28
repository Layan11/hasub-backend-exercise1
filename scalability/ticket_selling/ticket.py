

class Ticket:
    def __init__(self, id, price, event):
        self.id = id
        self.price = price
        self.event = event
        self.is_sold = False
