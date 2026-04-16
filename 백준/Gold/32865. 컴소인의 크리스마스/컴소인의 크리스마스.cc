#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    // 1->0 2->1 3->2
    // at least 1 0

    int n, s;
    cin >> n; // 200000

    int k=0;
    vector<int> zero;
    vector<pair<int,int>> st;
    for (int i=0; i<n; i++) {
        cin >> s;
        k+=s;
        if (s==0) {
            zero.push_back(i+1);
        } else {
            st.push_back({s,i+1});
        }
    }

    if (k!=n-1 || zero.size()==0) {
        cout << -1;
        return 0;
    }

    auto cmp=[](auto a, auto b){return a.first<b.first;};
    sort(st.begin(),st.end(),cmp);

    // 40만
    int idx=0;
    for (auto p : st) {

        for (int i=p.first; i>0; i--) {
            cout << zero[idx] << "\n" << p.second << "\n";
            idx++;
        }
        zero.push_back(p.second);
    }
    cout << zero[zero.size()-1];
    return 0;
}