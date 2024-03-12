
def remove_duplicates(list1, list2):
    for prime in list1:
        multiplier = 2
        multiplications = prime * multiplier
        while multiplications <= 150:
            if multiplications in list2:
                list2.remove(multiplications)
            multiplier += 1
            multiplications = prime * multiplier


def SieveOfEratosthenes(n):
    main_number_list = [i for i in range(4, n + 1)]
    prime_number_list = [2, 3]
    remove_duplicates(prime_number_list, main_number_list)
    found_prime = True
    for number in main_number_list:
        for prime in prime_number_list:
            if number % prime == 0:
                found_prime = False
                break
        if found_prime:
            prime_number_list.append(number)
            remove_duplicates(prime_number_list, main_number_list)
        found_prime = True

    for prime in prime_number_list:
        if prime in main_number_list:
            main_number_list.remove(prime)
    return len(prime_number_list), prime_number_list


if __name__ == '__main__':
    num_range = 150
    len, list = SieveOfEratosthenes(num_range)
    print("There are " + str(len) + " Prime numbers in the range (1. vars, logic, conditions, 150).")
    print("The prime numbers are: ")
    print(list)