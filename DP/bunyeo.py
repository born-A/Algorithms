dic = {}
def apt(k,n):
    if k == 0:
        return n
    else:
        list=[]
        for i in range(1,n+1):
            list.append(i)
        
        dic[k-1] = list
        print(dic[k-1])
        realapt = 0
        for j in range(n):
            realapt += dic[k-1][j]
        return realapt

test = int(input())
for i in range(test):
    k = int(input())
    n = int(input())
    print (apt(k,n))



