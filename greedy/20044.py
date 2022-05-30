n = int(input())

l = list(map(int, input().split()))

m = []

for i in range(n):
    m.append(min(l) + max(l))
    l.remove(min(l))
    l.remove(max(l))

print(int(min(m)))
