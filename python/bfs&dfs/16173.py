# 점프왕 쩰리 (small)
import sys
from collections import deque
N = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

def bfs(y, x):
    visited[y][x] = True
    queue = deque([(y, x)])
    while queue:
        cy, cx = queue.popleft()
        dy = [cy, cy + graph[cy][cx]]
        dx = [cx + graph[cy][cx], cx]
        for i in range(2):
            ny = dy[i]
            nx = dx[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] == False and graph[ny][nx] < N:
                    visited[ny][nx] = True
                    queue.append([ny, nx])
                    if graph[ny][nx] == -1:
                        return True
if bfs(0, 0):
    print("HaruHaru")
    exit()
print("Hing")