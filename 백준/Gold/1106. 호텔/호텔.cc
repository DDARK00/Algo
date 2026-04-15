#include <iostream>
#include <vector>
using namespace std;

int c, n;
vector<int> dp(1101, 1e9); // 고객=비용

void solve(){
    int sub_ans, target;
    dp[0]=0;
    for (int i=0; i<n; i++) {
        cin >> sub_ans >> target;
        // 비용 고객
        for (int j=target; j<=c+100; j++) {
            dp[j]=min(dp[j],dp[j-target]+sub_ans);
        }
    }

    for (int i=c+1; i<c+100; i++) {
        dp[c]=min(dp[c],dp[i]);
    }
    cout << dp[c];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> c >> n;
    // target, citys
    solve();
    return 0;
}