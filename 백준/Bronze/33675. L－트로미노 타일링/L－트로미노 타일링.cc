#include <iostream>
using namespace std;
int main() {
    int n, t;
    cin >> t;
    long long dp[101];
    dp[1] = 0;
    dp[2] = 2;
    dp[3] = 0;
    dp[4] = dp[4-2]*2;
    for (int i=5; i<101; i++){
        dp[i] = dp[i-2]*2;
    }
    for (int i=0; i<t; i++){
        cin >> n;
        cout << dp[n] << "\n";
    }
    return 0;
}
// 이게맞나