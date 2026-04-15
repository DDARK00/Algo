#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 012
// 345
// 678
vector<vector<int>> delta = {{1,3},{0,2},{1,5},{0,6},{},{2,8},{3,7},{6,8},{5,7}};
void solve() {
    char board[9];
    for (int i=0; i<9; i++) {
        cin >> board[i];
    }

    vector<int>st;
    vector<int> answer;
    for (int i=0; i<9; i++) {
        if (board[i]=='O') {
            st.push_back(i);
        } else {
            continue;
        }
        int cnt=1, v;
        while (!st.empty()) {
            v=st.back();
            st.pop_back();
            board[v]='X';
            for (auto k:delta[v]) {
                if (board[k]=='O') {
                    cnt++;
                    board[k]='X';
                    st.push_back(k);
                }
            }
        }
        answer.push_back(cnt);
    }

    sort(answer.begin(),answer.end());

    int n, k;
    cin >> n;
    int rst=1;
    if (answer.size()!=n) {
        rst=0;
    }
    for (int i=0; i<n; i++) {
        cin >> k;
        if (i>=answer.size() || k!=answer[i]) {
            rst=0;
        }
    }

    cout << rst << "\n";
}

int main() {
    int tc;
    cin >> tc;
    for (int i=0; i<tc; i++) {
        solve();
    }
    return 0;
}