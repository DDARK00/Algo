#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    int x=50, y=50;
    string s;
    cin >> n >> s;
    
    vector<vector<char>> maze(101, vector<char>(101,'#'));
    maze[50][50]='.';
    int xl=50, xr=50, yl=50, yr=50, d=1; // 동 남 서 북
    int dx[4]={0,1,0,-1};
    int dy[4]={1,0,-1,0};
    for (auto c : s) {
        if (c=='R') {
            d=(d+1)%4;
        } else if (c=='L') {
            d=(d+3)%4;
        } else {
            x+=dx[d];
            y+=dy[d];
            xl=min(xl,x);
            xr=max(xr,x);
            yl=min(yl,y);
            yr=max(yr,y);
            maze[x][y]='.';
        }
    }
    for (int i=xl; i<xr+1; i++) {
        for (int j=yl; j<yr+1; j++) {
            cout << maze[i][j];
        }
        cout << "\n";
    }

    return 0;
}