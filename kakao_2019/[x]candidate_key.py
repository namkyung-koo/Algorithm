'''
< 풀이과정 >
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