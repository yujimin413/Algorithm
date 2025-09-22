numbers = list(input())
arr = [0] * 10 # 0~9

for num in numbers:
    arr[int(num)] += 1
    if arr[6] - arr[9] > 1:
        arr[6] -= 1
        arr[9] += 1
    elif arr[9] - arr[6] > 1:
        arr[6] += 1
        arr[9] -= 1

print(max(arr))
