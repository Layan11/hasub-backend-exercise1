import pytest
from reliability.basic_testing.lottery import Lottery
from reliability.basic_testing.person import Person


# test if the picked winner is a valid output and check if he is in the list of people in the lottery
def test_valid_input():
    lottery = Lottery(3, 4, 5)
    people = lottery.people_names
    assert type(lottery.pick_winner(people)) == Person
    assert lottery.pick_winner(people).name in people


# test if the function pick a winner fails when given invalid input
def test_invalid_input():
    lottery = Lottery(3, 4, 5)
    with pytest.raised(TypeError):
        lottery.pick_winner([])
        lottery.pick_winner(1)
        lottery.pick_winner("1")




