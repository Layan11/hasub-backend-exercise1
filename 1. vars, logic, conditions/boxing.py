from random import randrange


def winner(num1, num2):
    moves_mat = [[-1, 1, 1, 1, 1, 0],
                 [0, -1, 1, 1, 1, 1],
                 [0, 0, -1, 1, 1, 1],
                 [0, 0, 0, -1, 1, 1],
                 [0, 0, 0, 0, -1, 1],
                 [1, 0, 0, 0, 0, -1]]

    res = moves_mat[num2 - 1][num1 - 1]
    if res == -1:
        print('Its json_funcs tie!')
    elif res == 1:
        print('You won!')
    else:
        print('You lost!')


if __name__ == '__main__':
    user_move = '0'
    while user_move not in ['1. vars, logic, conditions', '2.  loops, lists, dictionaries', '3', '4', '5', '6']:
        user_move = input(print('Please select json_funcs number from 1. vars, logic, conditions to 6, representing json_funcs boxing move: '))
    random_move = randrange(1, 5)
    print('random move = ' + str(random_move))
    winner(int(user_move), random_move)
