# DFS와 BFS
from collections import deque

# N = 정점의 갯수, M = 간선의 갯수, V = 정점의 번호
N, M, V = map(int, input().split())

# 0번 인덱스는 비우고, 1번 인덱스부터 사용 (2차원 리스트)
graph = [[] for _ in range(N + 1)]

# 간선 연결

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 각 인덱스 오름차순 정렬
for i in range(len(graph)):
    graph[i].sort()

# 방문 여부를 체크하기 위한 리스트 (1차원 리스트), 모두 False로 초기화
visited = [False] * (N + 1)
res = ''

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, V, visited)
visited = [False] * (N + 1)
print()
bfs(graph, V, visited)