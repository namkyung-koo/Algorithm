from time import time

start = time()
n = int(input())

l = sorted(list(map(int, input().split())))

k = []

res = 0

for i in range(n):
    for j in range(n):
        res += abs(l[i] - l[j])
    k.append(res)
    res = 0

print(l[k.index(min(k))])

end = time()
print (end - start)

# 1 3 12 35 78 100
# 1 3 10 12 35 78 100