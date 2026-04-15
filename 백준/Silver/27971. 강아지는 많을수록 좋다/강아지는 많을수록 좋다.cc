#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, a, b;
    cin >> n >> m >> a >> b;
    // a소환, b소환
    vector<int> visited(100001,-1);

    int l, r;
    // 100000*100
    for (int i=0; i<m; i++) {
        cin >> l >> r;
        for (int j=l; j<r+1; j++) {
            visited[j]=0;
        }
    }
    visited[0]=0;
    
    queue<int> q;
    q.push({0});

    int v;
    while (!q.empty()){
        v=q.front();q.pop();
        if (v+a<=n&&visited[v+a]==-1) {
            visited[v+a]=visited[v]+1;
            q.push(v+a);
        }
        if (v+b<=n&&visited[v+b]==-1) {
            visited[v+b]=visited[v]+1;
            q.push(v+b);
        }
    }

    cout << visited[n];
    return 0;
}