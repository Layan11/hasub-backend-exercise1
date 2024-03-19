from reliability.basic_testing.person import Person


# test if the function of add_ticket works correctly and adds one everytime the person buys a ticket
def test_valid_input():
    person = Person("person1")
    person.add_ticket()
    assert person.tickets_num == 1
    person.add_ticket()
    assert person.tickets_num == 2




