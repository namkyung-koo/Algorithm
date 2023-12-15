// 18352번 - 특정 거리의 도시 찾기
#include <iostream>
#include <vector>
#include <queue>

int n, m, k, x; // 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호

void bfs(std::vector<std::vector<int>> &graph, int now, std::vector<std::vector<int>> &dist)
{
    for (int i = 0; i < graph[now].size(); i++)
    {
        int next = graph[now][i];

        dist[now][next]++;

        std::cout << "now : " << now << ", next : " << next << ", dist : " << dist[now][next] << std::endl;

        if (n < dist[now][next])
            dist[now][next] = n + 1;

        bfs(graph, next, dist);
    }
}

int main(void)
{
    std::cin >> n >> m >> k >> x;

    std::vector<std::vector<int>> graph(n + 1);

    int i, a, b;

    for (i = 0; i < m; i++)
    {
        std::cin >> a >> b;

        graph[a].push_back(b);
    }

    std::vector<std::vector<int>> dist(n + 1, std::vector<int>(n + 1, 0));

    bfs(graph, x, dist);

    std::queue<int> queue;

    for (i = 1; i < dist[x].size(); i++)
        if (dist[x][i] == k)
            queue.push(i);

    if (queue.empty())
        std::cout << -1 << std::endl;
    else
    {
        while (!queue.empty())
        {
            std::cout << queue.front() << std::endl;
            queue.pop();
        }
    }

    return 0;
}

/*
4 4 2 1
1 2
1 3
2 3
2 4

1 - 2 - 4
  \ |
    3

출발 도시의 번호만 체크
1 2 3 => 2
1 2 4 => 2
1 3 => 1 (최단 거리로 갱신)
1 - 2 1
1 - 3 1
2 - 3 1
2 - 4 1
*/