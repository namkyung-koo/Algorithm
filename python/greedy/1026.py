# 보물
N = int(input())

A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))

b = sorted(B, reverse=True)

res = 0

for i in range(N):
    res += A[i] * b[i]

print(res)