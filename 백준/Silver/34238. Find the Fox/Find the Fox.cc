#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;

    vector<string> board(n);
    for (int i=0; i<n; i++) {
        cin >> board[i];
    }

    int answer=0;
    // 8방향
    int delta[8][2]={{1,0},{0,1},{-1,0},{0,-1},{1,-1},{1,1},{-1,1},{-1,-1}};
    char chk[2]={'O','X'};
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (board[i][j]=='F') {
                for (int d=0; d<8; d++) {
                    auto [dx, dy]=delta[d];
                    for (int k=1; k<4; k++) {
                        if (k==3) {
                            answer++;
                            continue;
                        }
                        int nx=i+dx*k,ny=j+dy*k;
                        if (nx<0 || ny<0 || nx==n || ny==m || board[nx][ny]!=chk[k-1]) {
                            break;
                        }
                    }
                }
            }
        }
    }
    cout << answer;
    return 0;
}