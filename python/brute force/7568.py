# 덩치
N = int(input())

L = [list(map(int, input().split())) for _ in range(N)]

i = 0

while i < N:
    rank = 1
    j = 0
    for j in range(N):
        if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            rank += 1
    print(rank, end=' ')
    i += 1