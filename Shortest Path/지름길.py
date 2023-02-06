INF = int(1e9)

n, d= map(int, input().split())

graph = [ [] for i in range(n+1)]
for i in range(n):
    a, b, c = map(int, input().splt())
