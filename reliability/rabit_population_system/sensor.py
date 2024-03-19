import asyncio
import random
import sys
import time
# import reliability.rabit_population_system.json_funcs as json_funcs
from json_funcs import write
import record
import record_tracker


class Sensor:
    def __init__(self):
        self.max_records = random.randrange(10, 15)
        print(self.max_records)
        self.curr_records = 0

    def create_new_record(self):
        timestamp = time.time()
        deaths = random.randint(0, sys.maxsize)
        births = random.randint(0, sys.maxsize)
        new_record = record.Record(timestamp, deaths, births)
        return new_record

    # this function generates and adds json_funcs new record
    def add_record(self, tracker):
        new_record = self.create_new_record()
        # try block for all kinds of exceptions in the write function and deal with each one accordingly.
        # try:
        print("Printing what the write to json func returns>>>>>>>>>>>>>>>")
        try:
            write.write_to_json(new_record.deaths)
        except FileNotFoundError:
            print("HAHA ERROR")
        except PermissionError:
            print("TWO")
        except IsADirectoryError:
            print("THREE")
        except FileExistsError:
            print("FOUR")
        except NotADirectoryError:
            print("FIVE")
        except IOError:
            print("SIX")

        self.curr_records += 1
        tracker.record_num += 1
        print("record num = ")
        print(tracker.record_num)

    def start(self, tracker):
        while self.curr_records <= self.max_records:
            print("num of records is " + str(self.curr_records))
            self.add_record(tracker)
            # seconds_to_wait = random.randrange(5, 10)
            seconds_to_wait = random.randrange(1, 2)
            # asyncio.sleep(seconds_to_wait)
            time.sleep(seconds_to_wait)

