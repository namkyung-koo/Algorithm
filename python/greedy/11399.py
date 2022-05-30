# ATM

N = int(input())

P = sorted(list(map(int, input().split())))

res = 0
j = N

for i in range(N):
    res += P[i] * j
    j -= 1

print(res)
