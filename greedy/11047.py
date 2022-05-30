n, k = map(int, input().split())

m = []

for i in range(n):
    m.append(int(input()))

coin = []

for j in m:
    if k >= j:
        coin.append(j)

coin.sort(reverse = True)
cnt = 0

for l in coin:
    cnt += k // l
    k %= l

print(cnt)