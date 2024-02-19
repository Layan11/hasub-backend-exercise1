
def gen_even_arr(values, keys):
    for k in keys:
        if values[k]:
            yield values[k][0]


if __name__ == '__main__':
    file = open("declaration of independence.txt", "r")
    declaration_of_independence = file.read()
    declaration_of_independence = declaration_of_independence.split()
    keys = [4, 93, 52, 12, 41, 23, 9, 1, 34, 2, 11, 111, 6, 13, 24, 99, 100,
            30, 10, 26, 16, 29, 155, 32, 37, 61, 15, 42, 3, 633, 27, 70, 77,
            45, 55, 43, 35, 108, 103, 56, 159, 166, 7, 8, 174, 36]
    # print(declaration_of_independence)


    my_gen_arr = gen_even_arr(declaration_of_independence, keys)
    arr = []
    for i in my_gen_arr:
        arr.append(i)
    print(arr)

#our plan is to get all of apples stock as soon as possible!