# Four Squares
# 시간 초과로 dp를 올바르게 구현하지 못함.
n = int(input())

dp = []

for i in range(n + 1):
    dp.append(i)

for j in range(2, int(n ** 0.5) + 1):
    k = j * j
    while k <= n:
        dp[k] = min(dp[k], dp[k - j * j] + 1)
        k += 1

print(dp[n])
    

# k는 인덱싱에 필요한 변수
# 왜 리스트을 사용하는지 ? -> dp로 시간을 줄이기 위해 ?
# 단순히 자연수 n보다 작은 제곱수들 중 가장 큰 것으로만 빼서 계산하게 되면 틀린다.
