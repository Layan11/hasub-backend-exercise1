from random import randrange, choice, randint
from server import Server
from ticket import Ticket
from load_balancer import LoadBalancer
from request import Request


def create_tickets(tickets_num, events):
    tickets = []
    for i in range(tickets_num):
        price = randrange(40, 100)
        event = choice.random(events)
        ticket = Ticket(i, price, event)
        tickets.append(ticket)
    return tickets


def create_request():
    return Request(randint, randrange(1, 501))


def main():
    events = ['event1', 'event2', 'event3', 'event4']
    max_requests = 30
    tickets_num = 500
    tickets = create_tickets(tickets_num, events)
    server1 = Server(tickets, max_requests)
    server2 = Server(tickets, max_requests)
    server3 = Server(tickets, max_requests)
    servers = [server1, server2, server3]
    load_balancer = LoadBalancer(servers)

    for i in range(100):
        request = create_request()
        load_balancer.recieve_request(request)
        load_balancer.send_request_to_server()


if __name__ == '__main__':
    main()
