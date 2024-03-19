import random
from reliability.basic_testing.person import Person
from reliability.basic_testing.raffle import Raffle


class Lottery:
    def __init__(self, max_people, max_tickets, ticket_price):
        self.raffle = Raffle(max_people, max_tickets, ticket_price)
        self.people_list = None
        self.people_names = None

    def pick_winner(self, names_list):
        winner = random.choice(names_list)
        print(f"The winner of this lottery is: {winner}!")
        return winner

    def pick_winners(self, winners_num, names_list):
        winners = random.choices(names_list, k=winners_num)
        print(f"The {winners_num} winners of this lottery are: {winners}")
        return winners

    def create_people(self, people_num):
        if type(people_num) != int:
            print("Invalid input")
            pass
        people_list = []
        people_names = []
        for i in range(people_num):
            person = Person("person" + str(i + 1))
            people_list.append(person)
            people_names.append(person.name)
            self.people_list = people_list
            self.people_names = people_names
        return people_list, people_names
