// 투에-모스 문자열
#include <iostream>
#include <math.h>

int main(void)
{
	long long k;

	std::cin >> k;

	std::cout << k << std::endl;

	return 0;
}

// 0 => 1
// 0 1 => 2
// 0 1 1 0 => 4
// 0 1 1 0 1 0 0 1 => 8
// 0 1 1 0 1 0 0 1 0 1 1 0 1 0 0 1 => 16