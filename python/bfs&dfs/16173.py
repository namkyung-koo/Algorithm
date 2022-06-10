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
        for i in range(2):
            nx = graph[y][x + graph[cy][cx]]
            ny = graph[y + graph[cy][cx]][x]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] == False and graph[ny][nx] < N:
                    visited[ny][nx] = True
                    queue.append([ny, nx])
                elif graph[ny][nx] == -1:
                    return True

if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")

# 현재 위치 방문 표시
# 해당 인덱스의 값을 받아와서 val에 대입
# if val == -1 이면 True를 리턴
