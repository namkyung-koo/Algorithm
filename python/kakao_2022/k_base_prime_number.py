'''
[ k진수에서 소수 개수 구하기 ]
< 풀이과정 >
1. n -> k진수로 변환
2. 숫자 앞자리부터 소수인지 확인(형태는 0p, p0, 0p0, p)
3. 반복문 돌되 0이 나오기 전까지 str += n[i], 0이 나오는 순간 str => int형으로 변환 => 소수 판별

총 시간 : 48분 + 진수 변환, 소수 판별 인터넷 서칭
'''

def convert_to_k_base(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def is_prime_number(x):
    i = 2
    integer_x = int(x)
    while i * i <= integer_x:
        if integer_x % i == 0:
            return False
        i += 1
    return True

def solution(n, k):

    string_number = convert_to_k_base(n, k)
    string_list = string_number.split('0')
    answer = 0

    for str in string_list:
        if str == '' or int(str) < 2:
            continue
        if is_prime_number(str) == True:
            answer += 1

    return answer

def main():
    print(solution(437674, 3))
    # 3
    print(solution(110011, 10))
    # 2
    print(solution(797161, 3))

main()