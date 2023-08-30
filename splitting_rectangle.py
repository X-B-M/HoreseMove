
def splitting_rectangle(N, M):
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

#    x.sort()
#    y.sort(reverse=True)
    rezult = [x, y]
    return rezult


if __name__ == '__main__':
    a = splitting_rectangle(49, 49)
    print(a)
