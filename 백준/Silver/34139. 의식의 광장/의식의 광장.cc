#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int h, n, r, c;
    cin >> h >> n;

    vector<int> answer(n);
    vector<pair<int,int>> temp;
    for (int i=0; i<n; i++) {
        cin >> r >> c;
        temp.push_back({c,i});
    }
    auto cmp=[](auto a,auto b){return a.first>b.first;};
    sort(temp.begin(),temp.end(),cmp);

    for (auto k : temp) {
        answer[k.second]=n;
        n--;
    }

    cout << "YES" << "\n";
    for (auto k : answer) {
        cout << k << " ";
    }
    return 0;
}