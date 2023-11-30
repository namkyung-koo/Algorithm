// 24482번 알고리즘 수업 - 깊이 우선 탐색 4
#include <functional>
#include <algorithm>
#include <iostream>
#include <vector>

#define NOT_VISITED -1

void dfs(std::vector<std::vector<int> > &vertex, std::vector<int> &visited, int r, int &depth)
{
	int ret = depth;

	visited[r] = ret;
	ret++;

	for (int next : vertex[r])
		if (visited[next] == false)
			dfs(vertex, visited, next, ret);
}

int main(void)
{
	std::ios_base::sync_with_stdio(false); // 입출력 속도 향상
	std::cin.tie(NULL);

	int n, m, r; // 정점의 수, 간선의 수, 시작 정점

	std::cin >> n >> m >> r;

	std::vector<std::vector<int> > vertex(n + 1);

	std::vector<int> visited(n + 1, 0);

	int i, u, v, depth = 1;

	for (i = 0; i < m; i++)
	{
		std::cin >> u >> v;
		vertex[u].push_back(v);
		vertex[v].push_back(u);
	}

	for (auto &row : vertex)
		std::sort(row.begin(), row.end(), std::greater<int>());

	dfs(vertex, visited, r, depth);

	for (i = 1; i < n + 1; i++)
		std::cout << (visited[i] == false ? -1 : visited[i] - 1) << '\n';

	return 0;
}

/*

5 5 1
1 4
1 2
2 1
2 4
1 3

0
2
1
1
-1

*/