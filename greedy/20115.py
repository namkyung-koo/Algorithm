n = int(input())

x = sorted(list(map(int, input().split())), reverse=True)

res = x[0]

for i in range(1, n):
    res += x[i] / 2

print(res)