#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, t;
    cin >> n;

    int pfs_r[402][402]{}; // a
    int pfs_l[402][402]{}; // b
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> t;
            pfs_r[i+1][j+1]=pfs_r[i][j]+t;
            pfs_l[i+1][j+1]=pfs_l[i][j+2]+t;
        }
    }

    int answer=-1e9; // 400 400 1000
    // 123 r 1  2  3  l 1  2  3
    // 456   4  6  8    6  8  6
    // 789   7  12 15   15 14 9
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            for (int k=1; k<n; k++) {
                if (i+k>=n || j+k>=n) {
                    break;
                }
                int a=pfs_r[i+1+k][j+1+k]-pfs_r[i][j];
                int b=pfs_l[i+1+k][j+1]-pfs_l[i][j+2+k];
                answer=max(answer,a-b);
            }
        }
    }

    cout << answer;
    return 0;
}