# 로프
N = int(input())

L = []

for _ in range(N):
    L.append(int(input()))

L.sort()
res = L[0] * N

for i in range(len(L) - 1):
    if res < L[i + 1] * (N - 1):
        res = L[i + 1] * (N - 1)
    N -= 1

print(res)

# [10 10 6] - 20
# [7 5 6] - 15