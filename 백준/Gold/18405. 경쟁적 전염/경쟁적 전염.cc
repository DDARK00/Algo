#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    cin >> n >> k;

    vector<vector<pair<int,int>>> v_pos(k+1);
    vector<vector<int>> board(n,vector<int>(n));
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> board[i][j];
            if (board[i][j]!=0) {
                v_pos[board[i][j]].push_back({i,j});
            }
        }
    }

    vector<pair<int,int>> delta={{1,0},{0,1},{-1,0},{0,-1}};
    int s, ex, ey;
    cin >> s >> ex >> ey;
    // 1~k size n, cnt s

    queue<pair<int,int>> q;
    queue<pair<int,int>> nxt_q;
    for (int i=1; i<k+1; i++) {
        for (auto k : v_pos[i]) {
            q.push(k);
        }
    }

    for (int i=0; i<s; i++) {
        while (!q.empty()){
            auto [x,y]=q.front();
            q.pop();
            for (auto k : delta) {
                auto [dx,dy]=k;
                if (x+dx>=0&&x+dx<n&&y+dy>=0&&y+dy<n&&board[x+dx][y+dy]==0) {
                    board[x+dx][y+dy]=board[x][y];
                    nxt_q.push({x+dx,y+dy});
                }
             }
        }
        q=nxt_q;
        nxt_q={};
    }

    cout << board[ex-1][ey-1];
    return 0;
}