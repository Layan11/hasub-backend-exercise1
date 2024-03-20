from datetime import time

from reliability.rabit_population_system.json_funcs import read


class Backend:
    def __init__(self):
        self.alive = 100
        self.read_records = 0
        self.curr_read_index = 0

    # this function tries to read the new record if there was an exception for four times max
    def try_again(self):
        for x in range(0, 4):  # try 4 times
            try:
                content = read.read_from_json()
                str_error = None
            except Exception as str_error:
                pass

            if str_error:
                time.sleep(2)  # wait for 2 seconds before trying to read the data again
            else:
                break
        return content

    def update_alive_rabbits(self, records_left):
        if type(records_left) != int:
            raise TypeError
        # should read 10 records from json, after each new added 10 records from sensor into db
        print("updating number of alive rabbits.")
        # try block for all kinds of exceptions in the read function and deal with each one accordingly.
        # for the IOError exception the function tries to read the data again, using the function 'try_again'
        content = None
        try:
            content = read.read_from_json()
        except FileNotFoundError:
            print("Reading error: The file was not found")
        except PermissionError:
            print("Reading error: There was a permission error")
        except IsADirectoryError:
            print("Reading error: IsADirectoryError")
        except FileExistsError:
            print("Reading error: FileExistsError")
        except NotADirectoryError:
            print("Reading error: NotADirectoryError")
        except IOError:
            print("Reading error: IOError, trying again..")
            content = self.try_again()

        # if the reading eas successful, update the number of rabbits
        if content:
            records_num = min(10, records_left)  # in case the records remaining are less than 10
            for i in range(records_num):
                # check if the record is valid, meaning that the number of deaths doesn't exceed
                # the number of rabbits alive, if its invalid ignore the record.
                if self.alive + int(content[self.curr_read_index]) >= int(content[self.curr_read_index + 1]):
                    self.alive += int(content[self.curr_read_index])
                    self.alive -= int(content[self.curr_read_index + 1])
                    self.curr_read_index += 3
                else:
                    print("Discarding record, invalid input!")
            self.read_records += records_num
        # couldn't  read data due to exceptions (other than IOError)
        else:
            print("A reading error occured!")

