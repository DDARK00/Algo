#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int r, c;
    cin >> r >> c;

    vector<vector<int>> grid(r,vector<int>(c));

    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> visited(r,vector<int>(c,0));
    queue<pair<int,int>> q;
    q.push({0,0});
    visited[0][0]=1;

    int dx[4]={0,0,1,-1};
    int dy[4]={1,-1,0,0};
    int cnt=0, time=0;
    while (true) {
        vector<pair<int,int>> pos;
        queue<pair<int,int>> nxt_q;

        while (!q.empty()) {
            auto [x,y]=q.front();q.pop();
            for (int i=0; i<4; i++) {
                int nx=x+dx[i];
                int ny=y+dy[i];
                if (0<=nx && nx<r && 0<=ny && ny<c){
                    if (visited[nx][ny]==0) {
                        if (grid[nx][ny]) {
                            nxt_q.push({nx,ny});
                        } else {
                            q.push({nx,ny});
                        }
                        visited[nx][ny]=1;
                    }
                }
            }
        }
        if (nxt_q.empty()) {
            break;
        }
        time++;
        cnt=nxt_q.size();
        q=nxt_q;
    }
    cout << time << "\n" << cnt << "\n";
    return 0;
}