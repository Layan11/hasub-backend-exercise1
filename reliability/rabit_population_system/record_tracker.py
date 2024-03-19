
class Tracker:
    def __init__(self, max_records):
        self.record_num = 0
        self.max_records = max_records

    def track_records(self):
        if self.record_num == 10:
            self.record_num -= 0
            return True
        else:
            # print("RETURNING FLASE")
            return False
