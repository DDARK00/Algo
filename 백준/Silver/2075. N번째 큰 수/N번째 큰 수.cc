#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MIN=-1000000001;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, tmp;
    cin >> n;
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i=0; i<n; i++) {
        pq.push(MIN);
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> tmp;
            if (tmp>pq.top()) {
                pq.pop();
                pq.push(tmp);
            }
        }
    }

    cout << pq.top();
    return 0;
}