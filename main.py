# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from sys import argv
from random import shuffle
import time

SIZE_POLE_QUADRO = 0
SIZE_POLE_HALF_X = 0
SIZE_POLE_HALF_Y = 0
POLE_FIILED = 0
POLE_LIST_MAX = []
TIME_PREV = time.time()
TIME_START = time.time()

min_num = SIZE_POLE_QUADRO
EXIT_N = False  # если True то выходим с любой глубины move_horse
LIST_MOVE = [(-1, -2), (1, -2),
             (2, -1), (2, 1),
             (1, 2), (-1, 2),
             (-2, 1), (-2, -1)]




#random.seed(time.time())
#shuffle(LIST_MOVE)

def splitting_rectangle(N, M):
    ''' разбиваем прямоугольник N * M на несколько меньших
        таких, что почти все x * y < 36
    '''
    delitel_x = 6
    x = []
    while delitel_x * (len(x) + 2) <= N:
        # while N % delitel_x != 0 and N % delitel_x <= 4:
        x.append(delitel_x)
    tmp = N - delitel_x * (len(x))
    if tmp == delitel_x * 2 - 1 and tmp > 8:
        x.append(delitel_x)      # 7
        x.append(delitel_x - 1)  # 6
    elif tmp == delitel_x * 2 - 2 and tmp > 8:
        x.append(delitel_x - 1)  # 6
        x.append(delitel_x - 1)  # 6
    elif tmp == delitel_x * 2 - 3 and tmp > 8:
        x.append(delitel_x - 2)  # 6
        x.append(delitel_x - 1)  # 5
    elif tmp == delitel_x * 2 - 4 and tmp > 8:
        x.append(delitel_x - 2)  # 5
        x.append(delitel_x - 2)  # 5
    elif tmp != 0:
        x.append(tmp)

    #    x = [delitel_x for i in range(N // delitel_x)]
    #    if N % delitel_x != 0:
    #        x.append(N % delitel_x)

    delitel_y = 5
    y = []
    while delitel_y * (len(y) + 2) <= M:
        y.append(delitel_y)
    tmp = M - delitel_y * len(y)

    if tmp != 0:
        y.append(tmp)

    x.sort(reverse=True)
    #    y.sort(reverse=True)
    rezult = [x, y]
    return rezult


def fill_zero(pole, aa, n, m):  # глобальные переменные инициализируются в этой функции
    global SIZE_POLE_QUADRO
    global SIZE_POLE_HALF_X
    global SIZE_POLE_HALF_Y
    global POLE_FIILED
    global POLE_LIST_MAX

    SIZE_POLE_HALF_X = 0
    SIZE_POLE_HALF_Y = 0

    for pole_a in pole:
        for pole_b in pole_a:
            if pole_b < 0 and pole_b not in POLE_LIST_MAX:
                POLE_LIST_MAX.append(pole_b)
            if pole_b < POLE_FIILED:
                POLE_FIILED = pole_b
    POLE_LIST_MAX.sort(reverse=True)
    print(*POLE_LIST_MAX)

    #min_num = SIZE_POLE_QUADRO
    #exit_N = False  # если True то выходим с любой глубины move_horse


def print_pole_norm(pole):
    global POLE_LIST_MAX
    global TIME_START
    for j in range(len(pole[0])):
        for i in range(len(pole)):
            if pole[i][j] > 0:
                if pole[i][j] == min_num:
                    print(f'\033[32m{pole[i][j]:5d}\033[0m', end='')
                elif -pole[i][j] in POLE_LIST_MAX:
                    print(f'\033[33m{pole[i][j]:5d}\033[0m', end='')
                else:
                    print(f'{pole[i][j]:5d}', end='')
            elif pole[i][j] < 0:
                print('    .', end='')

        print()
    print(f'{(time.time()-TIME_START)//60:5.0f}минут, {(time.time()-TIME_START)%60:2.0f}секунд'+'-'*(5*(SIZE_POLE_X-4)))
    TIME_PREV = time.time()

def move_horse(N: int, x: int, y: int, pole: list, index_max_n: int) -> object:
    ''' Заполняем ячейку массива pole с координатами x и у числом N
        и пытаемся заполнить следующую пустую ячейку с координатами x,y + tmp_move числом N+1.
        Если такой возможности нет уменьшаем N на 1 и возврат, если достигли максимум N == SIZE_POLE_X * SIZE_POLE_Y возврат и выход.
        direct - указывает где должно быть окончание заполнения верху 1, справа 2, внизу 3, слева 4
    '''
    global min_num
    global EXIT_N
    global LIST_MOVE
    global TIME_PREV
    pole[x][y] = N
    if time.time() - TIME_PREV > 100:
        print_pole_norm(pole)
        TIME_PREV = time.time()

    if N == -POLE_LIST_MAX[index_max_n]:
        #print(f'N={N}')
        print_pole_norm(pole)
        if index_max_n == len(POLE_LIST_MAX) - 1:
            EXIT_N = True
            return
        else:
            index_max_n += 1

    for i in LIST_MOVE:
        if pole[x+i[0]][y+i[1]] == POLE_LIST_MAX[index_max_n]:
            N += 1
            x += i[0]
            y += i[1]
            move_horse(N, x, y, pole, index_max_n)
            if EXIT_N:
               return
            N -= 1

            pole[x][y] = POLE_LIST_MAX[index_max_n]
            x -= i[0]
            y -= i[1]


def fill_all_small_rectangle(pole, aa):
    """  малые поля заполняем -1*i*k, что и будет признаком заполнения малого поля"""

    max_num_g = 0
    max_num_index = 0
    for i in aa[0]:
        max_num_index += i
    pole_i = 2
    pole_k = 2
    for k in range(0,len(aa[1]), 2):
        for k_1 in range(aa[1][k]):
            max_num = max_num_g
            for i in range(len(aa[0])):
                max_num += aa[0][i]*aa[1][k]
                for i_1 in range(aa[0][i]):
                    print(f'{max_num:4.0f} ', sep=" ", end="")
                    pole[pole_i][pole_k] = -1 * max_num
                    pole_i += 1
            print()
            pole_i = 2
            pole_k += 1

        max_num_list = [0 for r in range(max_num_index)]

        if k+1 < len(aa[1]):
            for i in range(len(aa[0])-1,-1,-1):
                max_num += aa[0][i] * aa[1][k+1]
                for i_1 in range(aa[0][i]):
                    max_num_index -= 1
                    max_num_list[max_num_index] = max_num
    #        print()
#        print(*max_num_list)
        max_num_g = max_num_list[0]

        if k+1 < len(aa[1]):
            for k_1 in range(aa[1][k+1]):
                max_num_index = 0
                for i in range(len(aa[0])-1,-1,-1):
                    for i_1 in range(aa[0][i]):
                        print(f'{max_num_list[max_num_index]:4.0f} ', sep=" ", end="")
                        pole[pole_i][pole_k] = -1 * max_num_list[max_num_index]
                        pole_i += 1
                        max_num_index += 1
                pole_i = 2
                pole_k += 1
                print()

        print()
    #b=input()

    for j in range(len(pole[0])):
        print(f'j={j:2d}, ',end='')
        for i in range(len(pole)):
            if pole[i][j] >= 0:
                print(f'{"    ."}', end='')
            else:
                print(f'{pole[i][j]:5d}', end='')

        print()
    print('-'*(5*(SIZE_POLE_X+2+2+1)+1))



#print()


if __name__ == '__main__':
    param = argv
    SIZE_POLE_X = int(param[1])
    SIZE_POLE_Y = int(param[2])

    # разбиваем поле на малые поля
    aa = splitting_rectangle(SIZE_POLE_X, SIZE_POLE_Y)
    print(*aa)

    # заполняем большую матрицу -1
    pole = [[0 for i in range(SIZE_POLE_Y + 2 + 2)] for j in range(SIZE_POLE_X + 2 + 2)]

    # заполняем отдельные прямоугольники соответствующими отрицательными значениями
    fill_all_small_rectangle(pole, aa)
    fill_zero(pole, aa, SIZE_POLE_X, SIZE_POLE_Y)

    move_horse(1, 0 + 2, 0 + 2, pole, 0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
