#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

template <typename T>
using min_pq=priority_queue<T, vector<T>, greater<T>>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, t, r, c;
    cin >> n >> t >> r >> c;

    vector<string> board(500);
    for (int i=0; i<n; i++) {
        cin >> board[i];
    }

    // 상하좌우 가까운 워프
    int near[4][500][500]; // 100만
    for (int i=0; i<n; i++) {
        int last=-1;
        for (int j=0; j<n; j++) { // L -> R
            near[0][i][j]=last;
            if (board[i][j]=='#') last=j;
        }
        last=-1;
        for (int j=n-1; j>=0; j--) { // R -> L
            near[1][i][j]=last;
            if (board[i][j]=='#') last=j;
        }
        last=-1;
        for (int j=0; j<n; j++) { // U -> D
            near[2][j][i]=last;
            if (board[j][i]=='#') last=j;
        }
        last=-1;
        for (int j=n-1; j>=0; j--) { // D -> U
            near[3][j][i]=last;
            if (board[j][i]=='#') last=j;
        }
    }

    vector dist(n+1,vector(n+1,vector(2,1e9)));
    dist[0][0][0]=0;
    // 0,0 -> r-1,c-1

    min_pq<tuple<int,int,int,int>> pq;
    pq.push({0,0,0,0}); // w, x, y, type

    vector<pair<int,int>> delta={{0,1},{1,0},{-1,0},{0,-1}};

    while (!pq.empty()) {
        auto [w,x,y,z]=pq.top();pq.pop();
        if (dist[x][y][z]<w) continue;
        for (auto d : delta) {
            auto [dx,dy]=d;
            if (0<=x+dx&&x+dx<n&&0<=y+dy&&y+dy<n&&dist[x+dx][y+dy][0]>w+1) {
                pq.push({w+1,x+dx,y+dy,0});
                dist[x+dx][y+dy][0]=w+1;
            }
        }

        if (!z) w+=t;
        for (int i=0; i<4; i++) { // 01 x,k 23 k,y
            int k=near[i][x][y];
            if (k==-1) continue;
            int nx=i/2?k:x, ny=i/2?y:k;
            if (dist[nx][ny][1]>w+1) {
                dist[nx][ny][1]=w+1;
                pq.push({w+1,nx,ny,1});
            }
        }
    }

    cout << min(dist[r-1][c-1][0],dist[r-1][c-1][1]);
    return 0;
}