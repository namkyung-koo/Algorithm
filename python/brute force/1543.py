# 문서 검색
str = input()
find = input()

cnt = 0

i = 0
j = 0

while i < len(str):
    j = 0
    while j < len(find) and i + j < len(str) and str[i + j] == find[j]:
        if j == len(find) - 1:
            cnt += 1
            i += j
            break        
        j += 1
    i += 1
print(cnt)

# to_find와 str을 각각 인덱스 비교
# 다르면 바로 break. 그렇지 않고 to_find와 끝까지 같으면 cnt++
# to_find의 인덱스는 계속 0으로 초기화 해줘야함
# aabb / ab 인 경우
# a / b 인 경우
# ababaa / abaa 인 경우