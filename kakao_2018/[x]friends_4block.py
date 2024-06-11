'''
< 풀이과정 >
1. 가장 먼저 떠오른 방법은 bfs
2. 반복문의 종료 조건은 큐가 비었을 때
3. 지울 board의 인덱스를 저장해두고 마지막에 전부 지우고 바로 위 인덱스가 공백이 아니라면 해당 값을 가져오기
4. 오른쪽, 오른쪽아래(대각선), 아래 총 3면을 체크할 것인데 같은 캐릭터인지 어떻게 기록할건지 ?

가장 쉬운 방법은 모든 인덱스를 탐색하면서 3면을 체크하는 것. 그러나 시간복잡도는 (3n^3).

'''

from collections import deque

def solution(m, n, board):

def main():
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC",
          "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

main()
