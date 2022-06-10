# 연결 요소의 개수
import sys
# 재귀 깊이 한도를 1000 -> 10000으로 변경
sys.setrecursionlimit(10**4)
# 시간 초과 문제를 해결하기 위해 사용
input = sys.stdin.readline
# N = 점점의 개수, M = 간선의 개수
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
print(graph)
cnt = 1

def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        cnt += 1

print(cnt)