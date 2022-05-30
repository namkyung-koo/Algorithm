# 기타줄
N, M = map(int, input().split())

L = []

for _ in range(M):
    L.append(list(map(int, input().split())))

L.sort(key=lambda x: x[0])
A = L[0][0]

L.sort(key=lambda x: x[1])
B = L[0][1]

res = 0

while N >= 6:
    if A <= B * 6:
        N -= 6
        res += A
    else:
        N -= 6
        res += B * 6

while N > 0:
    if A <= B * N:
        N -= 6
        res += A
    else:
        N -= 1
        res += B

print(res)