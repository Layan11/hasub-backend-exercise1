import asyncio
import multiprocessing
import time
import random

from backend_main import main as backend_main
import sensor
import backend
import record_tracker

if __name__ == '__main__':
    sensor = sensor.Sensor()
    tracker = record_tracker.Tracker(sensor.max_records)
    # process1 = multiprocessing.Process(target=sensor.start, args=[tracker])
    #
    backend = backend.Backend()  # this is not asynchronous!!!
    # process2 = multiprocessing.Process(target=backend_main, args=[backend, tracker])
    #
    # process1.start()
    # process2.start()
    # process1.join()
    # process2.join()
    #
    # print("SOMETHING STUPID")
    while sensor.curr_records < sensor.max_records:
        print("num of records is " + str(sensor.curr_records))
        sensor.add_record(tracker)
        seconds_to_wait = random.randrange(5, 10)
        # seconds_to_wait = random.randrange(1, 2)
        asyncio.sleep(seconds_to_wait)
        # time.sleep(seconds_to_wait)

        if tracker.track_records():
            print("INN IFFFFFFFFFFFFFFffffffffffffffffffffffffffffffff")
            backend.update_alive_rabbits()

    print("diff is " + str(tracker.max_records - backend.read_records))
    while backend.read_records < tracker.max_records:
        print("IN HERE YALL")
        backend.update_alive_rabbits()
