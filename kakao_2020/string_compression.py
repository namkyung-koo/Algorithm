'''
< 풀이과정 >
len(s) == 24일 때, 
단위 == 10, *[10]****, 길이는 15
단위 == 11, *[11]**, 길이는 14
단위 == 12, *[12], 길이는 13
단위가 문자열 길이의 1/2를 넘는 순간, 압축을 할 수 없다. (단위 == 13, 24)
'''

def solution(s):

    s_len = len(s)

    answer = []
    answer.append(s_len)

    # 큰 반복문은 문자열 길이의 1/2보다 작거나 같을 때까지만 돈다.
    for split_length in range(1, s_len // 2 + 1):
        str = ""
        idx = 0
        cnt = 0
        base_string = s[idx:split_length]
        while idx < s_len:
            if base_string == s[idx:split_length + idx]:
                cnt += 1
            else:
                str += f'{cnt}{base_string}' if cnt != 1 else base_string
                cnt = 1
                base_string = s[idx:split_length + idx]
            idx += split_length
        str += f'{cnt}{base_string}' if cnt != 1 else base_string
        answer.append(len(str))

    return min(answer)

def main():
    print(solution("aabbaccc"))
    # 7
    print(solution("ababcdcdababcdcd"))
    # 9
    print(solution("abcabcdede"))
    # 8
    print(solution("abcabcabcabcdededededede"))
    # 14
    print(solution("xababcdcdababcdcd"))
    # 17
    
main()