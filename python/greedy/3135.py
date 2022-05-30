a, b = map(int, input().split())

n = int(input())

m = []

for i in range(n):
    m.append(int(input()))

cnt = 0

tmp = []

for j in m:
    if abs(a - b) > abs(b - j):
       tmp.append(abs(j - b))

if tmp != []:
    tmp_min = min(tmp)
    cnt += 1
else:
    tmp_min = abs(a - b)

while tmp_min > 0:
    tmp_min -= 1
    cnt += 1
print(cnt)





