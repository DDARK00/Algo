#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, w;
    cin >> n >> m;

    priority_queue<int> pq;
    for (int i=0; i<n; i++) {
        cin >> w;
        pq.push(w);
    }

    for (int i=0; i<m; i++) {
        cin >> w;
        if (pq.empty()||pq.top()<w) {
            cout << 0;
            return 0;
        }
        w=pq.top()-w;pq.pop();
        pq.push(w);
    }
    
    cout << 1;
    return 0;
}