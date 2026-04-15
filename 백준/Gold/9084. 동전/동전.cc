#include <iostream>
#include <vector>
using namespace std;

int t;
void solve(){
    int n, m;
    cin >> n;
    int coins[n];
    for (int i=0; i<n; i++) {
        cin >> coins[i];
    }
    cin >> m;
    vector<int> dp(m+1, 0);

    for (int i=0; i<n; i++) {
        if (m<coins[i]) {
            continue;
        }
        dp[coins[i]]++;
        for (int j=coins[i]; j<m+1; j++) {
            dp[j] = dp[j-coins[i]]+dp[j];
        }
    }

    cout << dp[m] << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;

    for (int i=0; i<t; i++) {
        solve();
    }
    return 0;
}