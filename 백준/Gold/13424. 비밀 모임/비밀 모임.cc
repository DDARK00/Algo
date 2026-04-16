#include <iostream>
#include <vector>
using namespace std;

void solve() {
    int n, m, a, b, c;
    cin >> n >> m;
    vector<vector<int>> dist(n+1,vector<int>(n+1,1e9));
    for (int i=0; i<m; i++) {
        cin >> a >> b >> c;
        dist[a][b]=c;
        dist[b][a]=c;
    }

    for (int i=1; i<n+1; i++) {
        dist[i][i]=0;
    }
    for (int m=1; m<n+1; m++) {
        for (int s=1; s<n+1; s++) {
            if (dist[s][m]==1e9) {
                continue;
            }
            for (int e=1; e<n+1; e++) {
                if (dist[m][e]==1e9) {
                    continue;
                }
                if (dist[s][m]+dist[m][e]<dist[s][e]) {
                    dist[s][e]=dist[s][m]+dist[m][e];
                }
            }
        }
    }
    int k;
    cin >> k;
    vector<int> fr(k);
    for (int i=0; i<k; i++) {
        cin >> fr[i];
    }
    vector<int> answer={-1,1000000}; // idx val
    // 어떤 방에서 다른 방으로 비밀통로를 이용해서 갈 수 없는 경우는 존재하지 않으며
    for (int i=1; i<n+1; i++) {
        int tmp=0;
        for (auto l : fr) {
            tmp+=dist[l][i];
        }
        if (tmp<answer[1]) {
            answer={i,tmp};
        }
    }
    cout << answer[0] << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int tc;
    cin >> tc;
    for (int i=0; i<tc; i++) {
        solve();
    }
    return 0;
}