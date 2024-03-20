

# this class is to track whenever the sensor adds 10 new records
class Tracker:
    def __init__(self, max_records):
        self.record_num = 0
        self.max_records = max_records

    def get_record_num(self):
        return self.record_num

    # whenever the sensor adds a new records, it updates it in the tracker class using this function
    def record_added(self):
        self.record_num += 1

    # whenever the backend reads a record it decrements it from the tracker so that it resets the counter
    # and starts counting again until it reaches 10 new records again
    def decrement_records(self, num):
        if type(num) != int:
            raise TypeError
        self.record_num -= num

    # checks if there are 10 newly added records
    def track_records(self):
        if self.get_record_num() == 10:
            self.decrement_records(10)
            return True
        else:
            return False
