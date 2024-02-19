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
        print('Its a tie!')
    elif res == 1:
        print('You won!')
    else:
        print('You lost!')


if __name__ == '__main__':
    user_move = '0'
    while user_move not in ['1', '2', '3', '4', '5', '6']:
        user_move = input(print('Please select a number from 1 to 6, representing a boxing move: '))
    random_move = randrange(1, 5)
    print('random move = ' + str(random_move))
    winner(int(user_move), random_move)
