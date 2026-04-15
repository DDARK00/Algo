#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    queue<int> q;

    int n, m, a, b;
    cin >> n >> m;
    vector<vector<int>> g(n+1, vector<int>());
    for (int i=0; i<m; i++) {
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    vector<int> visited(n+1, 100001);

    q.push(1);
    visited[1]=0;
    int v;
    while (!q.empty()){
        v = q.front();q.pop();
        if (v==n)break;
        for (auto nv : g[v]) {
            if (visited[nv]==100001) {
                visited[nv]=visited[v]+1;
                q.push(nv);
            }
        }
    }
    cout<<visited[n]-1;
    return 0;
}