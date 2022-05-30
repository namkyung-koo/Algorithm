# 회의실 배정
N = int(input())

L = []

for i in range(N):
    l = list(map(int, input().split()))
    L.append(l)

# 끝 시간 오름차순 정렬 후, 시작 시간 오름차순 정렬
L.sort(key=lambda x: (x[1], x[0]))

cnt = 1
cmp = L[0][1]

# 비교를 통해 회의 수 추가
for j in range(1, len(L)):
    if cmp <= L[j][0]:
        cmp = L[j][1]
        cnt += 1
print(cnt)

# print(L)
# 2 [1 1] [0 1] - 2
# 7 [3 10] [2 2] [1 3] [2 2] [9 10] [4 9] [2 2] - 5
# 5 [6 7] [6 6] [5 6] [5 5] [7 7] - 5
