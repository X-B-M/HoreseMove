# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from sys import argv
from sys import setrecursionlimit
from splitting_rectangle import splitting_rectangle_optimum
from splitting_rectangle import fill_all_small_rectangle_optimum
import time

setrecursionlimit(5000)
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


#print()


if __name__ == '__main__':
    param = argv
  
    if len(param) == 1:
        SIZE_POLE_X = 10
        SIZE_POLE_Y = 10
    elif len(param) == 2:
        SIZE_POLE_X = int(param[1])
        SIZE_POLE_Y = int(param[1])
    else:
        SIZE_POLE_X = int(param[1])
        SIZE_POLE_Y = int(param[2])

    # разбиваем поле на малые поля
    aa = splitting_rectangle_optimum(SIZE_POLE_X, SIZE_POLE_Y)
    print(SIZE_POLE_X, SIZE_POLE_Y, *aa)

    # заполняем большую матрицу -1
    pole = [[0 for i in range(SIZE_POLE_Y + 2 + 2)] for j in range(SIZE_POLE_X + 2 + 2)]

    # заполняем отдельные прямоугольники соответствующими отрицательными значениями
    fill_all_small_rectangle_optimum(pole, aa)
    fill_zero(pole, aa, SIZE_POLE_X, SIZE_POLE_Y)

    move_horse(1, 0 + 2, 0 + 2, pole, 0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
