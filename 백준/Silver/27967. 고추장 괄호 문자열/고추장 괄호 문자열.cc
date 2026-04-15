#include <iostream>
#include <vector>
#include <map>
using namespace std;

int n;
string s;
vector<int> arr;
vector<char> selected;
map<char, int> chk={{'(',1},{')',-1}};
char st[2]={'(',')'};

bool solve(int k, int val, bool ok){
    if (val<0 || ok) {
        return ok;
    }

    if (k==n) {
        if (val==0) {
            for (auto a : selected) {
                cout << a;
            }
            ok=1;
        }
        return ok;
    }

    if (s[k]=='G') {
        for (int i=0; i<2; i++) {
            selected.push_back(st[i]);
            ok=solve(k+1,val+chk[st[i]],ok);
            selected.pop_back();
        }
    } else {
        selected.push_back(s[k]);
        ok=solve(k+1,val+chk[s[k]],ok);
        selected.pop_back();
    }
    return ok;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    cin >> s;
    solve(0,0,0);
    return 0;
}