#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const long long MAX_MONEY=5000000;
void solve() {
    vector<long long> ttang;
    int value;
    cin >> value;
    while (value!=0) {
        ttang.push_back(value);
        cin >> value;
    }

    sort(ttang.begin(),ttang.end(),greater<long long>());
    long long answer=0, tmp;
    for (int i=0; i<ttang.size(); i++) {
        tmp=ttang[i];
        for (int j=0; j<i; j++) {
            tmp=tmp*ttang[i];
        }
        tmp*=2;
        answer+=tmp;
        if (answer>MAX_MONEY) {
            cout << "Too expensive\n";
            return;
        }
    }
    cout << answer << "\n";
    return;
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