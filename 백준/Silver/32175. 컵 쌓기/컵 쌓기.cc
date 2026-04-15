#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1000000007;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, h;
    cin >> n >> h;
    vector<int> cups(n);
    vector<long long> dp(h+1,0);
    for (int i=0; i<n; i++) {
        cin >> cups[i];
        if (cups[i]<=h) {
            dp[cups[i]]+=1;
        }
    }

    for (int i=1; i<=h; i++) {
        for (auto k : cups) {
            if (i-k>0) {
                dp[i]=(dp[i]+dp[i-k])%MOD;
            }
        }
    }
    cout << dp[h];
    return 0;
}