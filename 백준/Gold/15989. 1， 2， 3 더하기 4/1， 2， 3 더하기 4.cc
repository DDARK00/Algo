#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> dp(10001,1);

    for (int i=2; i<10001; i++) {
        dp[i]+=dp[i-2];
    }
    for (int i=3; i<10001; i++) {
        dp[i]+=dp[i-3];
    }

    int t, n;
    cin>> t;
    for (int i=0; i<t; i++) {
        cin >> n;
        cout << dp[n] << "\n";
    }
    return 0;
}