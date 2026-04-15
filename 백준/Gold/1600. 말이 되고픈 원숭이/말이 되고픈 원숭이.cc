#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int k, w, h;
int bfs(int board[201][201]){
    int dx[4] = {0,0,1,-1};
    int dy[4] = {1,-1,0,0};
    int hdx[8] = {-2, -1, 1, 2, 2, 1, -1, -2};
    int hdy[8] = {1, 2, 2, 1, -1, -2, -2, -1};

    queue<tuple<int, int, int>> q;
    // x, y, k
    q.push({0,0,0});

    int visited[201][201][31]{};
    visited[0][0][0]=1;

    int x, y, z, nx, ny;
    while(!q.empty()){
        tie(x, y, z) = q.front();q.pop();
        if (x==h-1 && y==w-1){
            return visited[x][y][z]-1;
        }
        if (z<k){
            for (int i=0; i<8; i++) {
                nx = x+hdx[i];
                ny = y+hdy[i];
                if (0<=nx && nx<h && 0<=ny && ny<w && board[nx][ny]!=1 && visited[nx][ny][z+1]==0 ) {
                q.push({nx,ny,z+1});
                visited[nx][ny][z+1]=visited[x][y][z]+1;
                }
            }
        }

        for (int i=0; i<4; i++) {
            nx = x+dx[i];
            ny = y+dy[i];
            if (0<=nx && nx<h && 0<=ny && ny<w && board[nx][ny]!=1 && visited[nx][ny][z]==0 ) {
                q.push({nx,ny,z});
                visited[nx][ny][z]=visited[x][y][z]+1;
            }
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // init
    cin >> k >> w >> h;
    int board[201][201];
    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            cin >> board[i][j];
        }
    }

    // bfs
    cout << bfs(board);
    return 0;
}