import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다

def dfs(v):
    visited[v] = True
    next = numbers[v] #다음 방문 장소
    if not visited[next]:
        dfs(next)


for i in range(int(input())):
    n = int(input())
    count = 0
    numbers = [0] + list(map(int,input().split()))
    visited = [True] + [False] * n
    for j in range(1,n+1):
        if not visited[j]: #방문 안했을때
            dfs(j) #DFS 실행
            count += 1 
    print(count)

