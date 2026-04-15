#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

vector<vector<int>> graph(100001,vector<int>());
void bfs(int n, int r){
    int visited[100001]{};
    visited[r]=1;
    queue<int> q;
    q.push(r);

    int x, c=1;
    while (!q.empty()){
        x=q.front();q.pop();
        sort(graph[x].begin(),graph[x].end(),greater<int>());
        for (auto nx : graph[x]) {
            if (visited[nx]!=0) {
                continue;
            }
            q.push(nx);
            c++;
            visited[nx]=c;
        }
    }

    for (int i=1; i<n+1; i++) {
        cout << visited[i] << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m, x, y, r;
    cin >> n >> m >> r;
    for (int i=0; i<m; i++) {
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    bfs(n, r);
    return 0;
}