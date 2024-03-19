import pytest
from reliability.basic_testing.lottery import Lottery
from reliability.basic_testing.person import Person


# test if the picked winners are a valid output, of type Person, and check if they are
# in the list of people in the lottery
def test_valid_input():
    lottery = Lottery(3, 4, 5)
    people = lottery.people_names
    winners = lottery.pick_winners(people, 3)
    for winner in winners:
        assert type(winner) == Person
        assert winner.name in lottery.people_names


# test if the function pick winners fails when given invalid input
def test_invalid_input():
    lottery = Lottery(3, 4, 5)
    people = lottery.people_names
    with pytest.raised(TypeError):
        lottery.pick_winners([], 3)
        lottery.pick_winners(1, [])
        lottery.pick_winners("1", '2')
        lottery.pick_winners(people, '2')




