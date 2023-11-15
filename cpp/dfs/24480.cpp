// 24480번 알고리즘 수업 - 깊이 우선 탐색 2
#include <iostream>
#include <functional> // std::greater를 위해 필요
#include <algorithm>
#include <utility> // std::pair를 위해 필요
#include <vector>

void dfs(int r, std::vector<std::pair<int, int> > &vec, std::vector<int> &visited)
{
	visited[r] = true;

	std::vector<int> found;

	for (const auto &value : vec) {
		if (value.first == r)
			found.push_back(value.second);
		else if (value.second == r)
			found.push_back(value.first);
	}

	if (!found.size())
		return ;
	
	std::sort(found.begin(), found.end(), std::greater<int>());

	unsigned int j;

	for (j = 0; j < found.size() && visited[found[j]] == false; j++)
		dfs(found[j], vec, visited);
}

int main(void)
{
	// N개의 정점(1 ~ N), M개의 간선으로 구성된 무방향 그래프, 시작 정점 R
	int n, m, r;

	std::cin >> n >> m >> r;

	std::vector<int> visited(n + 1); // 방문 여부 표시
	std::vector<std::pair<int, int> >vec(m); // 간선 정보를 담기 위한 vector

	int i, u, v;

	for (i = 0; i < m; i++)
	{
		std::cin >> u >> v;
		vec.push_back(std::make_pair(u, v));
	}

	dfs(r, order, vec, visited);

	// 출력 부분
	for (i = 1; i < n + 1; i++)
	{
		if (visited[i] == false)
			std::cout << 0 << std::endl;
		else
			std::cout << order[i] << std::endl;
	}

	return 0;
}

/*
      1
	 / \ 
    4 - 2
	 \ /
	  3   5

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