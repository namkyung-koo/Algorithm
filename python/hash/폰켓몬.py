# 폰켓몬

""" 
< 풀이 과정 >
우선 nums의 개수 / 2 (max)만큼이 선택할 수 있는 최대값이다.
nums를 순회하면서 해당 폰켓몬이 처음 등장할 때만 answer += 1을 해준다.
시간복잡도는 폰켓몬 하나를 기준으로 계속 반복문을 돌려야하기 때문에 O(n)으로 추측.
폰켓몬 리스트를 순회하며 dictionary에 삽입.
키는 해당 폰켓몬, 값은 리스트 내부의 해당 폰켓몬 개수.
해당 폰켓몬 갯수가 0이면 1로 올리고 answer += 1
answer > max == answer = max 
"""

def solution(nums):
    max_ponkemon = len(nums) // 2
    ponkemon_dict = {}
    answer = 0

    for ponkemon in nums:
        if ponkemon not in ponkemon_dict:
            ponkemon_dict[ponkemon] = 1
            answer += 1
            
    if answer > max_ponkemon:
        answer = max_ponkemon
    
    return answer

# 피드백
# 프로그래머스의 플랫폼에서 인자 받는 방법을 몰라서 헤맸다.