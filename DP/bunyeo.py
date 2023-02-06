test = int(input())

for i in range(test):
    k = int(input())
    n = int(input())
    floor0 = [x for x in range(1,n+1)]
    for k in range(k): # 층 수 만큼 반복
        for n in range(1,n): #n 은 인덱스
            floor0[n] += floor0[n-1]
    print(floor0[-1])




