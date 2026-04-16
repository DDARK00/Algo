#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;
    cin >> n >> x; // 100 10000

    vector<long long> dp(x+1, 0);
    int l, c;
    for (int i=0; i<n; i++) {
        cin >> l >> c;
        for (int j=x; j>l; j--) {
            for (int cnt=1; cnt<c+1; cnt++) {
                if (j-l*cnt<0) {
                    continue;
                }
                dp[j]+=dp[j-l*cnt];
            }
        }

        for (int cnt=1; cnt<c+1; cnt++) {
            if (l*cnt > x) {
                continue;
            }
            dp[l*cnt]++;
        }
    }

    cout << dp[x];
    return 0;
}