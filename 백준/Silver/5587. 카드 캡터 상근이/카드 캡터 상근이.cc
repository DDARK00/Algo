#include <iostream>
#include <queue>
using namespace std;

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;

    int temp;
    int t[201]{};

    for (int i=0; i<n; i++) {
        cin >> temp;
        t[temp]=1;
    }

    int turn = 1;
    int c[2]={n,n};
    bool flag=false;

    while (!flag){
        for (int i=1; i<2*n+1; i++) {
            if (t[i]==turn){
                t[i]=turn+2;
                c[turn]--;
                if (c[turn]==0) {
                    flag=true;
                    break;
                }
                turn^=1;
            }
        }
        turn^=1;
    }

    cout << c[0] << "\n" << c[1];
    return 0;
}