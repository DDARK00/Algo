#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, a, b;
    cin >> n;
    vector<vector<int>> vc(n+1);
    for (int i=0; i<n; i++) {
        cin >> a >> b;
        vc[a].push_back(b);
    }
    priority_queue<int> pq;

    long long ans=0;
    for (int i=n; i>0; i--) {
        for (auto k:vc[i]){
            pq.push(k);
        }

        if(!pq.empty()){
            ans+=pq.top();
            pq.pop();
        }
    }
    cout << ans;
    return 0;
}