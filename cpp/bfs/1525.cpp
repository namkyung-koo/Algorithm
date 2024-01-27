// 1525번 - 퍼즐
#include <iostream>
#include <utility>
#include <queue>
#include <set>

int grid[3][3] = {0};

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

std::string str = "";

std::set<std::string> unique_str;

int x, y, pos = 0;

int bfs()
{
    std::queue<std::pair<std::string, int>> q;

    std::pair<std::string, int> cur = {str, 0};

    unique_str.insert(str);
    q.push(cur);

    while(!q.empty())
    {
        std::string tmp_str = q.front().first;
        int tmp_cnt = q.front().second;

        pos = tmp_str.find("0");
        x = pos / 3, y = pos % 3;
        q.pop();

        if (tmp_str == "123456780")
            return tmp_cnt;

        for (int dir = 0; dir < 4; dir++)
        {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx > -1 && nx < 3 && ny > -1 && ny < 3)
            {
                std::string next = tmp_str;
                std::swap(next[x * 3 + y], next[nx * 3 + ny]);

                if (unique_str.find(next) == unique_str.end())
                {
                    unique_str.insert(next);
                    q.push(std::make_pair(next, tmp_cnt + 1));
                }
            }
        }
    }
    return -1;
}

int main(void)
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            std::cin >> grid[i][j];
            str += std::to_string(grid[i][j]);
        }
    }

    std::cout << bfs() << std::endl;

    return 0;
}

/*
아래, 오른쪽으로만 이동이 가능하다고 일단 가정.
위 , 왼쪽 이동도 고려해야함.

참고 : https://chat.openai.com/c/0d8a6689-cbee-4986-96ef-fb7b2a6568ad

< 예제 1 >
4 1 3
2 0 5
7 8 6

과정
4 1 3   4 1 3   0 1 3   1 0 3   1 2 3
2 0 5   0 2 5   4 2 5   4 2 5   4 0 5
7 8 6   7 8 6   7 8 6   7 8 6   7 8 6
(시작)
1 2 3   1 2 3
4 5 0   4 5 6
7 8 6   7 8 0
        (완료)
정답 : 6

< 예제 2 >
2 3 5
1 8 0
4 7 6

과정
2 3 5   2 3 0   2 0 3   0 2 3   1 2 3
1 8 0   1 8 5   1 8 5   1 8 5   0 8 5
4 7 6   4 7 6   4 7 6   4 7 6   4 7 6
(시작)
1 2 3   1 2 3   1 2 3   1 2 3   1 2 3
4 8 5   4 8 5   4 0 5   4 5 0   4 5 6
0 7 6   7 0 6   7 8 6   7 8 6   7 8 0
                                (완료)
정답 : 9
*/