#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    vector<int> dp(100001, 101);
    dp[0]=0;

    int n, k, t;
    cin >> n >> k;
    for (int i=0; i<n; i++) {
        cin >> t;
        for (int j=k; j>=t; j--) {
            dp[j]=min(dp[j], dp[j-t]+1);
        }
        dp[t]=1;
    }

    int ans=dp[k]==101?-1:dp[k];
    cout << ans;
    return 0;
}