# 도서관
N, M = map(int, input().split())

L = sorted(list(map(int, input().split())))

dir = 0

for i in range(N):
    if L[i] < 0:
        dir = -1
    else:
        dir += 1
        break

minV = abs(L[0])
maxV = abs(L[-1])

if N <= M:
    if dir == -1:
        print(abs(min(L)))
    elif dir == 1:
        print(max(L))
    else:
        if minV > maxV:
            print(minV + maxV * 2)
        else:
            print(minV * 2 + maxV)
    exit()
# 예제 4 처리 완료

res = 0

if minV > maxV:
    for j in range(1, N + 1, M):
        if L[-j] < 0:
            break
        res += abs(L[-j]) * 2
    for k in range(M, N, M):
        if L[k] >= 0:
            break
        res += abs(L[k]) * 2
    res += minV

else:
    for l in range(M + 1, N + 1, M):
        if L[-l] < 0:
            break
        res += abs(L[-l]) * 2
    for m in range(0, N - M, M):
        if L[m] >= 0:
            break
        res += abs(L[m]) * 2
    res += maxV

print(res)

# [-39 -37] [-29 -28] [-6] [2 11] -131 -> 양방향(minV)
# [-39 -37] [-29 -28] [-6 1] [2 11] -133
# [-45 -26 -18] [-9 -4] / [22 40 50] -158 -> 양방향(maxV)
# [-4 -3] [-1 2] [6 11] - abs(V1) = 6 / V2 = 10 / a: 25, o: 21
# [-1 3] [4 5] / [6 11] -29 -> abs(V1) = 11 / V2 = 13 / a: 29, o: 23
# [-10 -9 -8] / [1 2 21] -41-> 양방향(maxV) / 음수 스타트
# [-10 -9] [-8 1] [2 21] - abs(V1) = 26 / V2 = 28 / a: 59, o: 57
# [0 1] [2 3] [4 5] [6 7] / [8 9] -41 -> 단방향(maxV) / 양수 스타트