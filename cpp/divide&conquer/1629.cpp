// 곱셈

#include <iostream>

long long myDiv(int n, int power, int mod)
{
	if (power == 1)
		return n % mod;

	if (power % 2)
		return (myDiv(n, power - 1, mod) * myDiv(n, 1, mod)) % mod;
	return (myDiv(n, power / 2, mod) * myDiv(n, power / 2, mod)) % mod;
}

int main(void)
{
	int a, b, c;

	std::cin >> a >> b >> c;

	long long result = myDiv(a, b, c);

	std::cout << result << std::endl;

	return 0;
}

// 10 11 12 => 4
// 6 11 13 => 11
// 4 1 2 => 0
// 99999 99999 100000 => 99999