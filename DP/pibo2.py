def pibo(num):
        pibolist = []
        for i in range(num+1):
            if i == 0:
                pibolist.append(i)
            if (i == 1):
                pibolist.append(i)
            if (i >= 2):
                pibosum = 0
                pibosum = pibolist[i-1] + pibolist[i-2]
                pibolist.append(pibosum)

        return pibolist[num]

num = int(input())
print(pibo(num))