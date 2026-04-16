#include <iostream>
#include <queue>
using namespace std;

int t, h, w;
char ground[100][100];
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};

void solve() {
    cin >> h >> w;
    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            cin >> ground[i][j];
        }
    }

    int answer=0;
    queue<pair<int,int>> q;
    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            if (ground[i][j]=='#') {
                answer++;
                q.push({i,j});
                ground[i][j]='.';
                while (!q.empty()) {
                    auto [x,y]=q.front();q.pop();
                    for (int k=0; k<4; k++) {
                        int nx=x+dx[k], ny=y+dy[k];
                        if (0<=nx&&nx<h&&0<=ny&&ny<w&&ground[nx][ny]=='#') {
                            q.push({nx,ny});
                            ground[nx][ny]='.';
                        }
                    }
                }
            }
        }
    }

    cout << answer << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;
    for (int i=0; i<t; i++) {
        solve();
    }
    return 0;
}