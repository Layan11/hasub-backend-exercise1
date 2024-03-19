
class Raffle:
    def __init__(self, max_people, max_tickets, ticket_price):
        self.max_people = max_people
        self.max_tickets = max_tickets
        self.ticket_price = ticket_price
        self.earnings = 0
        self.people_list = []
        self.tickets_sold = 0

    def buy_ticket(self, person):
        if len(self.people_list) < self.max_people and self.tickets_sold < self.max_tickets:
            if person not in self.people_list:
                self.people_list.append(person)
            self.earnings += self.ticket_price
            person.add_ticket()
            self.tickets_sold += 1
            print(f"{person.name} just bought a ticket!")
        else:
            print("Tickets are sold out!")
