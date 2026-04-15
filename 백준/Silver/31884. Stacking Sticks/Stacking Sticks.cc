#include <iostream>
#include <unordered_map>

using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int q, cmd, x;
    cin >> q;
    // -10e9 ~ 10e9
    unordered_map<int,int> board;

    for (int i=0; i<q; i++) {
        cin >> cmd >> x;
        switch (cmd) {
            case 1:{
                int mx=0;
                for (int j=x; j<x+4; j++) {
                    mx=max(mx,board[j]);
                }
                mx++;
                for (int j=x; j<x+4; j++) {
                    board[j]=mx;
                }
                break;}
            case 2:{
                board[x]+=4;
                break;}
            case 3:{
                cout << board[x] << "\n";
                break;}
        }
    }
    return 0;
}