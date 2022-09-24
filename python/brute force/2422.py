# 한윤정이 이탈리에 가서 아이스크림을 사먹는데
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

worst = []

# 최악의 맛 조합을 이차원 리스트로 생성
for _ in range(M):
    worst.append(list(map(int, sys.stdin.readline().split())))

# 아이스크림의 종류
flavour = [i for i in range(1, N + 1)]

#아이스크림의 종류를 이용한 조합 만들기
list(map(list, combinations(flavour, 3)))

cnt = 0

