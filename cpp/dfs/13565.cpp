// 13565번 - 침투
#include <iostream>
#include <vector>
#include <string>

#define WHITE 0
#define BLACK 1

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

void dfs(std::vector<std::vector<char>> &grid, int x, int y, std::vector<std::vector<bool>> &visited, int &row, int &col, bool &answer)
{
    if (y == row - 1)
    {
        answer = true;
        return ;
    }

    visited[y][x] = true;

    int nx, ny, dir;

    for (dir = 0; dir < 4; dir++)
    {
        ny = y + dy[dir];
        nx = x + dx[dir];

        if ((nx >= 0 && nx < col) && (ny >= 0 && ny < row))
        {
            if (grid[ny][nx] == WHITE && visited[ny][nx] == false)
            {
                dfs(grid, nx, ny, visited, row, col, answer);
                if (answer) return ;
            }
        }
    }
}

int main(void)
{
    int m, n;

    std::cin >> m >> n;

    // 2차원 vector 생성
    std::vector<std::vector<char>> grid(m, std::vector<char>(n));

    int i, j;
    // 각 줄의 데이터 입력
    for (i = 0; i < m; i++)
    {
        std::string row_input;
        std::cin >> row_input;
        for (j = 0; j < n; j++)
            grid[i][j] = row_input[j] - '0';
    }

    std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));

    bool answer = false;

    for (i = 0; i < n; i++)
    {
        dfs(grid, i, 0, visited, m, n, answer);
        if (answer ==  true)
        {
            std::cout << "YES" << std::endl;
            return 0;
        }
    }
    std::cout << "NO" << std::endl;

    return 0;
}
