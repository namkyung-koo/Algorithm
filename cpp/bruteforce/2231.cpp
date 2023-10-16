// 분해합
#include <iostream>

int size(int n)
{
	if (n < 10)
		return 1;
	return 1 + size(n / 10);
}

int main(void)
{
	int n, len;

	std::cin >> n;

	int temp, sum, i, j;

	for (i = 0; i < n; i++)
	{
		len = size(i);
		sum = i;
		temp = i;
		for (j = 0; j < len; j++)
		{
			sum += temp % 10;
			temp = temp / 10;
		}
		if (sum == n)
		{
			std::cout << i << std::endl;
			return 0;
		}
	}
	std::cout << 0 << std::endl;

	return 0;
}

// 216 = 198 + 1 + 9 + 8
// 90 => 81 + 8 + 1
// 123 => 114 + 1 + 1 + 4 = 120 / 115 + 1 + 1 + 5 = 122 / 116 + 1 + 1 + 6 = 124
// 252 => 242 + 2 + 4 + 2 = 250 / 243 + 2 + 4 + 3 = 252