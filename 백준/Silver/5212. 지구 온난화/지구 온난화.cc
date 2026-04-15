#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int r, c;
    cin >> r >> c;

    vector<vector<char>> board(r+2, vector<char>(c+1));
    for (int i=1; i<r+1; i++) {
        for (int j=1; j<c+1; j++) {
            cin >>board[i][j];
        }
    }

    int sx=r+2, sy=c+2, ex=0, ey=0;
    vector<vector<char>> new_board(r+2, vector<char>(c+2,'.'));
    vector<vector<int>> delta={{1,0},{0,1},{-1,0},{0,-1}};
    for (int i=1; i<r+1; i++) {
        for (int j=1; j<c+1; j++) {
            if (board[i][j]=='X') {
                int cnt=0;
                for (auto k : delta) {
                    if (board[k[0]+i][k[1]+j]=='X') {
                        cnt++;
                    }
                }
                if (cnt>1) {
                    new_board[i][j]='X';
                    sx=min(sx,i);
                    sy=min(sy,j);
                    ex=max(ex,i);
                    ey=max(ey,j);
                }
            }
        }
    }

    for (int i=sx; i<=ex; i++) {
        for (int j=sy; j<=ey; j++) {
            cout << new_board[i][j];
        }
        cout << "\n";
    }
    return 0;
}