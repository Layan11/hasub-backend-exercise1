import time


class Request:
    def __init__(self, user_id, tickets_num):
        self.time_stamp = time.time()
        self.user_id = user_id
        self.tickets_num = tickets_num
