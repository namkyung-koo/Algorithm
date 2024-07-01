'''
[ 두 큐의 합 같게 만들기 ]
< 풀이과정 >
1. 무조건 두 큐의 원소의 합 / 2(sum)가 되도록 해야한다.
2. sum보다 원소의 합이 큰 배열은 pop(0) 후 해당 원소를 다른 배열 맨 뒤에 삽입(append).
3. 크기 비교
'''

from collections import deque

def solution(queue1, queue2):

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    result = (queue1_sum + queue2_sum) // 2
    deque1 = deque()
    deque2 = deque()
    # 한 개의 원소가 result 보다 클 때 -1을 반환
    for e in queue1:
        if e > result:
            return -1
        deque1.append(e)

    for e in queue2:
        if e > result:
            return -1
        deque2.append(e)

    deque1_sum = sum(deque1)
    deque2_sum = sum(deque2)
    n = len(deque1) + len(deque2)
    answer = 0

    for _ in range(n * 2):
        if result > deque1_sum:
            data = deque2.popleft()
            deque2_sum -= data
            deque1.append(data)
            deque1_sum += data
            answer += 1
        elif result > deque2_sum:
            data = deque1.popleft()
            deque1_sum -= data
            deque2.append(data)
            deque2_sum += data
            answer += 1
        if result == deque1_sum and result == deque2_sum:
            break
    # 모든 원소의 개수 * 2만큼 반복문 다 돌고나서도 같지 않으면 더 이상 돌지 않도록 한다.
    if result != deque1_sum or result != deque2_sum:
        return -1
    return answer

def main():
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
    # 2
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
    # 7
    print(solution([1, 1], [1, 5]))
    # -1
    print(solution([10, 5, 1], [2, 2, 2]))
    # -1

main()