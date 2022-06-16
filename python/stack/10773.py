# 제로
K = int(input())

l = []

for _ in range(K):
    l.append(int(input()))

L = []

for i in range(len(l)):
    if l[i] == 0:
        L.pop()
        continue
    L.append(l[i])

res = 0

for j in range(len(L)):
    res += L[j]

print(res)