#include <iostream>
using namespace std;

int n, t;
int dp[100001]{};
void solve(){
    int k, s;
    for (int i=0; i<n; i++) {
        cin >> k >> s;
        for (int j=t+1; j>=k; j--) {
            dp[j]=max(dp[j-k]+s, dp[j]);
        }
    }
    cout << dp[t];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> t;

    solve();
    return 0;
}