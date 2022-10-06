n = int(input())
roadLen = list(map(int, input().split()))
cost = list(map(int, input().split()))

sum = cost[0] * roadLen[0]
min = cost[0]
distance = 0

for i in range(1,n-1):
    if cost[i] < min:
        sum += min * distance
        distance = roadLen[i]
        min = cost[i]
    else:
        distance += roadLen[i]
    if i == n - 2:
        sum += min * distance

print(sum)
