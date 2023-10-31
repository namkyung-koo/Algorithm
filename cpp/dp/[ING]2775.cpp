// 부녀회장이 될테야
#include <iostream>
#include <vector>

int dp(int floor, int unit, std::vector<std::vector<int> > &memo)
{
	// 기저 조건
	if (floor == -1)
		return 0;
	if (unit == -1)
		return 0;

	if (memo[floor][unit] != -1)
		return memo[floor][unit];

	// 재귀 조건
	memo[floor][unit] = dp(floor, unit, memo) + dp(floor, unit - 1, memo);

	return memo[floor][unit];
}

int main()
{
	int T, k, n;

	std::cin >> T;

	std::vector< std::pair<int, int> > v;

	int i, max = 0;
	// ==== 인자 입력 받기 ====
	for (i = 0; i < T; i++)
	{
		std::cin >> k;
		std::cin >> n;
		if (max < k)
			max = k;
		v.push_back(std::make_pair(k, n));
	}

	// 0층만 제외하고 모든 층을 -1로 초기화
	std::vector<std::vector<int> > matrix(max, std::vector<int>(14, -1));
	for (int i = 0; i < 14; i++)
		matrix[0][i] = i + 1;

	int result = 0;

	for (i = 0; i < T; i++)
		result = dp(v[i].first - 1, v[i].second, matrix);

	std::cout << result << std::endl;

	return 0;
}


// 1 5 15 35 70          => 3층       
// 1 4 10 20 35 51       => 2층
// 1 3  6 10 15 21 18    => 1층
// 1 2  3  4  5  6  7  8 => 0층