from threading import Thread

import utils.utils_fns as fns


class Server:
    def __init__(self, available_tickets, max_requests):
        self.available_tickets = available_tickets
        self.requests = []
        self.max_requests = max_requests
        self.json_account = self.load_json()
        self.ticket_logs = self.json_account["ticket_logs"]

    def available_ids(self):
        ids = []
        for ticket in self.available_tickets:
            ids.append(ticket.id)
        return ids

    def show_unsold(self):
        return self.available_tickets

    def update_tickets(self, tickets_num):
        for i in range(tickets_num):
            self.available_tickets.pop()

    def sell_ticket(self):
        request = self.requests[0]

        if request.tickets_num <= len(self.available_tickets):
            log = fns.gen_log(request.time_stamp, request.user_id, request.tickets_num)
            self.ticket_logs.append(log)
            self.requests.pop()
            self.update_tickets(request.tickets_num)
        else:
            print("Not enough available tickets.")
            raise Exception

    def handle_requests(self):
        threads = []
        for i in range(self.max_requests):
            thread = Thread(target=self.sell_ticket())
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


Server.handle_requests()
