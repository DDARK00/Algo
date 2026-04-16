#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> graph;
vector<long long> visited;
long long answer=0;
long long cnt=1;

void dfs(long long v, long long d) {
    visited[v]=cnt;
    answer+=cnt*d;
    cnt++;

    for (long long nv : graph[v]) {
        if (visited[nv]==-1) {
            dfs(nv, d+1);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, r;
    cin >> n >> m >> r;

    graph.assign(n+1, vector<int>());
    visited.assign(n+1, -1);

    for (int i=0; i<m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i=1; i<=n; i++) {
        sort(graph[i].begin(), graph[i].end(), greater<long long>());
    }

    dfs(r, 0); // v, depth

    cout << answer;
    return 0;
}
