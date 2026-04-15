#include <iostream>
using namespace std;

int arr[11][11];
bool used[11]{};
int dfs(int k, int val) {
    if (k==11) {
        return val;
    }
    int p=0;
    for (int i=0; i<11; i++) {
        if (arr[k][i]==0 || used[i]) continue;
        used[i]=1;
        p=max(p,dfs(k+1, val+arr[k][i]));
        used[i]=0;
    }
    return p;
}

void solve() {
    for (int i=0; i<11; i++) {
        for (int j=0; j<11; j++) {
            cin >> arr[i][j];
        }
    }

    cout << dfs(0, 0) << "\n";
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