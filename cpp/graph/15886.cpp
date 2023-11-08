// 15886번 내 선물을 받아줘 2
#include <iostream>

int main(void)
{
	int n, i, count;

	std::cin >> n;

	std::string map;

	std::cin >> map;

	count = 0;
	for (i = 0; i < n - 1; i++)
	{
		if (map[i] == 'E' && map[i + 1] == 'W')
		{
			count++;
			if (i + 2 >= n)
			{
				std::cout << count << std::endl;
				return 0;
			}
			// 조건에 맞으면 for에 있는 i++을 포함하여 두 칸 뒤로 뛸꺼임
			++i;
		}
		else if (map[i] == 'W' && map[i - 1] == 'E')
		{
			count++;
			if (i + 2 >= n)
			{
				std::cout << count << std::endl;
				return 0;
			}
			// 조건에 맞으면 for에 있는 i++을 포함하여 두 칸 뒤로 뛸꺼임
			++i;
		}
	}
	std::cout << count << std::endl;
	return 0;
}

/*
6 EEWWEW
len = 6
*/