from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[-1] * n for _ in range(n)]
d= [(-2,-1), (-2,1), (0,-2), (0,2),(2,-1),(2,1)]
def bfs(y,x):
    q = deque()
    q.append((y,x))
    graph[y][x] 