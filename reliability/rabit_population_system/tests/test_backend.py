import pytest
import reliability.rabit_population_system.backend as b

# tests the functions of 'Backend' class


# tests the 'update_rabbits' function when given invalid input
def test_update_rabbits_invalid_input(records_left):
    backend = b.Backend()
    with pytest.raised(TypeError):
        backend.update_alive_rabbits("a")
        backend.update_alive_rabbits([])
        backend.update_alive_rabbits(None)


# tests the 'update_rabbits' function when given valid input
def test_update_rabbits_valid_input():
    backend = b.Backend()
    prev_idx = backend.curr_read_index
    backend.update_alive_rabbits(1)
    curr_idx = backend.curr_read_index
    assert prev_idx + 3 == curr_idx
    prev_read = backend.read_records
    backend.update_alive_rabbits(10)
    curr_read = backend.read_records
    assert prev_read + 10 == curr_read

