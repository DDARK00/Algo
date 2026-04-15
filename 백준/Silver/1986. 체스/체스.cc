#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, r, c, cnt;
    cin >> n >> m;
    vector<vector<int>> board(n, vector<int>(m));

    cin >> cnt; // q
    vector<pair<int,int>> q_pos;
    for (int i=0; i<cnt; i++) {
        cin >> r >> c;
        q_pos.push_back({r-1,c-1});
        board[r-1][c-1]=-1;
    }

    cin >> cnt; // k
    vector<pair<int,int>> k_pos;
    for (int i=0; i<cnt; i++) {
        cin >> r >> c;
        board[r-1][c-1]=-1;
        k_pos.push_back({r-1,c-1});
    }

    cin >> cnt; // p
    for (int i=0; i<cnt; i++) {
        cin >> r >> c;
        board[r-1][c-1]=-1;
    }

    vector<pair<int,int>> d_q={{-1,0},{1,0},{0,-1},{0,1},{1,1},{-1,-1},{1,-1},{-1,1}};
    cnt=q_pos.size()+2;
    for (auto q : q_pos) {
        auto [r, c]=q;
        board[r][c]=cnt;
        for (auto d : d_q) {
            auto [nr, nc]=d;
            int dr=nr, dc=nc;
            while (r+dr>=0 && r+dr < n && c+dc >= 0 && c+dc < m && board[r+dr][c+dc]!=-1 && board[r+dr][c+dc]!=cnt){
                board[r+dr][c+dc]=cnt;
                dr+=nr;
                dc+=nc;
            }
        }
        cnt--;
    }

    vector<pair<int,int>> d_k={{1,2},{2,1},{-1,2},{2,-1},{1,-2},{-2,1},{-1,-2},{-2,-1}};
    for (auto k : k_pos) {
        auto [r, c]=k;
        for (auto d : d_k) {
            auto [nr, nc]=d;
            int dr=nr, dc=nc;
            if (r+dr>=0 && r+dr < n && c+dc >= 0 && c+dc < m){
                board[r+dr][c+dc]=-1;
            }
        }
    }

    int answer=0;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            // cout << board[i][j] << " ";
            answer+=board[i][j]==0;
        }
        // cout << "\n";
    }

    cout << answer << "\n";
    return 0;
}