import pytest
import reliability.rabit_population_system.sensor as s
import reliability.rabit_population_system.record_tracker as t

# tests the functions of 'Tracker' class


# tests the functionality of the 'track_records' function
def test_track_records():
    sensor = s.Sensor()
    tracker = t.Tracker(sensor.max_records)
    # assert that the function returns False when less than 100 records have been added
    assert tracker.track_records() is False

    for i in range(10):
        sensor.add_record(tracker)
    # assert that the function returns True when 10 records have been added
    assert tracker.track_records()


# tests the functionality of the 'decrement_records' function with invalid input
def test_decrement_records_invalid_input():
    sensor = s.Sensor()
    tracker = t.Tracker(sensor.max_records)
    with pytest.raises(TypeError):
        tracker.decrement_records([])
        tracker.decrement_records("as")
        tracker.decrement_records(None)


# tests the functionality of the 'decrement_records' function with valid input
def test_decrement_records_valid_input():
    sensor = s.Sensor()
    tracker = t.Tracker(sensor.max_records)
    for i in range(10):
        sensor.add_record(tracker)
    prev_records = tracker.record_num
    tracker.decrement_records(3)
    curr_records = tracker.record_num
    assert prev_records - 3 == curr_records
