'''
< 풀이과정 >
1. key = 단어(대문자), value = 색인번호로 딕셔너리에 저장.
2. msg의 길이만큼 반복문을 돌면서 체크한다.
첫번째 현재 글자 + 다음 글자가 딕셔너리에 있는지 체크. 없으면 색인번호 27부터 추가
'''

def solution(msg):

    uppercase_dict = dict()
    # 딕셔너리 초기화
    for order in range(1, 27):
        uppercase_dict[chr(order + 64)] = order

    order = 27
    answer = []
    msg_len = len(msg)

    index = 0
    while index < msg_len:
        cur = msg[index]
        # msg의 마지막 인덱스일 때
        if index == msg_len - 1:
            answer.append(uppercase_dict[cur])
            break
        # 마지막 인덱스가 아닐 때
        else:
            next = msg[index + 1]
            new = uppercase_dict.get(cur + next)
            # 현재 + 다음 글자가 없을 때
            if new == None:
                uppercase_dict[cur + next] = order
                order += 1
                answer.append(uppercase_dict[cur])
            # 현재 + 다음 글자가 있을 때, 반복문을 돌면서 최대 길이를 구한다.
            else:
                answer.append(new)
                if index + len(cur + next) < msg_len:
                    index += len(cur + next)
                    cur = msg[index]
                    next = msg[index + 1]
                    answer.append(uppercase_dict[next])
                    new = uppercase_dict.get(cur + next)

                uppercase_dict[cur + next] = order
                order += 1
            index += 1

    return answer

def main():
    print(solution("KAKAO"))
    # [11, 1, 27, 15]
    print(solution("TOBEORNOTTOBEORTOBEORNOT"))
    # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    print(solution("ABABABABABABABAB"))
    # [1, 2, 27, 29, 28, 31, 30]

main()