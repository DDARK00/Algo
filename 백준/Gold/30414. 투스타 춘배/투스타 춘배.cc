#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> graph(100001,vector<int>());
vector<int> san(100001);
vector<int> want(100001);

int dfs(int v, vector<bool> &visited) {
    int w=want[v]-san[v];
    for (auto nv : graph[v]) {
        if (visited[nv]) {
            continue;
        }
        visited[nv]=1;
        w+=dfs(nv, visited);
    }

    w=max(0,w);
    return w;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, p;
    cin >> n >> p;
    for (int i=1; i<n+1; i++) {
        cin >> san[i];
    }

    for (int i=1; i<n+1; i++) {
        cin >> want[i];
    }

    int u, v;
    for (int i=1; i<n; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<bool> visited(n+1,0);
    visited[p]=1;
    int answer = dfs(p, visited);
    cout << answer;
    return 0;
}