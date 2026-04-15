#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m, r;
int visited[100001]{};
vector<vector<int>> graph(100001,vector<int>());
void init() {
    cin >> n >> m >> r;
    int u, v;
    for (int i=0; i<m; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
}

// pseudo
// dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
//     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
//     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
//         if (visited[x] = NO) then dfs(V, E, x);
// }

int answer=1;
void dfs(int r) {
    visited[r]=answer;
    answer++;
    sort(graph[r].begin(),graph[r].end());
    for (auto k : graph[r]) {
        if (visited[k]) {
            continue;
        }
        dfs(k);
    }
}

void print() {
    for (int i=1; i<=n; i++) {
        cout << visited[i] << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    init();
    dfs(r);
    print();
    return 0;
}