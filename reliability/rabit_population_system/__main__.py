import asyncio
import multiprocessing
import time
import random

from backend_main import main as backend_main
import sensor
import backend
import record_tracker

# the main function runs the sensor and the backend consecutively in a loop
if __name__ == '__main__':
    # creating a sensor, backend and tracker instances
    sensor = sensor.Sensor()
    tracker = record_tracker.Tracker(sensor.max_records)
    backend = backend.Backend()

    # this loop keeps creating records and adds them to the db until it reaches the max number of records
    # and each time it waits a random number of seconds in the range (5, 10) before it continues to add new records.
    while sensor.curr_records < sensor.max_records:
        print("The number of added records so far is:  " + str(sensor.curr_records))
        sensor.add_record(tracker)
        seconds_to_wait = random.randrange(5, 10)
        asyncio.sleep(seconds_to_wait)  # asynchronous sleep so that other threads don't get blocked

        if tracker.track_records():  # enters this if after every 10 new records have been added
            backend.update_alive_rabbits(tracker.max_records - backend.read_records)
            print("*******************************************************")
            print("NUMBER OF ALIVE RABBITS IS = " + str(backend.alive))
            print("********************************************************")

    # if the number of not read records left is less than 10
    print("Not read records left: " + str(tracker.max_records - backend.read_records))
    while backend.read_records < tracker.max_records:
        backend.update_alive_rabbits(tracker.max_records - backend.read_records)
    print("*********************The end******************************")
    print("THE FINAL NUMBER OF ALIVE RABBITS IS = " + str(backend.alive))
    print("*********************The end******************************")




    # backend = backend.Backend()
    # process1 = multiprocessing.Process(target=sensor.start, args=[tracker])
    #
    #
    # process2 = multiprocessing.Process(target=backend_main, args=[backend, tracker])
    #
    # process1.start()
    # process2.start()
    # process1.join()
    # process2.join()



    # # print("SOMETHING STUPID")
    # while sensor.curr_records < sensor.max_records:
    #     print("num of records is " + str(sensor.curr_records))
    #     sensor.add_record(tracker)
    #     seconds_to_wait = random.randrange(5, 10)
    #     # seconds_to_wait = random.randrange(1, 2)
    #     asyncio.sleep(seconds_to_wait)
    #     # time.sleep(seconds_to_wait)
    #
    #     if tracker.track_records():
    #         print("INN IFFFFFFFFFFFFFFffffffffffffffffffffffffffffffff")
    #         backend.update_alive_rabbits()
    #
    # print("diff is " + str(tracker.max_records - backend.read_records))
    # while backend.read_records < tracker.max_records:
    #     print("IN HERE YALL")
    #     backend.update_alive_rabbits()
