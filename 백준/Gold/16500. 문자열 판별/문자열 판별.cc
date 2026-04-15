#include <iostream>
#include <vector>
using namespace std;

int solve(string s, int n){
    int dp[101]{};
    int s_size = s.size();
    dp[s_size] = 1;

    vector<string> a(n);
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }

    for (int i=s_size-1; i>=0; i--) {
        if (!dp[i+1]) continue;
        
        for (auto c : a) {
            bool flag = true;
            int size = c.size()-1;
            if (i-size < 0 || c[size] != s[i])continue;
            for (int j=0; j<size; j++) {
                if ( c[j] != s[i-size+j]){
                    flag = false;
                    break;
                }
            }
            if (flag){
                dp[i-size] = 1;
            }
        }
    }

    return dp[0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    int n;
    cin >> n;


    cout << solve(s, n);
    return 0;
}