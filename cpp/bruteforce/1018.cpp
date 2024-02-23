// 체스판 다시 칠하기
#include <iostream>
#include <string>
#include <vector>

int main(void)
{
	int m, n;

	std::cin >> m >> n;

	std::vector<std::vector<std::string>> chess(m, std::vector<std::string>(n));

	// 체스판 인자 받기
	for (int i = 0; i < m; i++)
	{
		std::string str;
		std::cin >> str;
		for (int j = 0; j < n; j++)
			chess[i][j] = str[j];
	}

	int b_cnt, w_cnt, cnt, min = 100000000;
	std::string pos;

	for (int i = 0; i <= m - 8; i++)
	{
		for (int j = 0; j <= n - 8; j++)
		{
			b_cnt = 0, w_cnt = 0, cnt = 0;
			for (int row = i; row < i + 8; row++)
			{
				for (int col = j; col < j + 8; col++)
				{
					// WBWBWBWB
					if ((row - i) % 2 == 0)
					{ 
						if ((col - j) % 2 == 0 && chess[row][col] != "W")
							w_cnt++;
						else if ((col - j) % 2 == 1 && chess[row][col] != "B")
							w_cnt++;
					}
					else if ((row - i) % 2 == 1)
					{
						if ((col - j) % 2 == 0 && chess[row][col] != "B")
							w_cnt++;
						else if ((col - j) % 2 == 1 && chess[row][col] != "W")
							w_cnt++;
					}
					// BWBWBWBW
					if ((row - i) % 2 == 0)
					{
						if ((col - j) % 2 == 0 && chess[row][col] != "B")
							b_cnt++;
						else if ((col - j) % 2 == 1 && chess[row][col] != "W")
							b_cnt++;
					}
					else if ((row - i) % 2 == 1)
					{
						if ((col - j) % 2 == 0 && chess[row][col] != "W")
							b_cnt++;
						else if ((col - j) % 2 == 1 && chess[row][col] != "B")
							b_cnt++;
					}
				}
			}
			cnt = b_cnt < w_cnt ? b_cnt : w_cnt;
			if (cnt < min)
				min = cnt;
		}
	}
	std::cout << min << std::endl;

	return 0;
}

// BW BW BW BW
// WB WB WB WB
// 정답 체스판 만들어놓고 string compare
// 예제 2, 4
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