arr = list(input())
res = [0] * 26 # a~z

for char in arr:
    res[ord(char) - 97] += 1 
print(*res)
