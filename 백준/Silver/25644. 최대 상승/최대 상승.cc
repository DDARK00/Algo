#include <iostream>
using namespace std;
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, ans, t, min_v;
    cin >> n;
    min_v = 1e9;
    ans = 0;
    for (int i=0; i<n; i++) {
        cin >> t;
        ans = max(ans, t-min_v);
        min_v = min(t, min_v);
    }
    cout << ans;
    return 0;
}