n = int(input())
graph = [ list(map(int, input().split())) for i in range(n)]

for k in range(n): #중간 경유지
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# for all in graph:
#     print(*all) #이부분을 수정

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()