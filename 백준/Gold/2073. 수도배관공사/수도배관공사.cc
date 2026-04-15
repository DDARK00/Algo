#include <iostream>
using namespace std;

int dp[100001];

void solve(int n, int m){
    int l, c;
    for (int i=0; i<m; i++) {
        cin >> l >> c; // 길이 용량
        if (l>n) continue;
        for (int j=n; j>=l; j--) {
            dp[j]=max(dp[j], min(dp[j-l],c));
        }
        dp[l]=max(dp[l],c);
    }
}

void print(int n){
    cout << dp[n];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int d, p; // 거리 파이프수
    cin >> d >> p;

    solve(d, p);
    print(d);
    return 0;
}