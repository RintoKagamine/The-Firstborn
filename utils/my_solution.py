# coding=utf-8

def check(a):
    # zero = [0,0,0]
    # if a[0] == a [1] != zero:
    #     return False
    # if a[1] == a [2] != zero:
    #     return False
    # if a[2] == a [0] != zero:
    #     return False 
    # zero = tuple(zero)
    # if a[0][0], a[1][0], a[2][0] ==  a[0][1], a[1][1], a[2][1] != zero:
    #     return False
    # if a[0][0], a[1][0], a[2][0] ==  a[0][2], a[1][2], a[2][2] != zero:
    #     return False
    # if a[0][2], a[1][2], a[2][2] ==  a[0][1], a[1][1], a[2][1] != zero:
    #     return False
    # return True
    x, o = 0, 0

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 1:
                x += 1
            elif a[i][j] == -1:
                o += 1
    if abs(x - o) > 1:
        return False
    return True

def noughts_n_crosses(a):
    #assert check(a)
    if a[0][0] == a[1][1] == a[2][2] != 0:
        return (True, a[0][0])
    if a[2][0] == a[1][1] == a[0][2] != 0:
        return (True, a[2][0])
    for i in (0, 1, 2):
        if a[i][0] == a[i][1] == a[i][2] != 0:
            return (True, a[i][0])
        if a[0][i] == a[1][i] == a[2][i] != 0:
            return (True, a[0][i])
    if 0 not in a[0] + a[1] + a[2]:
        return (True, 2) #0
    return (False, None)
# coding=utf-8