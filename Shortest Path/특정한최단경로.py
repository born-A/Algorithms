import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

m1, m2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, [0,start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
                continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost,i[0]])

    return distance

d_start = dijkstra(1)
d_m1 = dijkstra(m1)
d_m2 = dijkstra(m2)

result = min(d_start[m1] + d_m1[m2] + d_m2[n], d_start[m2] + d_m2[m1] + d_m1[n])

print(result)