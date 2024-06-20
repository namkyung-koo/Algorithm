'''
< 풀이과정 >
유일성 체크를 쉽게 하기 위해 자료구조 set(중복을 허용치 않음)을 사용
속성을 나타내는 1 <= column <= 8. 8비트 캐릭터 변수 하나로 비트마스킹.
'''

def solution(relation):
    new = []
    for i in range(len(relation)):
        new.append(relation[i][0])

    s = set(new)
    return s

def main():
    print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
    # 2(후보 키의 개수)

main()