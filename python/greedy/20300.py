n = int(input())

t = sorted(list(map(int, input().split())))

start = 0
end = n - 1
m = t[end]

if n % 2 == 1:
    end -= 1

while start < end:
    if m < t[start] + t[end]:
        m = t[start] + t[end]
    start += 1
    end -= 1

print(m)

# 1 5 8 9 11 - 13
# 1 5 8 9 11 16 - 17
# 1 7 8 9 - 15