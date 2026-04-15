#include <iostream>
#include <tuple>
#include <queue>
#include <vector>
using namespace std;

int l; // board size
vector<vector<int>> visited(301, vector<int>(301, 0));
vector<vector<int>> cnt(301, vector<int>(301, 0)); // answer

vector<pair<int,int>> delta={{1,2},{2,1},{1,-2},{2,-1},{-1,2},{-2,1},{-1,-2},{-2,-1}};

void bfs(int& x, int& y, int& ex, int& ey, int i){
    queue<pair<int,int>> q;
    q.push({x,y});
    visited[x][y]=i;
    cnt[x][y]=0;
    while (!q.empty()){
        tie(x,y)=q.front();
        q.pop();
        if (x==ex && y==ey) {
            return;
        }
        for (auto d : delta) {
            auto [dx,dy]=d;
            if (x+dx>=0 && y+dy>=0 && x+dx<l && y+dy<l && visited[x+dx][y+dy]!=i) {
                cnt[x+dx][y+dy]=cnt[x][y]+1;
                visited[x+dx][y+dy]=i;
                q.push({x+dx,y+dy});
            }
        }
    }
}

void solve(int i){
    // init
    cin >> l;
    int sx, sy, ex, ey;
    cin >> sx >> sy >> ex >>ey;
    bfs(sx,sy,ex,ey,i);
    cout << cnt[ex][ey] << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    for (int i=0; i<tc; i++) {
        solve(i+1);
    }
    return 0;
}