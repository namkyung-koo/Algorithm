// 15559번 - 내 선물을 받아줘
#include <iostream>
#include <vector>

enum direct
{
    WEST,
    NORTH,
    EAST,
    SOUTH
};

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};
int n, m, i, j, gift = 0, circle = 0; // 세로 길이, 가로 길이

void dfs(std::vector<std::vector<char>> &map, int y, int x, std::vector<std::vector<int>> &visited)
{
    visited[y][x] = circle;

    int ny, nx;

    switch (map[y][x])
    {
    case 'W':
        ny = y + dy[WEST];
        nx = x + dx[WEST];
        break;
    case 'N':
        ny = y + dy[NORTH];
        nx = x + dx[NORTH];
        break;
    case 'E':
        ny = y + dy[EAST];
        nx = x + dx[EAST];
        break;
    case 'S':
        ny = y + dy[SOUTH];
        nx = x + dx[SOUTH];
        break;
    }

    if ((ny >= 0 && ny < n) && (nx >= 0 && nx < m))
    {
        if (visited[ny][nx] == false)
            dfs(map, ny, nx, visited);
        else if (visited[ny][nx] != false && visited[ny][nx] == circle)
            gift++;
    }
}

int main(void)
{
    std::cin >> n >> m;

    std::vector<std::vector<char>> map(n, std::vector<char>(m, 0));

    std::string input;

    for (i = 0; i < n; i++)
    {
        std::cin >> input;
        for (j = 0; j < m; j++)
            map[i][j] = input[j];
    }

    std::vector<std::vector<int>> visited(n, std::vector<int>(m, false));

    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            if (visited[i][j] == false)
            {
                ++circle;
                dfs(map, i, j, visited);
            }

    std::cout << gift << std::endl;

    return 0;
}

/*
어떤 서클이 생기면 선물 + 1
이 때, 서클이라함은 이미 방문하여 visited == true인 경우
문제의 핵심은 서클
기존의 서클 요소들은 visited != false로 다 건너뛰고
새로운 서클의 요소가 될 수 있는 녀석들 체크할 때, visited != false면 결국 이전 서클과 같다는 뜻
반대로 visited == false면 새로운 서클이 형성되었다는 뜻 ?
*/