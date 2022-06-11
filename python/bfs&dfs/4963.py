# 섬의 개수
from collections import deque
import sys

while True:
    # w = 지도의 너비, h = 지도의 높이
    w, h = map(int, sys.stdin.readline().split())
    # 종료 조건
    if w == 0 and h == 0:
        break
    # 1은 섬, 0은 바다
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    
    visited = [[False] * w for _ in range(h)]

    Is = 0

    # 위에서부터 시계방향으로 체크
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    def bfs(y, x):
        queue = deque([(y, x)])
        while queue:
            cy, cx = queue.popleft()
            for i in range(8):
                ny = cy + dy[i]
                nx = cx + dx[i]
                # 상하좌우, 대각선 체크
                if 0 <= nx < w and 0 <= ny < h:
                    if visited[ny][nx] == False and graph[ny][nx] == 1:
                        visited[ny][nx] = True
                        queue.append([ny, nx])

    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and graph[i][j] == 1:
                visited[i][j] = True
                bfs(i, j)
                Is += 1
                
    print(Is)