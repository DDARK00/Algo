#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    int val;
    vector<pair<int,int>> dp(k+1,{0,0}); // idx val
    pair<int,int> target_1={0,0}, target_2={0,0};
    auto cmp=[](auto a, auto b){return a.second>b.second;};

    for (int i=0; i<n; i++) {
        for (int j=1; j<k+1; j++) {
            cin >> val;
            if (target_1.first==j) {
                dp[j]={j,target_2.second+val};
            } else {
                dp[j]={j,target_1.second+val};
            }
        }
        sort(dp.begin(),dp.end(),cmp);
        target_1=dp[0];
        target_2=dp[1];
        dp.assign(k+1,{0,0});
    }

    cout << target_1.second;
    return 0;
}