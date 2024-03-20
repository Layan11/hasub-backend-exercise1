import time


# the main function of the backend
def main(backend, tracker):
    # keeps updating the number of rabbits until it reads all of the existing records in the db
    while backend.read_records <= tracker.max_records:
        # it updates the number of alive rabbits only after each 10 newly added records
        if tracker.track_records():
            backend.update_alive_rabbits()
        else:
            # if there are no 10 records yet, it waits for a few seconds to let the sensor time to add new records
            time.sleep(5)
