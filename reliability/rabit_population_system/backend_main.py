


def main(backend, tracker):
    while backend.read_records <= tracker.max_records:

        print("TRAKER NUM ISSSSS " + str(tracker.record_num))
        # if tracker.record_num >= 10:
        #     print("WTF IS P|HAPPENINH")
        if tracker.track_records():
            print("INN IFFFFFFFFFFFFFFffffffffffffffffffffffffffffffff")
            backend.update_alive_rabbits()