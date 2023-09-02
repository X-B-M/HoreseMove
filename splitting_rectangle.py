
def splitting_rectangle_optimum(N, M):
    ''' разбиваем прямоугольник N * M на несколько меньших
        таких, что  каждый x * y <= 36
    '''
    delitel_x = 6
    x = []
    while delitel_x * (len(x) + 2 ) <= N:
    #while N % delitel_x != 0 and N % delitel_x <= 4:
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

# создаем list в котором в y строках, x ячейки могут быть разного размера
# нулевой элемент это размер y
    xy = []
    for y1 in y:
        xy.append([])
        xy[-1].append(y1)
        for x1 in x:
            if y1 * x1 > 45:
                tmp_x = x1 // 2
                xy[-1].append(x1 - tmp_x)
                xy[-1].append(tmp_x)

            else:
                xy[-1].append(x1)

#    x.sort()
#    y.sort(reverse=True)
    #rezult = [x, y]

    return xy

def fill_all_small_rectangle_optimum(pole, aa):
    """  малые поля заполняем -1*i*k, что и будет признаком заполнения малого поля"""

    pole_i = 2
    pole_j = 2
    max_num_1 = 0
    for j_1 in range(0, len(aa), 2):
        # идем слева направо
        for j in range(aa[j_1][0]):
            pole_i = 2
            max_num = max_num_1
            for i_1 in range(1, len(aa[j_1])):
                max_num += aa[j_1][0] * aa[j_1][i_1]
                for i in range(aa[j_1][i_1]):
                    pole[pole_i][pole_j] = - max_num
                    pole_i += 1
            pole_j += 1
        if j_1+1 >= len(aa):
            break

        # теперь идем справа налево
        for j in range(aa[j_1+1][0]):
            pole_i = - 2 - 1
            max_num_1 = max_num
            for i_1 in range(len(aa[j_1+1])-1, 0, -1):
                max_num_1 += aa[j_1+1][0] * aa[j_1+1][i_1]
                for i in range(aa[j_1+1][i_1]):
                    pole[pole_i][pole_j] = - max_num_1
                    pole_i -= 1
            pole_j += 1

    for j in range(len(pole[0])):
        print(f'j={j:2d}, ',end='')
        for i in range(len(pole)):
            if pole[i][j] >= 10000000:
                print(f'{"    ."}', end='')
            else:
                print(f'{pole[i][j]:5d}', end='')

        print()
    #print('-'*(5*(SIZE_POLE_X+2+2+1)+1))
    print('-' * (5 * (18 + 2 + 2 + 1) + 1))



if __name__ == '__main__':
    aa = splitting_rectangle_optimum(28, 7)
    print(aa)
    pole = [[0 for i in range(7 + 2 + 2)] for j in range(28 + 2 + 2)]

    fill_all_small_rectangle_optimum(pole, aa)
