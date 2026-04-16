#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

vector<vector<int>> board(201, vector<int>(201));
int r, c, n;

void print() {
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cout << (board[i][j]>0?"O":".");
        }
        cout << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> r >> c >> n; // 200 200 200

    n--;
    char tmp;

    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cin >> tmp;
            board[i][j] = tmp=='O'?2:0;
        }
    }

    int dx[] ={0,0,1,-1};
    int dy[] ={1,-1,0,0};
    queue<pair<int,int>> q;

    while (n>0) {
        for (int i=0; i<r; i++) {
            for (int j=0; j<c; j++) {
                if (board[i][j]==1) {
                    q.push({i,j});
                    board[i][j]--;
                }else if (board[i][j]==0) {
                    board[i][j]=3;
                }else {
                    board[i][j]--;
                }
            }
        }

        while (!q.empty()) {
            auto [x, y]=q.front(); q.pop();
            for (int i=0; i<4; i++) {
                if (x+dx[i]<r && x+dx[i]>=0 && y+dy[i]<c && y+dy[i]<=c) {
                    board[x+dx[i]][y+dy[i]]=0;
                }
            }
        }

        n--;
        // print();
        // cout << "--- \n";
    }
    print();
    return 0;

}