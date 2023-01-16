n = int(input())
arr_min = 0
arr_max = 0
for i in range(n):
    arr = list(map(int,input().split()))
    arr.remove(min(arr))
    arr.remove(max(arr))
    if( (max(arr)-min(arr)) >= 4):
        print("KIN")
    else :
        print(sum(arr))