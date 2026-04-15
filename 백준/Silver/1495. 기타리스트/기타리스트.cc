#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, s, m;
    cin >> n >> s >>  m;
    int p;
    vector<vector<bool>> dp(n+1,vector<bool>(m+1,0));
    dp[0][s]=1;
    for (int i=1; i<n+1; i++) {
        cin >> p;
        for (int j=0; j<m+1; j++) {
            if (dp[i-1][j]) {
                if (j-p>=0) dp[i][j-p]=1;
                if (j+p<=m) dp[i][j+p]=1;
            }
        }
    }

    int answer=-1;
    for (int i=m; i>=0; i--) {
        if (dp[n][i]) {
            answer=i;
            break;
        }
    }

    cout << answer;
    return 0;
}