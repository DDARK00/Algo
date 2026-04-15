#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<vector<int>> graph(100001);
vector<int> visited(100001, -1);

const auto cmp = [](auto a, auto b){return a>b;};
void dfs(int v, int depth){
    visited[v] = depth;
    sort(graph[v].begin(), graph[v].end(), cmp);
    for (auto nv : graph[v]) {
        if (visited[nv] == -1){
            dfs(nv, depth+1);
        }
    }
}

void print(int n){
    for (int i=1; i<n+1; i++) {
        cout << visited[i] << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, r;
    cin >> n >> m >> r;
    int u, v;
    for (int i=0; i<m; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    dfs(r,0);
    print(n);
    return 0;
}