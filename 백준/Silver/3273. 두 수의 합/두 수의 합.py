n = int(input())
arr = list(map(int, input().split())) # 입력 받기용
x = int(input())
nums = [False] * 2000001 # arr에 입력 받은 숫자에 해당하는 인덱스에 True
res = 0

for num in arr:
    nums[num] = True

for num in arr:
    if nums[x - num] == num: # '서로 다른 양의 정수' 조건 있으므로 같은 수는 pass
        nums[num] = False
        continue
    elif nums[x - num] == True:
        res += 1
        nums[num] = False

print(res)
