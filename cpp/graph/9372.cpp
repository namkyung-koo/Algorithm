// 9372번 상근이의 여행
#include <iostream>
#include <vector>

int main(void)
{
	int t, n, m; // 테스트 케이스, 국가의 수, 비행기의 종류
	int i, j, a, b; // 1st, 2nd반복문, 방문 여부, 출발, 도착

	std::cin >> t;

	for (i = 0; i < t; i++)
	{
		std::cin >> n >> m;

		for (j = 0; j < m; j++)
			std::cin >> a >> b;
		std::cout << n - 1 << std::endl;
	}

	return 0;
}

/* T1
국가의 수 = 3, 비행기의 종류 = 3
1 - 2 - 3 - 1 

T2
국가의 수 = 5, 비행기의 종류 = 4
1 - 2 - 3 - 4 - 5
*/