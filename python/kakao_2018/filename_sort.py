'''
< 풀이과정 >
긴 시간동안 생각해도 이렇다 할 해결 방법이 떠오르지 않아 해설지 참조
< 키워드 - 안정 정렬>
중복된 값의 경우 입력 순서와 동일하게 유지해서 정렬 하는 것

1. list를 튜플 형태로 변환 (원본, 숫자만 추출)
2. 대/소문자 구분없이 정렬 후, 숫자만 추출한 부분으로 오름차순으로 또 정렬해서 반환
'''

import re

def solution(files):

    new_list = []
    files_len = len(files)

    for i in range(files_len):
        file = files[i] # 파일명 추출

        p = re.compile(r'([a-zA-Z.\- ]+)([0-9]\d*)([\s\w\-. ]*)') # 파일명에서 숫자 부분만 추출. 반환값은 리스트에 들어간 채로 반환된다.
        s = p.search(file)
        if s:            
            head = s.group(1)
            numbers = s.group(2)
            tail = s.group(3)
            new_list.append([head, numbers, tail])

    new_list.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = []

    for i in range(len(new_list)):
        answer.append(new_list[i][0] + new_list[i][1] + new_list[i][2])
    return answer

def main():
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
    # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

main()