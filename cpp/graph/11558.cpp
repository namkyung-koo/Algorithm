// 11558번 The Game of Death
#include <iostream>
#include <vector>

void theGameOfDeath()
{
    int n; // 플레이어의 수

    std::cin >> n;

    std::vector<int> p(n + 1, 0); // 플레이어가 지목한 플레이어

    std::vector<bool> visited(n + 1, false); // 방문 여부. 즉, 자기 자신을 지목한 경우

    for (int i = 1; i <= n; i++)
        std::cin >> p[i];
    
    int pos = 1, count = 0;

    while (pos != n)
    {

        // 자기 자신을 지목한 경우
        if (visited[pos] == true)
        {
            std::cout << 0 << std::endl;
            return ;
        }

        visited[pos] = true;
        count++;
        pos = p[pos];
    }
    std::cout << count << std::endl;
}

int main(void)
{
    int t; // 테스트 케이스의 수

    std::cin >> t;

    while (t-- > 0)
        theGameOfDeath();

    return 0;
}

/*
2 - 3 - 4 - 5 - 6 - 7 - 1 - 7
1   2   3   4   5   6   7
t   t   t   t   t   t

참고 : https://github.com/jwvg0425/boj/blob/master/solutions/11558/11558.cpp14.cpp
*/