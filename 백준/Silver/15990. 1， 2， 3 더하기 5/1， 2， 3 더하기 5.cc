#include <iostream>
#include <vector>
using namespace std;
const int MOD=1000000009;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    vector<vector<long long>> dp(100001, vector<long long>(4,0));

    dp[1][1]=1; // 끝 수가 1, 2, 3인 경우
    dp[2][2]=1;
    dp[3][1]=1; 
    dp[3][2]=1; 
    dp[3][3]=1; 
    // 0 0
    // 1 1 <- 1
    // 2 2 <- 1
    // 3 12 21 3 <- 3
    // 4 121 13 31 <- 3
    // 5 131 212 23 32 <- 4  1+4 2+3
    // 6 1212 123 132 213 231 312 321 <- 7 1+2 2+3 3+1
    // 7 12121 1213 1231 1312 1321 2131 232 3121 313   <- 9 2+1 1+3 3+1

    for (int i=4; i<100001; i++) {
        dp[i][1]=(dp[i-1][2]+dp[i-1][3])%MOD;
        dp[i][2]=(dp[i-2][1]+dp[i-2][3])%MOD;
        dp[i][3]=(dp[i-3][1]+dp[i-3][2])%MOD;
    }
    int t, tc;
    cin >> t;
    for (int i=0; i<t; i++) {
        cin >> tc;
        cout << (dp[tc][1]+dp[tc][2]+dp[tc][3])%MOD<< "\n";
    }
    return 0;
}