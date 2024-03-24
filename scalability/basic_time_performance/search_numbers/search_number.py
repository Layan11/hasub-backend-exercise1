from random import random, randint

import time


def search_number(num, list):
    for i in range(100):
        for item in list:
            x = 0

    for item in list:
        if item == num:
            return True
        return False


def search_optimized(num, list):
    for item in list:
        if item == num:
            return True
        return False


def init_input():
    lists = []
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 453, 782, 89, 567, 224, 935, 101, 366, 678, 47]
    list3 = [783, 42, 541, 235, 878, 927, 346, 867, 127, 544, 34, 418, 897, 612, 986, 732,
             452, 345, 678, 876, 998, 701, 112, 856, 333, 521, 105, 724, 901, 255, 840, 671,
             816, 185, 596, 259, 159, 890, 470, 533, 211, 464, 194, 937, 998, 682, 249, 83, 766,
             478, 729, 977, 392, 458, 463, 707, 309, 155, 951, 860, 714, 276, 956, 235, 433, 644,
             333, 99, 169, 634, 784, 415, 58, 611, 904, 23, 246, 701, 342, 42, 749, 332, 91, 428,
             846, 508, 653, 957, 627, 964, 574, 526, 500, 413, 676, 856, 139, 823, 975, 295, 318, 813]

    list4 = [845, 376, 692, 513, 267, 40, 811, 904,
             156, 718, 478, 971, 209, 788, 52, 624,
             357, 123, 892, 609, 312, 991, 498, 793,
             67, 244, 422, 871, 515, 57]

    list5 = [784, 235, 901, 432, 567, 89, 321, 677, 124, 876, 543, 222, 444, 789, 999]

    list6 = [1, 2, 3, 214, 3232, 5]
    list7 = [2]
    list8 = [randint(1, 300) for _ in range(300)]
    list9 = [randint(1, 300) for _ in range(500)]
    list10 = [randint(1, 300) for _ in range(11)]
    lists.append(list1)
    lists.append(list2)
    lists.append(list3)
    lists.append(list4)
    lists.append(list5)
    lists.append(list6)
    lists.append(list7)
    lists.append(list8)
    lists.append(list9)
    lists.append(list10)
    return lists


if __name__ == '__main__':
    num = 2
    input_lists = init_input()
    total_not_optimized = total_optimized = 0
    for list in input_lists:
        start = time.perf_counter()
        search_number(num, list)
        end = time.perf_counter()
        total_not_optimized += (end - start)

        start = time.perf_counter()
        search_optimized(num, list)
        end = time.perf_counter()
        total_optimized += (end - start)

    file = open('C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/scalability/basic_time_performance'
                '/search_numbers/time_results', 'a+')
    file.write("Search number not optimized average time : " + str(total_not_optimized / len(input_lists)) + "\n")
    file.write("Search number optimized average time : " + str(total_optimized / len(input_lists)))
