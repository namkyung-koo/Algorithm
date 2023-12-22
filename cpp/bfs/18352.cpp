// 18352번 - 특정 거리의 도시 찾기
#include <iostream>
#include <utility>
#include <vector>
#include <queue>
// #include <bits/stdc++.h> C++ 표준 라이브러리의 거의 모든 헤더 파일들이 포함(GNU GCC 컴파일러에서 사용)

#define INF 1e9 // 무한을 의미하는 값으로 10억을 설정

int n, m, k, x; // 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
int a, b;       // 출발 도시, 도착 도시

// 각 노드에 연결되어 있는 노드에 대한 정보를 담는 배열
std::vector<std::pair<int, int>> graph[300001];
// 최단 거리 테이블 만들기
int distance[300001];

void dijstra(int start)
{
    std::priority_queue<std::pair<int, int>> pq;
    // 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    pq.push({0, start});
    distance[start] = 0;
    while (!pq.empty()) // 큐가 비어있지 않다면
    {
        // 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        int dist = -pq.top().first; // 현재 노드까지의 비용
        int now = pq.top().second; // 현재 노드
        pq.pop();
        // 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if (distance[now] < dist)
            continue;
        // 현재 노드와 연결된 다른 인접한 노드들을 확인
        for (int i = 0; i < graph[now].size(); i++)
        {
            int cost = dist + graph[now][i].second;
            // 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if (cost < distance[graph[now][i].first])
            {
                distance[graph[now][i].first] = cost;
                pq.push(std::make_pair(-cost, graph[now][i].first));
            }
        }
    }
}

void initInf(void)
{
    for (int i = 1; i < 300000; i++)
        distance[i] = INF;
}

void print(void)
{
    std::queue<int> queue;

    for (int i = 1; i <= n; i++)
        if (distance[i] == k)
            queue.push(i);

    if (queue.empty())
        std::cout << -1 << '\n';
    else
    {
        while (!queue.empty())
        {
            std::cout << queue.front() << '\n';
            queue.pop();
        }
    }
}

int main(void)
{
    std::cin >> n >> m >> k >> x;

    // 모든 간선 정보를 입력받기
    for (int i = 0; i < m; i++)
    {
        std::cin >> a >> b;
        // a번 노드에서 b번 노드로 가는 비용이 1이라는 의미
        graph[a].push_back({b, 1});
    }

    // 최단 거리 테이블을 모두 무한으로 초기화
    initInf();

    // 다익스트라 알고리즘을 수행
    dijstra(x);

    // 거리가 k인 노드 출력
    print();

    return 0;
}

/* 참고 : https://www.youtube.com/watch?v=acqm9mM1P6o */
