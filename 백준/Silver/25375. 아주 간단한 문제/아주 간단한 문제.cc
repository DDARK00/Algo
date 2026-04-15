#include <iostream>

using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    long long t, a, b; // 아 롱롱롱롱~~~!
    cin >> t;
    for (int i=0; i<t; i++) {
        cin >> a >> b;
        if ((b%a==0) && (b/a >=2)) {
            cout << 1 << "\n";
        } else{
            cout << 0 << "\n";
        }
    }
    return 0;
}