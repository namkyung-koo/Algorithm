'''
[ 주차 요금 계산 ]
< 풀이과정 >
1. records를 반복문으로 돌면서 공백(' ')을 기준으로 split한다.
2. split_list[2] == "IN"이면 입출차기록 딕셔너리{차량번호 : 출입시간}에 삽입.
3. split_list[2] == "OUT"이면 입출차기록 딕셔너리에서 같은 차량 번호의 출입 기록을 가져와 계산한다.
4. {차량번호 : 누적시간} 딕셔너리에 삽입한다.
5. 차량번호(key)를 기준으로 오름차순으로 청구할 주차 요금을 answer 리스트에 담아 return.

총 시간 : 1시간 27분, 딕셔너리 변수 3개 사용
'''

import math

def calculate_time(past, now):
    past_list = past.split(':')
    past_time = int(past_list[0]) * 60 + int(past_list[1])

    now_list = now.split(':')
    now_time = int(now_list[0]) * 60 + int(now_list[1])
    return now_time - past_time

def charge_parking_fee(fees, total_time):
    if total_time < fees[0]:
        return fees[1]
    fee = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]

    return fee

def solution(fees, records):

    parking_log = dict()
    is_parking = dict()
    car_total_usage_time = dict()
    for i in range(len(records)):
        l = records[i].split(' ')
        if l[2] == "IN":
            parking_log[l[1]] = l[0]
            is_parking[l[1]] = True
        elif l[2] == "OUT":
            if l[1] in car_total_usage_time:
                car_total_usage_time[l[1]] = car_total_usage_time[l[1]] + calculate_time(parking_log[l[1]], l[0])
            else:
                car_total_usage_time[l[1]] = calculate_time(parking_log[l[1]], l[0])
            is_parking[l[1]] = False

    # 출차 기록이 없는 차량의 경우 23:59 출차로 기록
    for key, value in is_parking.items():
        if value == True:
            if key in car_total_usage_time:
                car_total_usage_time[key] = car_total_usage_time[key] + calculate_time(parking_log[key], "23:59")
            else:
                car_total_usage_time[key] = calculate_time(parking_log[key], "23:59")
            is_parking[key] = False

    sorted_dict = dict(sorted(car_total_usage_time.items()))
    answer = []

    for key, value in sorted_dict.items():
        answer.append(charge_parking_fee(fees, value))

    return answer

def main():

    print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
    # [14600, 34400, 5000]
    print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
    # [0, 591]

    print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
    # [14841]

main()