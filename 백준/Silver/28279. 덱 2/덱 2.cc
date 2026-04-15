#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k, x;
    cin >> n;

    deque<int> dq;
    for (int i=0; i<n; i++) {
        cin >> k;
        switch (k) {
            case 1:
                cin >> x;
                dq.push_front(x);
                break;
            case 2:
                cin >> x;
                dq.push_back(x);
                break;
            case 3:
                if (!dq.empty()) {
                    cout << dq.front();
                    dq.pop_front();
                } else {
                    cout << -1;
                }
                cout << "\n";
                break;
            case 4:
                if (!dq.empty()) {
                    cout << dq.back();
                    dq.pop_back();
                } else {
                    cout << -1;
                }
                cout << "\n";
                break;
            case 5:
                cout << dq.size() << "\n";
                break;
            case 6:
                if (!dq.empty()) {
                    cout << 0;
                } else {
                    cout << 1;
                }
                cout << "\n";
                break;
            case 7:
                if (!dq.empty()) {
                    cout << dq.front();
                } else {
                    cout << -1;
                }
                cout << "\n";
                break;
            case 8:
                if (!dq.empty()) {
                    cout << dq.back();
                } else {
                    cout << -1;
                }
                cout << "\n";
                break;
        }
    }
    return 0;
}