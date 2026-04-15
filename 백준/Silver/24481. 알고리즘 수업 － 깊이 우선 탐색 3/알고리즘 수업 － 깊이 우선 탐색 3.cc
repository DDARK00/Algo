#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> graph(100001);
int visited[100001]{};
void dfs(int r, int depth){
    visited[r] = depth;
    for (auto k : graph[r]) {
        if (!visited[k])dfs(k,depth+1);
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

    for (int i=1; i<n+1; i++) {
        sort(graph[i].begin(),graph[i].end());
    }
    
    dfs(r,1);

    for (int i=1; i<n+1; i++) {
        if (visited[i]==0){
            cout << -1 << "\n";
        }else{
            cout << visited[i]-1 << "\n";
        }
    }
    return 0;
}