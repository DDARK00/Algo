#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, query; // 2000
    cin >> n >> m >> query;

    queue<pair<int,int>> q; // st, v
    vector<vector<int>> graph(n+1,vector<int>());
    
    int u, v;
    for (int i=0; i<m; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
    }

    vector<vector<int>> visited(n+1,vector<int>(n+1,2002));
    for (int i=1; i<n+1; i++) {
        visited[i][i]=0;
        q.push({i,i});
    }

    while (!q.empty()) {
        // st to v to nv
        auto [st, v]=q.front();q.pop();
        for (auto nv : graph[v]) {
            if (visited[st][nv]>visited[st][v]+1) {
                visited[st][nv]=visited[st][v]+1;
                q.push({st,nv});
            }
        }
    }

    int wu, wv, answer;
    for (int t=0; t<query; t++) {
        cin >> u >> v;
        answer=2002;
        // 모든 u, v중 최단이 아닌 최소
        for (int i=1; i<n+1; i++) {
            wu=visited[i][u];
            wv=visited[i][v];
            if (wu !=2002 && wv !=2002) {
                answer=min(answer,max(wu,wv));
            }
        }
        if (answer==2002) {
            answer=-1;
        }
        cout << answer << "\n";
    }

    return 0;
}