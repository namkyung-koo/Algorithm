# 바이러스
N = int(input())

M = int(input())

# 0번째 인덱스는 비우고 1번째 인덱스부터 사용 (2차원 리스트)
graph = [[] for _ in range(N + 1)]

# 간선 연결
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부를 기록하는 리스트 생성
visited = [False] * (N + 1)

global cnt
cnt = 0

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            global cnt
            cnt += 1
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(cnt)