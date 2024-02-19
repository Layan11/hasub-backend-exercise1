

def SieveOfEratosthenes():
    main_number_list = [i for i in range(4, 151)]
    prime_number_list = [2, 3]
    prime = True
    for number in main_number_list:
        for prime in prime_number_list:
            # print("the number is: " + str(number) + ". the prime is: " + str(prime))
            if number % prime == 0:
                prime = False
                break
        if prime:
            prime_number_list.append(number)
            multiplier = 2
            multiplications = number * multiplier
            while multiplications <= 150:
                if multiplications in main_number_list:
                    main_number_list.remove(multiplications)
                multiplier += 1
                multiplications = number * multiplier

        prime = True
    return len(prime_number_list), prime_number_list


if __name__ == '__main__':
    len, list = SieveOfEratosthenes()
    print("There are " + str(len) + " Prime numbers in the range (1, 150).")
    print("The prime numbers are: ")
    print(list)