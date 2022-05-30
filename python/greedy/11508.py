n = int(input())

c = []

for i in range(n):
    c.append(int(input()))

c.sort(reverse=True)

cnt = 0
k = 2

for j in range(n):
    if j == k:
        k += 3
        continue
    cnt += c[j]

print(cnt)

# 0 1 [2] 3 4 [5] 6 7 [8] 9 10 [11]