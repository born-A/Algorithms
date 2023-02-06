import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, d= map(int, input().split())

#지름길 정보 담을 그래프 0~150 까지 담을것임
#즉 0~150까지 노드번호가 매겨짐
graph = [ [] for i in range(d+1)]

for i in range(d):
    graph[i].append((i+1,1))

#최단거리 그래프
distance = [INF] * (d+1)
distance[0] = 0
for i in range(n):
    start, end, length  = map(int, input().split())  
    #이부분을 안해줘서 인덱스에러 났음
    if end > d: continue
    graph[start].append((end,length))


q = []
heapq.heappush(q,(0,0))

    
while q:
    dist , now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(distance[d])