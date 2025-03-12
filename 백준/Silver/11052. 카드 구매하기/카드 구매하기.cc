#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    int pack[n];
    for (int i=0; i<n; i++) {
        cin >> pack[i];
    }

    int dp[n+1] = {0};

    for (int i=1; i<n+1; i++) {
        dp[i] = pack[i-1];

        for (int j=1; j<i/2+1; j++) {
            dp[i] = max(dp[i], dp[i-j]+dp[j]);

        }
    }

    cout << dp[n] << "\n";
	return 0;
}