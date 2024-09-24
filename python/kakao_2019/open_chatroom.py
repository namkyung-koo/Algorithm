'''
< 풀이과정 >
딕셔너리 사용.
유저 아이디(key) - 닉네임(value)
"Enter" - 딕셔너리에 등록
"Change" - 딕셔너리 해당 키의 값 변경
'''

def translate_record(record, d):
    
    record_len = len(record)
    result = []
    
    for i in range(record_len):
        first_word = record[i].split()[0]
        user_id = record[i].split()[1]
        
        if first_word == "Enter":
            result.append(f"{d[user_id]}님이 들어왔습니다.")
        elif first_word == "Leave":
            result.append(f"{d[user_id]}님이 나갔습니다.")
            
    return result
            

def solution(record):
    
    d = dict()
    record_len = len(record)

    for i in range(record_len):
        first_word = record[i].split()[0]
        user_id = record[i].split()[1]

        if first_word == "Enter" or first_word == "Change":
            nickname = record[i].split()[2]
            d[user_id] = nickname

    answer = translate_record(record, d)
    return answer

def main():
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
    # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

main()