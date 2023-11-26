// 24480번 알고리즘 수업 - 깊이 우선 탐색 2
#include <iostream>
#include <functional> // std::greater를 위해 필요
#include <algorithm>
#include <vector>

void dfs(std::vector<std::vector<int>> &vec, std::vector<int> &visited, int &order, int r)
{
	visited[r] = order;
	order++;

	for (int next_node : vec[r])
	{
		if (!visited[next_node])
			dfs(vec, visited, order, next_node);
	}
}

int main(void)
{
	std::ios_base::sync_with_stdio(false); // 입출력 속도 향상
	std::cin.tie(NULL);

	// N개의 정점(1 ~ N), M개의 간선으로 구성된 무방향 그래프, 시작 정점 R
	int n, m, r;

	std::cin >> n >> m >> r;

	std::vector<std::vector<int>> vec(n + 1);

	int i;

	// 정점 u와 정점 v 간의 간선 정보를 저장
	for (i = 0; i < m; i++)
	{
		int u, v;
		std::cin >> u >> v;
		vec[u].push_back(v);
		vec[v].push_back(u);
	}

	// 각 정점의 인접 정점을 내림차순으로 정렬
	for (auto &row : vec)
		std::sort(row.begin(), row.end(), std::greater<int>());

	std::vector<int> visited(n + 1, 0);
	int order = 1;

	dfs(vec, visited, order, r);

	// // 노드의 방문 순서를 출력
	for (i = 1; i < n + 1; i++)
		std::cout << (visited[i] ? visited[i] : 0) << '\n';

	return 0;
}

/*

입력 :
5 1 1
1 4
정답 :
1
0
0
2
0

*/