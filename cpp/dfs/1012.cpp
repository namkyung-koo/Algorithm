// 1012번 유기농 배추
#include <iostream>

#define CABBAGE 1

int cx[4] = {-1, 0, 1, 0};
int cy[4] = {0, 1, 0, -1};

void bfs(bool **&farm, bool **&visited, int &x, int &y, int &m, int &n)
{
	visited[y][x] = true;

	int dir, nx, ny;

	for (dir = 0; dir < 4; dir++)
	{
		ny = y + cy[dir];
		nx = x + cx[dir];

		if ((ny >= 0 && ny < n) && (nx >= 0 && nx < m) && visited[ny][nx] == false && farm[ny][nx] == CABBAGE)
			bfs(farm, visited, nx, ny, m, n);
	}
}

int main(void)
{
	int t; // 테스트 케이스 개수

	std::cin >> t;

	int m, n, k; // 배추밭의 가로길이, 세로길이, 배추의 위치의 개수

	bool **farm;
	bool **visited;

	int i, j;

	for (i = 0; i < t; i++)
	{
		std::cin >> m >> n >> k;

		farm = new bool *[n];
		visited = new bool *[n];

		for (j = 0; j < n; j++)
		{
			farm[j] = new bool[m]();
			visited[j] = new bool[m]();
		}

		int x, y, worm = 0; // 배추의 가로 위치, 배추의 세로 위치
		for (j = 0; j < k; j++)
		{
			std::cin >> x >> y;
			farm[y][x] = CABBAGE;
		}

		for (y = 0; y < n; y++)
		{
			for (x = 0; x < m; x++)
			{
				if (farm[y][x] == CABBAGE && visited[y][x] == false)
				{
					bfs(farm, visited, x, y, m, n);
					worm++;
				}
			}
		}
		std::cout << worm << std::endl;

		for (j = 0; j < n; j++)
		{
			delete[] farm[j];
			delete[] visited[j];
		}
		delete[] farm;
		delete[] visited;
	}

	return 0;
}

/*

	 0 1 2 3 4 5 6 7 8 9
	 | | | | | | | | | |
0 -> 1 1 0 0 0 0 0 0 0 0
1 -> 0 1 0 0 0 0 0 0 0 0
2 -> 0 0 0 0 1 0 0 0 0 0
3 -> 0 0 0 0 1 0 0 0 0 0
4 -> 0 0 1 1 0 0 0 1 1 1
5 -> 0 0 0 0 1 0 0 1 1 1
6 -> 0 0 0 0 0 0 0 1 1 1
7 -> 0 0 0 0 0 0 0 0 0 0


     0 1 2 3 4
     | | | | |
0 -> 0 0 0 0 1
1 -> 0 0 0 0 0
2 -> 1 1 1 1 1

*/