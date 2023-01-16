def dfs(n):
    #시작노드 방문 처리
    visited[n] = True
    #시작노드 출력
    print(n, end=' ')
    #인접 노드 방문 하였는지 확인
    for i in graph[n]:
        if visited[i] == True:
            continue
        #방문하지 않았으면
        else:
            visited[i] = True
            dfs(i)

def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


from collections import deque
n, m, v = (map(int, input().split()))
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()   
print(graph)

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)