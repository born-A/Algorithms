n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])
    arr = sorted(arr, key=lambda a: a[1])
    arr = sorted(arr, key=lambda a: a[0])
last = 0
cnt = 0
for i, j in arr:
    if i >= last:
        cnt += 1
        last = j
print(cnt)