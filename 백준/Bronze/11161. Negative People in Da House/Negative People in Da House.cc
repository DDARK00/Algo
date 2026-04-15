#include <iostream>
using namespace std;
int main() {
    int t, m;
    cin >> t;
    for (int i=0; i<t; i++) {
        cin >> m;
        int p1, p2, now=0;
        int ans=0;
        for (int j=0; j<m; j++) {
            cin >> p1 >> p2;
            now += p2;
            now -= p1;
            if (now>0){
                ans += now;
                now = 0;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}