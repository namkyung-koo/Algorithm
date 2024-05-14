#완주하지 못한 선수

"""
< 풀이과정 >
모든 참가자의 명단이 배열 형태로 담긴 participant와 completion에 참가자의 이름이 있다면, 참가 + 완주도 한 선수다.
그러나 completion 명단에 이름이 없다면 완주를 하지 못한 선수임으로 get 메서드를 이용해 해당 선수의 이름은 반환한다.
핵심은 동일한 키를 가지고 있는지 확인하는 것.

첫 번째 반복문 O(n)
두 번째 반복문 O(n-1)
세 번째 반복문 O(해당 값을 가진 키가 나올 때까지)

+ 문제사항 participant에 중복된 키가 있을 수 있다.
+ participant 리스트를 업데이트 하는 동안 확인하려고 시도할 때, 값이 제대로 처리되지 않을 수 있다.
그러므로 모든 반복문을 완전히 마친 후 확인하는 작업을 수행시킴
"""

def solution(participant, completion):
    
    player_dict = {}
    
    for player in participant:
        if player in player_dict:
            player_dict[player] += 1
        else:
            player_dict[player] = 1
            
    for completer in completion:
        if player_dict[completer]:
            player_dict[completer] -= 1
            
    for key, value in player_dict.items():
        if value > 0:
            return key