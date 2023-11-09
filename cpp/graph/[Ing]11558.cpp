// 11558번 The Game of Death
#include <iostream>
#include <vector>

int main(void)
{
    int testCase, n, playerOrder, i; // 테스트 케이스의 수, 플레이어의 수, 플레이어의 순서

    std::cin >> testCase;

    std::vector<int> vector;

    bool f;

    while (testCase-- > 0)
    {
        std::cin >> n;
        if (n == 1)
        {
            std::cout << 0 << std::endl;
            continue;
        } 
        f = false;
        for (playerOrder = 0; playerOrder < n; playerOrder++)
        {
            std::cin >> i;   
            vector.push_back(i);
            if (playerOrder != 0 && vector[playerOrder - 1] == vector[playerOrder])
            {
                std::cout << 0 << std::endl;
                f = true;
                break ;
            }
        }
        if (!f)
            std::cout << n - 1 << std::endl;

        vector.clear();
    }

    return 0;
}

/*
2 - 3 - 4 - 5 - 6 - 7 - 1 - 7
    1   2   3   4   5   6   7
*/