// 2252번 - 줄 세우기
#include <iostream>
#include <vector>
#include <queue>

int n, m; // 학생의 수, 키를 비교한 횟수

int i, a, b;

std::queue<int> order;

int main(void)
{
    std::cin >> n >> m;

    std::vector<std::vector<int>> graph(n + 1);

    std::vector<int> count(n + 1, 0);

    for (i = 0; i < m; i++)
    {
        std::cin >> a >> b;

        graph[a].push_back(b);

        // 가리키고 있는 정점(학생)은 기다려야하는 순서가 +1
        count[b]++;
    }

    for (i = 1; i < n + 1; i++)
        if (count[i] == 0)
            order.push(i);

    while (!order.empty())
    {
        int student;

        student = order.front();

        order.pop();

        std::cout << student << " ";

        for (i = 0; i < graph[student].size(); i++)
        {
            int next = graph[student][i];
            
            count[next]--;

            if (count[next] == 0)
                order.push(next);
        }
    }
    std::cout << std::endl;
    return 0;
}

/*
HINT: 단방향 그래프
참고: https://yabmoons.tistory.com/409
*/