#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;

    int a, b;
    vector<vector<bool>> g(n+1, vector<bool> (n+1));
    for (int i=0; i<m; i++) {
        cin >> a >> b;
        g[a][b]=true;
        g[b][a]=true;
    }
    int answer=0;
    for (int i=1; i<n+1; i++) {
        for (int j=i+1; j<n+1; j++) {
            if (g[i][j]) continue;
            for (int k=j+1; k<n+1; k++) {
                if (g[i][k] || g[j][k]) continue;
                answer++;
            }
        }
    }
    cout << answer;
    return 0;
}