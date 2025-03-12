#include <iostream>
#include <tuple>
#include <unordered_map>
using namespace std;

const int MAX_SIZE = 1000;
char ar[MAX_SIZE][MAX_SIZE];
int visited[MAX_SIZE][MAX_SIZE]{};
unordered_map<char,tuple<int,int>> delta = {{'U',{-1,0}},{'D',{1,0}},{'L',{0,-1}},{'R',{0,1}}};

int dx, dy, nx, ny;
int ans = 1;
int dfs(int x, int y){
    tie(dx, dy) = delta[ar[x][y]];
    nx = x+dx;
    ny = y+dy;
    visited[x][y] = ans; // temp

    if (visited[nx][ny]==0){
        visited[x][y]=dfs(nx, ny);
    }else if(visited[nx][ny]==ans){
        ans+=1;
        return ans-1;
    }
    visited[x][y]=visited[nx][ny];
    return visited[nx][ny];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    cin >> n >> m;

    for (int i=0;i<n;i++) {
        for (int j=0;j<m;j++){
            cin >> ar[i][j];
        }
    }
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            if (visited[i][j]==0){
                dfs(i,j);
            }
        }
    }
    cout << ans-1;
    return 0;
}