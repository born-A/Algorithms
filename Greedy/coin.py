n, k = map(int, input().split())
count = 0

data = []
for i in range(0,n):
    number = int(input())
    data.append(number)

data.sort(reverse=True)
for coin in data:
    count = int(count + (k/coin))
    k %= coin
    
print(count)