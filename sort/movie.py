n,l, h = map(int, input().split())
arr = sorted(list(map(int,input().split())))
arr_sum = sum(arr[l:n-h])
avg = arr_sum / (n-l-h)
print(avg)