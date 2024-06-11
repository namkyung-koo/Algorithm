'''
< 풀이과정 >
1. 반복문의 종료 조건은 len(answer) == t

'''

def convert_to_n_base(base, number):

    if number == 0:
        return [0]
    
    base_list = []

    while (number > 0):
        number, mod = divmod(number, base)
        base_list.insert(0, "0123456789ABCDEF"[mod])

    return base_list

def solution(n, t, m, p):

    answer = ''
    number = 0

    order = 1
    while True:
        base_list = convert_to_n_base(n, number)
        for i in range(len(base_list)):
            temp = base_list.pop(0)
            if order == p:
                answer += str(temp)
            if t == len(answer):
                return answer
            order += 1
            if order == m + 1:
                order = 1

        number += 1

def main():

    print(solution(2, 4, 2, 1))
    # "0111"
    print(solution(16, 16, 2, 1))
    # # "02468ACE11111111"
    print(solution(16, 16, 2, 2))
    # # "13579BDF01234567"

main()