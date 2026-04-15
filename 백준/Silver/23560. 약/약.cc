#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;

    cin >> n;
    // 1 2 2 6
    int dp[16];
    
    dp[0]=0;
    dp[1]=2;
    dp[2]=6;
    for (int i=3; i<16; i++) {
        dp[i]=dp[i-1]*2+dp[i-1];
    }

    cout << dp[n];
    return 0;
}