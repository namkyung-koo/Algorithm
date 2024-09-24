'''
< 풀이과정 >
파이썬의 조합과 딕셔너리를 사용
총 59분 30초 걸림
'''

from itertools import combinations

def list_to_dict(orders_dict, orders, course):

    orders_len = len(orders)
    if (orders_len < course):
        return orders_dict

    orders_list = list(map(''.join, combinations(orders, course)))

    for i in orders_list:
        if i in orders_dict:
            orders_dict[i] += 1
        else:
            orders_dict[i] = 1

    return orders_dict

def solution(orders, course):

    answer = []
    for i in range(len(course)):
        orders_dict = dict()
        for j in range(len(orders)):
            # 문자열 내부에서도 오름차순으로 정렬을 한 번 거친다.
            orders[j] = ''.join(sorted(orders[j]))
            orders_dict = list_to_dict(orders_dict, orders[j], course[i])
        sorted_list = sorted(orders_dict.items(), key=lambda x:x[1], reverse=True)
        # 주문 횟수가 가장 많은 코스 메뉴 뽑기
        if sorted_list != []:
            max_course = sorted_list[0][1]
        for k in range(len(sorted_list)):
            if sorted_list[k][1] != 1 and sorted_list[k][1] == max_course:
                answer.append(sorted_list[k][0])
    answer.sort()

    return answer

def main():
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
    # ["AC", "ACDE", "BCFG", "CDE"]
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
    # ["ACD", "AD", "ADE", "CD", "XYZ"]
    print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
    # ["WX", "XY"]

main()