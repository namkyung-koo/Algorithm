# 일곱 난쟁이
height = []

for _ in range(9):
    height.append(int(input()))

height.sort()

sum = 0

for idx in range(9):
    sum += height[idx]

over = sum - 100

found = False

for i in range(8):
    for j in range(i + 1, 9):
        if height[i] + height[j] == over:
            height.pop(i)
            height.pop(j - 1)
            found = True
            break
    if found:
        break

for k in range(7):
    print(height[k])