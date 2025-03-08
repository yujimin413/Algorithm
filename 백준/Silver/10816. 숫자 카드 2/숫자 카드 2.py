n = int(input())
card_positive = [0 for _ in range(10000001)]
card_negative = [0 for _ in range(10000001)]
card_list = list(map(int, input().split()))

for i in range(n):
    if card_list[i] >= 0:
        card_positive[card_list[i]] += 1
    else:
        card_negative[-card_list[i]] += 1
m = int(input())
count_list = list(map(int, input().split()))
for i in range(m):
    if count_list[i] >= 0:
        print(card_positive[count_list[i]], end = ' ')
    else:
        print(card_negative[-count_list[i]], end = ' ')