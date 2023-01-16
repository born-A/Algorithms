import itertools

n = int(input())
arr = [i for i in range(n)]
cases = list(itertools.combinations(arr, n//2))
min_sum = n * n * 100

for i in range(n):
   arr[i] = list(map(int, input().split()))

for case_start in cases:
    sum_start = 0
    sum_link = 0
    for i in case_start:
        for j in case_start:
            if i == j: continue
            sum_start += arr[i][j]
    case_link = [i for i in range(n) if i not in case_start]
    for i in case_link:
        for j in case_link:
            if i == j: continue
            sum_link += arr[i][j]
    min_sum = min(min_sum,abs(sum_start - sum_link))
    
print(min_sum)