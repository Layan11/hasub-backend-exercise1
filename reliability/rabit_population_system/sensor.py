import random
import time
from reliability.rabit_population_system.json_funcs import write
import reliability.rabit_population_system.record as record


class Sensor:
    def __init__(self):
        self.max_records = random.randrange(100, 300)
        print("The max number of records is: " + str(self.max_records))
        self.curr_records = 0

    # this function creates a new record with random values in the Record class fields
    def create_new_record(self):
        timestamp = time.time()
        deaths = random.randint(0, 1000)  # the max number of deaths and births is chosen to be 1000, it can be changed.
        births = random.randint(0, 1000)
        new_record = record.Record(timestamp, deaths, births)
        return new_record

    # this function tries to write the new record if there was an exception for four times max
    def try_again(self, new_record):
        for x in range(0, 4):  # try 4 times
            try:
                write.write_to_json(new_record)
                str_error = None
            except Exception as str_error:
                pass

            if str_error:
                time.sleep(2)  # wait for 2 seconds before trying to write the data again
            else:
                break

    # this function generates and adds json_funcs new record
    def add_record(self, tracker):
        # if type(tracker) != Tracker:
        #     raise TypeError
        new_record = self.create_new_record()
        # try block for all kinds of exceptions in the write function and deal with each one accordingly.
        # for the IOError exception the function tries to write the data again, using the function 'try_again'

        try:
            write.write_to_json(new_record.to_json())
        except FileNotFoundError:
            print("Writing error: The file was not found")
        except PermissionError:
            print("Writing error: There was a permission error")
        except IsADirectoryError:
            print("Writing error: IsADirectoryError")
        except FileExistsError:
            print("Writing error: FileExistsError")
        except NotADirectoryError:
            print("Writing error: NotADirectoryError")
        except IOError:
            print("Writing error: IOError, trying again..")
            self.try_again(new_record.to_json())

        self.curr_records += 1
        tracker.record_added()
