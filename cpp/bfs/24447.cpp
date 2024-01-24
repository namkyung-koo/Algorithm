// 24447번 - 알고리즘 수업 - 너비 우선 탐색 4
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <queue>

int n, m, r; // 정점의 수, 간선의 수, 시작 정점

std::vector<int> graph[100001];

long long depth[100001];

long long order[100001];

void bfs()
{
    int o = 1;

    memset(depth, -1, sizeof(depth));

    std::queue<int> q;

    q.push(r);
    depth[r] = 0, order[r] = 0;
    while (!q.empty())
    {
        int now = q.front();
        q.pop();
        for (unsigned long i = 0; i < graph[now].size(); i++)
        {
            int next = graph[now][i];
            if (depth[next] == -1)
            {
                depth[next] = depth[now] + 1;
                order[next] = ++o;
                q.push(next);
            }
        }
    }
}

void print()
{
    long long sum = 0;

    for (int i = 1; i < n + 1; i++)
        sum += depth[i] * order[i];
    std::cout << sum << std::endl;
}

int main(void)
{
    std::cin >> n >> m >> r;

    int a, b;

    for (int i = 0; i < m; i++)
    {
        std::cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i < n + 1; i++)
        std::sort(graph[i].begin(), graph[i].end());

    bfs();

    print();

    return 0;
}

/*
방문 순서:
1 2 4 3 0

노드의 깊이:
0 1 2 1 -1

1 - 2 4
2 - 3
3 - 5

   1
  /  \
 2 -  4
 |  /
 3
 |
 5

   3
  /  \
2     4
 \   /
   1

8
(1 * 0) + (2 * 1) + (3 * 2) + (4 * 1) + (5 * 3) = 13 * 15 = 28
*/
