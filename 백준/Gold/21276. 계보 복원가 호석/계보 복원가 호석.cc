#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    vector<string> names(n);
    for (int i=0; i<n; i++) {
        cin >> names[i];
    }
    sort(names.begin(),names.end());
    unordered_map<string,int> deg;
    unordered_map<string,vector<string>> info;

    cin >> n;
    string a, b;
    for (int i=0; i<n; i++) {
        cin >> a >> b; // a조상이 b
        deg[a]++;
        info[b].push_back(a);
    }

    unordered_map<string, vector<string>> answer;
    vector<string> st; // 시조
    for (auto k : names) {
        if (deg[k]==0) {
            st.push_back(k);
        }
    }
    cout << st.size() << "\n";
    sort(st.begin(),st.end());
    for (auto k : st) {
        cout << k << " ";
    }
    cout << "\n";

    while (!st.empty()){
        a=st.back();
        st.pop_back();
        for (auto k : info[a]) {
            deg[k]--;
            if (deg[k]==0) {
                st.push_back(k);
                answer[a].push_back(k);
            }
        }
    }
    for (auto k : names) {
        cout << k << " " << answer[k].size() << " ";
        sort(answer[k].begin(),answer[k].end());
        for (auto l : answer[k]) {
            cout << l << " ";
        }
        cout << "\n";
    }
    return 0;
}