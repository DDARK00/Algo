#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
    cin.tie(NULL);

    int tc, n;
    cin >> tc;

    long dp[1000001]{};
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    dp[4] = 7;
    for (int i=5; i<1000001; i++) {
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009;
    }

    for (int i=0;i<tc;i++) {
        cin >> n;
        cout << dp[n] << "\n";
    }
	return 0;
}