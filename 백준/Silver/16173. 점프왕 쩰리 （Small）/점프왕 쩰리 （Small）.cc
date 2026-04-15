#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n; // n=2or3
    int board[3][3];
    for (int i=0; i<n*n; i++) {
        cin >> board[i/n][i%n];
    }
    queue<pair<int,int>> q;
    q.push({0,0});

    bool ok=false;
    while (!q.empty()){
        auto [x, y] = q.front();
        q.pop();
        int k=board[x][y];
        if (k==-1){
            ok=true;
            break;
        }
        if (k!=0 && x+k<n){
            q.push({x+k,y});
        }
        if (k!=0 && y+k<n){
            q.push({x,y+k});
        }
    }
    if (ok){
        cout << "HaruHaru";
    }else{
        cout << "Hing";
    }
    return 0;
}