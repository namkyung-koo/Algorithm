// 1329번 - 폴짝폴짝
#include <iostream>
#include <vector>
#include <queue>
int n, a, b; // 징검다리의 개수, 출발 징검다리, 도착 징검다리

int stepping_stone[10001];

std::vector<bool> visited;

int jumping(int start, int end)
{
    std::queue<int> queue;
    queue.push(start);
    int step = 0;
    visited[start] = true;

    while(!queue.empty())
    {
        int size = queue.size();
        for (int s = 0; s < size; s++)
        {
            int current = queue.front();
            queue.pop();

            if (current == end)
                return step;
        
            for (int i = 1; i * stepping_stone[current] + current <= n; i++)
            {
                int next = i * stepping_stone[current] + current;
                if (!visited[next]) {
                    visited[next] = true;
                    queue.push(next);
                }
            }

            for (int i = 1; current - i * stepping_stone[current] >= 1; i++)
            {
                int next = current - i * stepping_stone[current];
                if (!visited[next]) {
                    visited[next] = true;
                    queue.push(next);
                }
            }
        }
        step++;
    }
    return -1;
}

int main(void)
{
    std::cin >> n;

    visited.resize(n + 1, false);

    for (int i = 1; i < n + 1; i++)
        std::cin >> stepping_stone[i];

    std::cin >> a >> b;

    std::cout << jumping(a, b) << std::endl;

    return 0;
}

/*
징검다리에 쓰여있는 정수는 10,000보다 작거나 같은 자연수이다.
라는 말은 즉 음수도 포함될 수 있다는 뜻이므로 뒤로 가는 경우도 고려해야 한다.

x 1 2 2 1 2

*/