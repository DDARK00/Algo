#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, a, b;
    cin >> n;

    priority_queue<int> pq;
    for (int i=0; i<n; i++) {
        cin >> a;
        if (a==0) {
            if (!pq.empty()) {
                cout << pq.top();
                pq.pop();
            } else {
                cout << -1;
            }
            cout << "\n";
        } else {
            for (int j=0; j<a; j++) {
                cin >> b;
                pq.push(b);
            }
        }
    }
    return 0;
}