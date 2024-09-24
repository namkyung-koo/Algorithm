from collections import Counter

'''
< 풀이과정 >
1. 일단 str1과 str2를 2글자씩 잘라서 저장한다. (문자열 자르기 메서드 필요)
2. 이 때 소문자 또는 대문자로 통일하여 저장하며 알파벳이 아닌 경우 저장하지 않는다.
3. 합집합은 중복이 허용되지 않는 자료구조 선택
4. (교집합 원소의 개수 / 합집합 원소의 개수) * 65536
'''

# 해당 함수의 시간복잡도는 O(n - 1)
def str_to_list(str, str_len):

    str_list = []
    start = 0
    while (start < str_len - 1):
        end = str_len if start == str_len - 2 else start + 2
        substr = str[start:end]
        if substr.isalpha():
            str_list.append(substr.lower())
        start += 1

    return str_list

def solution(str1, str2):

    str1_len = len(str1)
    str2_len = len(str2)

    str1_list = str_to_list(str1, str1_len)
    str2_list = str_to_list(str2, str2_len)

    # 교집합 구하기
    intersection_counter = Counter(str1_list) & Counter(str2_list)
    intersection_len = len(list(intersection_counter.elements()))

    # 합집합 구하기
    union_counter = Counter(str1_list) | Counter(str2_list)
    union_len = len(list(union_counter.elements()))

    if intersection_len == 0 and union_len == 0:
        intersection_len = 1
        union_len = 1

    return int(intersection_len / union_len * 65536)

def main():
    print(solution("FRANCE", "french"))
    print(solution("handshake", "shake hands"))
    print(solution("aa1+aa2", "AAAA12"))
    print(solution("E=M*C^2", "e=m*c^2"))

main()