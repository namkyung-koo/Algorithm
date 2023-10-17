// 체스판 다시 칠하기
#include <iostream>
#include <string>

int main(void)
{
	int m, n;

	std::cin >> m >> n;

	std::string board[m];

	// 체스판 입력받기
	std::cin.ignore();
	for (int i = 0; i < m; i++)
		getline(std::cin, board[i]);

	int row, col, j, k, min, cnt;

	min = 32;
	for (row = 0; row <= m - 8; row++)
	{
		for (col = 0; col <= n - 8; col++)
		{
			cnt = 0;
			for (j = row; j < 8; j++)
			{
				for (k = col; k < 8; k++)
				{
				}
			}
			if (min > cnt)
				min = cnt;
		}
	}
	std::cout << cnt << std::endl;
	return 0;
}


// 10 13
// BBBBB  BBBWBWBW 1
// BBBBB  WBWBWBWB 2
// BBBBB  BWBWBWBW 1
// BBBBB  WBWBWBWB 2
// BBBBB  BWBWBWBW 1
// BBBBB  WBWBWBWB 2
// BBBBB  BWBWBWBW 1
// BBBBB  WBWBWBWB 2 => 12

// WWWWWWWWWWBWB
// WWWWWWWWWWBWB