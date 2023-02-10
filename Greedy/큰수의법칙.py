n, m, k = map(int, input().split())
nList = list(map(int, input().split()))

nList.sort()
first = nList[n-1]
second = nList[n-2]

maxsum = 0

while True:
    for i in range(k):
        if m == 0: break
        maxsum += first
        m -= 1
    if m == 0: break
    maxsum += second
    m -= 1

print(maxsum)