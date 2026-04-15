#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin  >> m >> n; // 0,0 ~ m,m

    int x=0,y=0,dir=0; // 0123 동남서북
    string order;
    int d;

    bool err=false;
    int delta[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
    for (int i=0; i<n; i++) {
        cin >> order >> d;
        // cout << order << " " << dir << " / " << x << " " << y << "\n";
        if (order=="TURN") {
            dir=(dir+4+(d?-1:1))%4;
        } else { // move
            auto [dx, dy]=delta[dir];
            if (0<=x+(dx*d) && x+(dx*d)<=m && 0<=y+(dy*d) && y+(dy*d)<=m) {
                x+=dx*d;
                y+=dy*d;
            }else {
                err=true;
                break;
            }
        }
    }

    if (err) {
        cout << -1;
    } else {
        cout << x << " " << y;
    }
    return 0;
}