// 2798 블랙잭
#include <iostream>

int main(void)
{
	int n, m, i, j, k;

	std::cin >> n;
	std::cin >> m;

	int arr[n];

	for (i = 0; i < n; i++)
		std::cin >> arr[i];

	int max = 0;

	for (i = 0; i < n - 2; i++)
	{
		for (j = i + 1; j < n - 1; j++)
		{
			for (k = j + 1; k < n; k++)
			{
				if (arr[i] + arr[j] + arr[k] > m)
					continue;
				if (max < arr[i] + arr[j] + arr[k])
					max = arr[i] + arr[j] + arr[k];
			}
		}
	}

	std::cout << max << std::endl;
	return 0;
}