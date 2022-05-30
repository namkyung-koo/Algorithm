# 우리집엔 도서관이 있어

n = int(input())

l = []

for i in range(n):
    l.append(int(input()))

cnt = 0
i = n - 1
j = 0

while i >= 0:
  if l[i] == n - j:
    cnt += 1
    j += 1
  i -= 1

print(n - cnt)

# 시간초과

# [1 2 3 4 5] - 0
# 1 2 3 [5] 4 - 4
# 1 2 [4 5] 3 - 3
# 1 [3 4 5] 2 - 2
# [3] 2 1 [4 5] - 2
# 1 [4 5] 2 3 - 3
