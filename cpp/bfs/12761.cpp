// 12761번 - 돌다리
#include <iostream>
#include <queue>

int a, b, n, m; // 스카이 콩콩의 힘 A, B, 동규의 현재위치 N, 주미의 현재위치 M


bool visited[100001] = {false, };

int count[100001] = {0, };

int i;

void bfs()
{
    const int dist[8] = {1, a, b, -1, -a, -b, a, b};
    std::queue<int> q;

    q.push(n);
    visited[n] = true;
    count[n] = 0;
    while (!q.empty())
    {
        int cur = q.front();
        q.pop();
        if (cur == m)
        {
            std::cout << count[m] << std::endl;
            return ;
        }

        for (i = 0; i < 6; i++)
        {
            int next = cur + dist[i];
            if (next < 0 || next > 100000)
                continue;
            if (!visited[next])
            {
                visited[next] = true;
                count[next] = count[cur] + 1;
                q.push(next);
            }
        }

        for (i = 6; i < 8; i++)
        {
            int next = cur * dist[i];
            if (next < 0 || next > 100000)
                continue;
            if (!visited[next])
            {
                visited[next] = true;
                count[next] = count[cur] + 1;
                q.push(next);
            }
        }
    }   
}

int main(void)
{
    std::cin >> a >> b >> n >> m;

    bfs();

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

참고 : https://jungahshin.tistory.com/240
*/