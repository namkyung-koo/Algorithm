'''
< 풀이과정 >
[조건] : 개발언어/직군/경력/소울푸드 + [코테점수]

반복문 돌면서 공백을 기준으로 info를 split해 이차원 리스트로 변환 - O(n)
반복문 돌면서 공백을 기준으로 query를 split해 이차원 리스트로 변환 - O(n)
단순 비교를 통해 언어 - ... - 점수

딕셔너리[조건] = 코테점수

누적시간 : 1시간 38분 -> 질문하기 검색함
1. info에 없는 조건들이 query에는 있을 수 있다.
2. info 50,000개 * query 100,000개 = 50억개 => 해시 테이블 사용
3. 점수 비교할 때도 선형 탐색 대신 더 빠른 탐색법 사용(예. 이진탐색)
'''

def atoi(str):
    n = ""
    for i in range(len(str)):
        if str[i].isdigit() == False:
            continue
        n += str[i]

    return int(n)

def solution(info, query):
    
    info_dict = dict()
    for i in range(len(info)):
        l = info[i].split(' ')
        str = ""
        for i in range(4):
            str += l[i]
        info_dict[str] = int(l[4])

    query_dict = dict()
    new_l = []
    for i in range(len(query)):
        l = query[i].split(' and ')
        str = ""
        for i in range(4):
            if l[i] == '-':
                continue
            if i == 3:
                new_l = l[i].split(' ')
                if new_l[0] == '-':
                    break
                str += new_l[0]
                break
            str += l[i]

        query_dict[str] = int(new_l[1])

    answer = []

    for query_key in query_dict.keys():
        cnt = 0
        for info_key in info_dict.keys():
            if info_key.find(query_key) != -1 and info_dict[info_key] >= query_dict[query_key]:
                cnt += 1
        answer.append(cnt)
    return answer

def main():
    print(solution(["java backend junior pizza 150",\
                    "python frontend senior chicken 210",\
                        "python frontend senior chicken 150",\
                            "cpp backend senior pizza 260",\
                                "java backend junior chicken 80",\
                                    "python backend senior chicken 50"], \
                                        \
                                        ["java and backend and junior and pizza 100",\
                                         "python and frontend and senior and chicken 200",\
                                            "cpp and - and senior and pizza 250",\
                                                "- and backend and senior and - 150",\
                                                    "- and - and - and chicken 100",\
                                                        "- and - and - and - 150"]))
    # [1,1,1,1,2,4]

main()