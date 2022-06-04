# 캠핑
i = 1

while 1:
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    res = (V // P) * L

    if V % P <= L:
        res += V % P
    else:
        res += L

    print('Case ', i, ': ', res, sep='')
    i += 1