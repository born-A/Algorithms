INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]
   

#각 간선에 대한 정보 입력받아 그 값으로 초기화시킴
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

#플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a == b: 
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print(0)
        else:
            print(graph[a][b], end=" ")
    print()