#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    priority_queue<int> pq;

    int tmp;
    for (int i=0; i<n; i++) {
        cin >> tmp;
        pq.push(tmp);
    }

    int before=0;
    vector<int> ans;
    while (!pq.empty()){
        tmp=pq.top();pq.pop();
        ans.push_back(before/2+tmp);
        before=ans.back();
        if (tmp-m>k){
            pq.push(tmp-m);
        }
    }

    cout << ans.size() << "\n";
    for (auto k : ans) {
        cout << k << "\n";
    }
    
    return 0;
}