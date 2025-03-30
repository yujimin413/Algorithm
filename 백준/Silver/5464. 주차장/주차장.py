import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

cost_dict = dict() # 키 - 주차 공간 인덱스, 값 - 주차 요금
car_weight_dict = dict() # 키 - 차량 번호, 값 - 무게
parking_list = dict() # 키 - 차량 번호, 값 - 주차 공간 인덱스
is_parked = [False] * n # 주차 여부
parking_slot = [0] * n # 주차공간에 차량번호 저장 (0 -> 빈자리)
waiting_deque = deque()

for i in range(n):
    cost_dict[i] = int(input().strip())
# print(cost_dict)

for i in range(m):
    car_weight_dict[i + 1] = int(input().strip())
# print(car_weight_dict)

total_fee = 0
for i in range(2 * m):
    # print(f'지금은 {i}번째')
    car_num = int(input().strip()) # 차랑번호
    if car_num > 0: # in
        for i in range(n):
            parked = False
            if not is_parked[i]:
                is_parked[i] = True
                # print(f'car_num {car_num} IN')
                parking_slot[i] = car_num
                parking_list[car_num] = i
                parked = True
                break
        if not parked:
            waiting_deque.append(car_num)
            # print(f'{car_num} to waiting_queue')
        # print(parking_list)
        # print(waiting_deque)
    elif car_num < 0: # out
        car_num *= -1
        slot_idx = parking_list[car_num]
        total_fee += car_weight_dict[car_num] * cost_dict[slot_idx]
        is_parked[slot_idx] = False
        parking_slot[slot_idx] = 0
        del parking_list[car_num]
        # print(f'car_num {car_num} out')
        # print(parking_list)
        # print(waiting_deque)
        # print(is_parked)
        while waiting_deque and False in is_parked:
            next_car = waiting_deque.popleft()
            # print(f'car_num {next_car} IN')
            parking_list[next_car] = slot_idx
            is_parked[slot_idx] = True
            parking_slot[slot_idx] = next_car
        # print(parking_list)
        # print(waiting_deque)
print(total_fee)
