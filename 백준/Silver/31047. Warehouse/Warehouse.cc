#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

void solve() {
    int n;
    cin >> n;
    string name;
    int k;

    map<string,int> data;
    for (int i=0; i<n; i++) {
        cin >> name >> k;
        data[name]+=k;
    }

    vector<vector<string>> box(10001,vector<string>());
    for (auto p : data) {
        auto [k,v]=p;
        box[v].push_back(k);
    }

    cout << data.size() << "\n";
    for (int i=10000; i>0; i--) {
        if (!box[i].empty()) {
            sort(box[i].begin(),box[i].end());
            for (auto s : box[i]) {
                cout << s << " " << i << "\n";
            }
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