# 전화번호 목록

"""
< 풀이과정 >
키워드 검색 : python 특정 문자열 포함 여부, python 특정 문자열 시작(접두사)
이중 반복문으로 구현 시 8,9,14와 테스트 3,4를 통과할 수 없었다.

가장 짧은 전화번호 길이까지 다 잘라서 저장?
해당 키를 이용하여 O(1) 시간 복잡도를 가지며 탐색

시간복잡도 "O(n^2)"를 줄일 수 있는 방법이 생각 나지 않아서 테스트19와 효율성 테스트 3,4를 통과하지 못했다.

연산 1억 번에 1초라고 생각하기.
"""

def solution(phone_book):
    
    for i in range(len(phone_book) - 1):
        min_number = phone_book[i]
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].startswith(min_number):
                return False
    return True