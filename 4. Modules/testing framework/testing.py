from assertions import Assert as assertions


def test_mathematical_operations_true():
    print(f'Mathematical Operation assertion where answer is true:\n'
          f'check if {2} is greater than {1} : {assertions(2).greater_than(1)} \n'
          f'check if {15} is equal to {15} : {assertions(15).equal_to(15)} \n'
          f'check if {3} is less than {10} : {assertions(3).less_than(10)} \n')


def test_mathematical_operations_false():
    print(f'Mathematical Operation assertion where answer is false:\n'
          f'check if {1} is greater than {2} : {assertions(1).greater_than(2)} \n'
          f'check if {10} is equal to {15} : {assertions(10).equal_to(15)} \n'
          f'check if {32} is less than {10} : {assertions(32).less_than(10)} \n')


def test_in_list_true():
    num_list = [1, 2, 3, 40]
    print(f'Check if value is in list where answer is true:\n'
          f'check if {2} is in {num_list} : {assertions(2).in_list(num_list)} \n'
          f'check if {40} is in {num_list} : {assertions(40).in_list(num_list)} \n')


def test_in_list_false():
    num_list = [1, 2, 3, 40]
    print(f'Check if value is in list where answer is false:\n'
          f'check if {12} is in {num_list} : {assertions(12).in_list(num_list)} \n'
          f'check if {410} is in {num_list} : {assertions(410).in_list(num_list)} \n')


def test_key_in_dict_true():
    my_dict = {'1': 'red', '2': 'blue', '3': 'red'}
    print(f'Check if key is in dict where answer is true:\n'
          f'check if the key {2} is in {my_dict} : {assertions(2).key_in_dict(my_dict)} \n'
          f'check if the key {1} is in {my_dict} : {assertions(1).key_in_dict(my_dict)} \n')


def test_key_in_dict_false():
    my_dict = {'1': 'red', '2': 'blue', '3': 'red'}
    print(f'Check if key is in dict where answer is false:\n'
          f'check if the key {21} is in {my_dict} : {assertions(21).key_in_dict(my_dict)} \n'
          f'check if the key {10} is in {my_dict} : {assertions(10).key_in_dict(my_dict)} \n')


def test_val_in_dict_true():
    my_dict = {'1': 'red', '2': 'blue', '3': 'red'}
    print(f'Check if value is in dict where answer is true:\n'
          f'check if the value "red" is in {my_dict} : {assertions("red").key_in_dict(my_dict)} \n'
          f'check if the value "blue" is in {my_dict} : {assertions("blue").key_in_dict(my_dict)} \n')


def test_val_in_dict_false():
    my_dict = {'1': 'red', '2': 'blue', '3': 'red'}
    print(f'Check if value is in dict where answer is false:\n'
          f'check if the value "black" is in {my_dict} : {assertions("black").key_in_dict(my_dict)} \n'
          f'check if the value "white" is in {my_dict} : {assertions("white").key_in_dict(my_dict)} \n')


# if __name__ == '__main__':
test_mathematical_operations_true()
test_mathematical_operations_false()
test_in_list_true()
test_in_list_false()
test_key_in_dict_true()
test_key_in_dict_false()
test_val_in_dict_true()
test_val_in_dict_false()
