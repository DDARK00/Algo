#include <iostream>
int main() {
    int n;
    int dp[100001];
    std::cin>>n;
    dp[0]=1;
    dp[1]=3;
    for (int i=2; i<n+1; i++) {
        dp[i] = ((dp[i-1]*2)+dp[i-2])%9901;
    }
    std::cout << dp[n];
    return 0;
}