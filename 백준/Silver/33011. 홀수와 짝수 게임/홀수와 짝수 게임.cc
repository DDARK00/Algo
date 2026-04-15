#include <iostream>
using namespace std;

// 1. 선은 많은걸 고른다
// 2. 후는 선이 안 고른걸 고르면 반드시 진다
// 3. 후는 선이랑 같은걸 고르면 이길 수도 있다
// 4. 많은 수가 짝수개면 후가 이김 홀수개면 선이 이김
// 5. 홀짝이 같으면 선은 아무거나 고르고 후가 이긴다

void solve() {
    int n, a;
    int even_odd[2] = {0,0};
    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> a;
        even_odd[a%2]++;
    }

    if (even_odd[0]==even_odd[1]) {
        cout << "heeda0528\n";
    } else {
        if (max(even_odd[0],even_odd[1])%2) {
            cout << "amsminn\n";
        } else {
            cout << "heeda0528\n";
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    for (int i=0; i<tc; i++) {
        solve();
    }

    return 0;
}