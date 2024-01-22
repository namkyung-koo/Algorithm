// 12761번 - 돌다리
#include <iostream>

int a, b, n, m; // 스카이 콩콩의 힘 A, B, 동규의 현재위치 N, 주미의 현재위치 M

int main(void)
{
    std::cin >> a >> b >> n >> m;

    int cur[8] = {n, n, n, n, n, n, n, n};
    int dist[8] = {0};

    int cnt = 0;

    while (true)
    {
        for (int i = 0; i < 8; i++)
        {
            
        }
    }

    return 0;
}

/*
예제 입력
2 3 1 20
1 * 3 => 3 * 3 => 9 * 2 => 18 + 2
총 4번 이동

+1 +a +b
-1 -a -b
*a *b

https://www.acmicpc.net/problem/12761

1. 주미의 현재 위치 - 동규의 현재 위치 => 저장
2. {+1, +a, +b, -1, -a, -b, *a, *b} 배열을 순회해서 다른 배열에 값 저장
3. 저장된 배열의 값 중 최솟값을 min에 대입 (반복문)
4. 탈출 조건 min == 0
*/