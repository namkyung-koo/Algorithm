// 18352번 - 특정 거리의 도시 찾기
#include <iostream>
#include <vector>

void bfs(std::vector<std::vector<int>> &info, int start, std::vector<std::vector<int>> &dist)
{
    std::vector<int>::iterator it = info[start].begin();

    dist[start][*it] += 1;

    
}

int main(void)
{
    int n, m, k, x; // 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호

    std::cin >> n >> m >> k >> x;

    std::vector<std::vector<int>> info(n + 1);

    int i, a, b;

    for (i = 0; i < m; i++)
    {
        std::cin >> a >> b;

        info[a][b] = 1;
    }

    std::vector<std::vector<int>> dist(n + 1);

    bfs(info, x, dist);



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