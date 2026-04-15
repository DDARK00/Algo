#include <iostream>
#include <unordered_map>
using namespace std;

int solve(string s, int dist) {
    if (dist==s.size()) {
        return 1;
    }
    unordered_map<string, int> chk;
    string ss;
    for (int i=0; i<s.size()-dist; i++) {
        ss=s[i];
        ss+=s[i+dist];
        if (chk[ss]) {
            return 0;
        }
        chk[ss]=1;
    }
    return solve(s, dist+1);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;

    while (true) {
        cin >> s;
        if (s=="*") {
            break;
        }
        cout << s;
        if (solve(s,1)) {
            cout << " is surprising.\n";
        } else {
            cout << " is NOT surprising.\n";
        }
    }
    return 0;
}