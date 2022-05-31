# 안테나
N = int(input())

L = sorted(list(map(int, input().split())))

if len(L) % 2 == 0:
    print(L[len(L) // 2 - 1])
else:
    print(L[len(L) // 2])

# 중앙값 개념
# 1 5 5 7 9 - 5
# 1 9 9 9 - 9 가중치 부여 ?