from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(n) ]

visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
maxv = 0

def bfs(y, x):
    q = deque()
    q.append([y, x])
    graph[y][x] = 0
    cnt = 1
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            #맵을 벗어나면 안됨. 다만 0은 가능. 왜냐하면 컴퓨터에서 0은
            #초기 시작 위치를 뜻함. list[0]은 리스트의 첫 번째 요소를 뜻함.
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == False and graph[ny][nx] == 1:
                    cnt += 1
                    graph[ny][nx] = 0
                    visited[ny][nx] == True
                    q.append([ny, nx])
                    
    return cnt



res = []
for j in range(n):

    for i in range(m):
        # 그래프가 1 축 그림이면, visited == false 즉 방문한 적이 없으면.
        if graph[j][i] == 1 and visited[j][i] == False:
            visited[j][i] == True
            #
            cnt += 1
            maxv = max(maxv, bfs(j, i))


print(cnt)
print(maxv)