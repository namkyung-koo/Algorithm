'''
[ 택배 배달과 수거하기 ]

< 풀이과정 >
1. 크게 세 과정으로 구분한다.
창고에서 cap 만큼 채우기 / 배달(cap -) / 수거(cap +)
종료 조건은 sum(deliveries) == 0 and sum(pickups) == 0
2. 가장 먼 곳부터 배달 및 수거를 해야 이동 거리를 줄일 수 있다.
'''

def solution(cap, n, deliveries, pickups):

    dist = 0

    sum_deliveries = sum(deliveries)
    sum_pickups = sum(pickups)

    while sum_deliveries > 0 and sum_deliveries > 0:
        # 물류 창고에서 택배 충전
        package = cap
        max_dist = []
        # 가장 먼 집부터 배달
        for i in range(n - 1, -1, -1):
            if package <= 0:
                break
            if deliveries[i] == 0:
                continue
            minus = deliveries[i]
            if package >= minus:
                package -= minus
                # 종료 조건을 위해 총합에서도 빼기
                sum_deliveries -= minus
                deliveries[i] = 0
                # 배달한 가장 먼 집까지 간 거리 추가
                max_dist.append(i + 1)
            else:
                deliveries[i] -= package
                sum_deliveries -= package
                package = 0
                break
        # 가장 먼 집부터 수거
        for i in range(n - 1, -1, -1):
            if package >= cap:
                break
            if pickups[i] == 0:
                continue
            if package + pickups[i] <= cap:
                package += pickups[i]
                sum_pickups -= pickups[i]
                pickups[i] = 0
                # 수거한 먼 집까지 간 거리 추가
                max_dist.append(i + 1)
            else:
                pickups[i] -= package
                sum_pickups -= package
                break
        dist += max(max_dist) * 2

    return dist

def main():
    print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
    # 16
    print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
    # 30

main()