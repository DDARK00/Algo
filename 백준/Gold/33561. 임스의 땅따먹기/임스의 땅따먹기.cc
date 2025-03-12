#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int arr[n][n];
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin>>arr[i][j];
        }
    }

    int k;
    cin >> k;
    int val[k];
    for (int i=0; i<k; i++) {
        cin >> val[i];
    }
    sort(val, val+k, greater<int>());

    // init
    int g_val[k+1];
    g_val[0] =0;
    for (int i=1; i<k+1; i++) {
        g_val[i] = g_val[i-1]+val[i-1];
    }

    pair<int,int> g[n+1][n+1];

    for (int i=0; i<n+1; i++) {
        g[i][0] = {0,0}; // val, zero_cnt
        g[0][i] = {0,0};
    }
    int ans = 0;

    // pre_sum
    for (int i=1; i<n+1; i++) {
        for (int j=1; j<n+1; j++) {
            g[i][j] = {
                g[i-1][j].first+g[i][j-1].first+arr[i-1][j-1]-g[i-1][j-1].first,
                arr[i-1][j-1]==0?g[i-1][j].second+g[i][j-1].second+1-g[i-1][j-1].second:g[i-1][j].second+g[i][j-1].second-g[i-1][j-1].second
            };
        }
    }

    int temp_zero=0, temp_val=0;
    for (int i=1; i<n+1; i++) {
        for (int j=1; j<n+1; j++) {
            // 현재 좌표에서 정사각형이 될 수 있는 경우
            for (int l=0;l<min(i,j);l++){ // val, zero_cnt
                temp_zero = g[i][j].second - g[i-1-l][j].second - g[i][j-1-l].second + g[i-1-l][j-1-l].second;
                temp_val = g[i][j].first - g[i-1-l][j].first - g[i][j-1-l].first + g[i-1-l][j-1-l].first;
                if (temp_zero>k) {
                    break;
                }else{
                    ans = max(ans,temp_val+g_val[temp_zero]);
                }
            }
        }
    }

    cout << ans;
    return 0;
}