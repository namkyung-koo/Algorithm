# 주유소
N = int(input())

km = list(map(int, input().split()))

price = list(map(int, input().split()))

res = 0

P = price[0]

for i in range(N - 1):
    if price[i] < P:
        P = price[i]
    res += P * km[i]

print(res)
# 5 2 4 1
#  2 3 1