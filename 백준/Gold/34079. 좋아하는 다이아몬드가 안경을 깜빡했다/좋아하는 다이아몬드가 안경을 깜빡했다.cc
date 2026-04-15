#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n+1,vector<int>());
    int u, v;
    for (int i=0; i<m; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    // bfs-> 1->n 유일한 간선 찾기
    queue<pair<int,int>> q;
    q.push({1,1});

    vector<int> visited(n+1,0);
    visited[1]=1;
    while (!q.empty()) {
        auto [v,c]=q.front();q.pop();
        for (auto nv : graph[v]) {
            if (visited[nv]==0) {
                visited[nv]=c+1;
                if (nv==1) break;
                q.push({nv,c+1});
            }
        }
    }

    int cost=visited[n];
    visited[n]=0;
    q={};
    q.push({n,cost});
    vector<int> answer(n+1,0);
    while (!q.empty()) {
        auto [v,c]=q.front();q.pop();
        for (auto nv : graph[v]) {
            if (visited[nv]==c-1) { // depth
                q.push({nv,c-1});
                if (answer[visited[nv]]==0) { // depth 내의 첫 방문
                    answer[visited[nv]]=nv;
                } else {
                    answer[visited[nv]]=-1;
                }
                visited[nv]=0;
            }
        }
    }

    for (int i=cost-1; i>1; i--) {
        if (answer[i] != -1 && answer[i] != 0) {
            cout << answer[i];
            return 0;
        }
    }
    cout << 1;
    return 0;
}