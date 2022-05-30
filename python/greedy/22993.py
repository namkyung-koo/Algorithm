# 서든어택3

n = input()

m = list(map(int, input().split()))
me = m.pop(0)

m.sort()

for i in m:
    if me > i:
        me += i
    else:
        print("No")
        exit()
print("Yes")