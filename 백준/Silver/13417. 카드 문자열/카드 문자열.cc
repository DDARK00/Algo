#include <iostream>
#include <deque>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t, n;
    char c;
    cin >> t;
    for (int i=0; i<t; i++) {
        deque<char> dq;
        cin >> n >> c;
        dq.push_back(c);
        for (int j=0; j<n-1; j++) {
            cin >> c;
            if (dq.front()>=c) {
                dq.push_front(c);
            } else {
                dq.push_back(c);
            }
        }
        for (auto k : dq) {
            cout << k;
        }
        cout << "\n";
    }
    return 0;
}