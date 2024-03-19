import lottery

if __name__ == '__main__':
    max_people = 5  # these numbers can be changed, this is just for testing.
    max_tickets = 6
    price = 5
    num_of_people = 3
    lottery = lottery.Lottery(max_people, max_tickets, price)
    people_list, people_names = lottery.create_people(num_of_people)
    lottery.raffle.buy_ticket(people_list[0])
    lottery.raffle.buy_ticket(people_list[0])
    lottery.raffle.buy_ticket(people_list[0])
    lottery.pick_winner(people_names)
    lottery.pick_winners(2, people_names)

