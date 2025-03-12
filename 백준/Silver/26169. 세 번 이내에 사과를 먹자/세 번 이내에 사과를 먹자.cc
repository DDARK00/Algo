#include <iostream>
using namespace std;

int dfs(int x, int y, int depth, int apple);
int board[5][5];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    // 5*5 0-4 init
    for (int i=0;i<5;i++){
        for (int j=0;j<5;j++){
            cin >> board[i][j];
        }
    }
    int sx, sy;
    cin >> sx >> sy;
    if (dfs(sx, sy, 0, 0)){
        cout<<1;
    }else{
        cout<<0;
    }
    return 0;
}
int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};

int dfs(int x, int y, int depth, int apple){
    // cout << x << y << "\n";
    if(depth==4)return 0;
    if(apple==2)return 1;
    if(depth>1 && apple ==0) return 0;
    int nx, ny, origin;
    for(int i=0; i<4; i++){
        nx = x+dx[i];
        ny = y+dy[i];
        if(nx<0||nx>4||ny<0||ny>4||board[nx][ny]==-1)continue;
        origin = board[x][y];
        board[x][y] = -1;
        if(dfs(x+dx[i],y+dy[i],depth+1, apple+board[nx][ny])){
            return 1;
        }
        board[x][y] = origin;
    }
    return 0;
}