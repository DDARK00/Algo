#include <iostream>
using namespace std;

int main() {
    int n, t;
    cin  >> n >> t;

    string order;
    int time, bef=0;
    int xy[]={0, 0};
    int dir=0;
    int delta[4][2]= {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};
    for (int i=0; i<n; i++) {
        cin >> time >> order;
        xy[0]+=(time-bef)*delta[dir][0];
        xy[1]+=(time-bef)*delta[dir][1];
        bef=time;
        dir=order=="right"?(dir+1)%4 : (4+dir-1)%4;
    }
    xy[0]+=(t-bef)*delta[dir][0];
    xy[1]+=(t-bef)*delta[dir][1];

    cout << xy[0] << " " << xy[1] << "\n";
    
    return 0;
}