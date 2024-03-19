import pytest
from reliability.basic_testing.lottery import Lottery
from reliability.basic_testing.person import Person


# test if the function create people, creates a list of people of type Person, and gives them names
# of type string and starts with the word 'person'
def test_valid_input():
    lottery = Lottery(3, 4, 5)
    people_list, people_names = lottery.create_people(3)
    for name in people_names:
        assert type(name) == str
        assert name.startswith("person")
    for person in people_list:
        assert type(person) == Person
        assert person.name is not None


# test if the function create_people fails when given invalid input
def test_invalid_input():
    lottery = Lottery(3, 4, 5)

    with pytest.raised(TypeError):
        people_list, people_names = lottery.create_people('3')
        lottery.pick_winners([])
        lottery.pick_winners(None)




