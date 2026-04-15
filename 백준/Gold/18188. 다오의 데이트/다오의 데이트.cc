#include <iostream>
#include <queue>
#include <map>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int h, w;
    cin >> h >> w;
    char grid[20][20];
    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            cin >> grid[i][j];
        }
    }

    int sx, sy, ex, ey;
    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            if (grid[i][j]=='D') {
                sx=i;
                sy=j;
            } else if (grid[i][j]=='Z') {
                ex=i;
                ey=j;
            }
        }
    }

    // wasd 0123
    map<char,int> change={{'W',0},{'A',1},{'S',2},{'D',3}};
    map<int,char> r_change={{0,'W'},{1,'A'},{2,'S'},{3,'D'}};
    int delta[4][2]={{-1,0},{0,-1},{1,0},{0,1}};
    int r_delta[4][2]={{1,0},{0,1},{-1,0},{0,-1}};

    int visited[21][20][20]{}; //n h w

    int n;
    cin >> n;
    char b, c;
    vector<vector<int>> order(20,vector<int>(2));
    for (int i=0; i<n; i++) {
        cin >> b >> c;
        order[i][0]=change[b];
        order[i][1]=change[c];
    }

    queue<tuple<int,int,int>> q; // cnt x y
    visited[0][sx][sy]=1;
    q.push({0,sx,sy});
    while (!q.empty()) {
        auto [cnt,x,y]=q.front();q.pop();
        if (cnt==n) {
            break;
        }
        for (auto k : order[cnt]) {
            auto [dx,dy]=delta[k];
            int nx=x+dx, ny=y+dy;
            if (0<=nx&&nx<h&&0<=ny&&ny<w&&grid[nx][ny]!='@'&&visited[cnt+1][nx][ny]==0) {
                visited[cnt+1][nx][ny]=k+1; // from, 1 2 3 4
                q.push({cnt+1,nx,ny});
            }
        }
    }

    for (int i=1; i<n+1; i++) {
        if (visited[i][ex][ey]!=0) {
            cout << "YES\n"; // Z->D
            vector<char> ans;
            int tx=ex, ty=ey;
            for (int j=i; j>0; j--) {
                // 1 2 3 4 w a s d, s w d a
                int k=visited[j][tx][ty]-1;
                ans.push_back(r_change[k]);
                tx=tx+r_delta[k][0];
                ty=ty+r_delta[k][1];
            }

            for (int j=ans.size()-1; j>=0; j--) {
                cout << ans[j];
            }
            return 0;
        }
    }
    cout << "NO\n";
    return 0;
}