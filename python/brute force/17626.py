# Four Squares
n = int(input())

dp = []

for i in range(n + 1):
    dp.append(i)

i = 1
j = 1

while i <= int(n ** 0.5):
    while j < (i + 1) * (i + 1) and j <= n:
        dp[j] = min(dp[j], dp[j - i * i] + 1)
        j += 1
    i += 1

print(dp[n])
    

# i는 인덱싱에 필요한 변수
# 왜 리스트을 사용하는지 ? -> dp로 시간을 줄이기 위해 ?
# 단순히 자연수 n보다 작은 제곱수들 중 가장 큰 것으로만 빼서 계산하게 되면 틀린다.
# 26 - 5^2 + 1^2
# 18인 경우 i가 4로 넘어가버려서, (j - 16) + 1을 계산한다.