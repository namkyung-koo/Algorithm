'''
< 풀이과정 >
1. 딕셔너리 형태로 변환. 난이도(key) - 해당 난이도를 클리어 하지 못한 사용자(value)
예시 => {'1': 1, '2': 3, '3': 2, '4': 1, '5': 0, '6(모두 클리어)': 1}

2. 두 번째 딕셔너리.  난이도(key) - 실패율(클리어 못한 사람 / 해당 난이도 이상 도달한 사람)
예시 => {'1': 1/8, '2': 3/7, '3': 2/4, '4': 1/2, '5': 0/1}
3. value를 기준으로 내림차순 정렬한 뒤 리스트 형태로 key(난이도) 반환
'''

def list_to_dict(stages):
    
    d = dict()
    for difficulty in stages:
        if difficulty in d:
            d[difficulty] += 1
        else:
            d[difficulty] = 1

    return dict(sorted(d.items()))

def solution(N, stages):
    
    num_players = len(stages)
    clear_failures = list_to_dict(stages)
    failure_rates = dict()

    for difficulty in clear_failures:
        if int(difficulty) > N:
            break
        failure_rates[difficulty] = int(clear_failures[difficulty]) / num_players
        # 다음 난이도까지 도달하지 못한 플레이어의 수 빼기
        num_players -= int(clear_failures[difficulty])
        
    # value를 기준으로 내림차순 정렬
    tuple_list = sorted(failure_rates.items(), key=lambda x: x[1], reverse=True)
    # 튜플을 다시 리스트로 변환
    answer = [t[0] for t in tuple_list]
    # 없는 원소들 채워주기
    for n in range(1, N + 1):
        if n not in answer:
            answer.append(n)
    return answer

def main():
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    # [3,4,2,1,5]
    print(solution(4, [4,4,4,4,4]))
    # [4,1,2,3]

main()