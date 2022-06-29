# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

# 숫자가 키, 이름이 값으로 하나 넣고 이름이 키, 숫자가 값인 값 쌍으로 넣는다.
for i in range(1, N + 1):
    name = input().rstrip()
    dict[str(i)] = name
    dict[name] = str(i)

for _ in range(M):
    print(dict[input().rstrip()])