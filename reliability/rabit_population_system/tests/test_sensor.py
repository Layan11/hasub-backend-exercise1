import pytest
import reliability.rabit_population_system.sensor as s
from reliability.rabit_population_system.record import Record
import reliability.rabit_population_system.record_tracker as t

# tests the functions of 'Sensor' class


# tests the 'create_new_record' function
def test_create_new_record():
    sensor = s.Sensor()
    record = sensor.create_new_record()
    assert type(record) == Record


# tests the 'add_record' function when given invalid input
def test_add_record_invalid_input():
    sensor = s.Sensor()
    with pytest.raised(TypeError):
        sensor.add_record(None)
        sensor.add_record("a")
        sensor.add_record(1)


# tests the 'add_record' function when given valid input
def test_add_record_valid_input():
    sensor = s.Sensor()
    tracker = t.Tracker(sensor.max_records)
    prev_records = sensor.curr_records
    prev_tracker_records = tracker.record_num
    sensor.add_record(tracker)
    curr_records = sensor.curr_records
    curr_tracker_records = tracker.record_num
    assert prev_records + 1 == curr_records
    assert prev_tracker_records + 1 == curr_tracker_records




