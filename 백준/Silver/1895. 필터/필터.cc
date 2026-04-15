#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int img[41][41];
    int r, c;
    cin >> r >> c;
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cin >> img[i][j];
        }
    }

    int t, arr[9], answer=0;
    cin >> t;
    for (int i=0; i<r-2; i++) {
        for (int j=0; j<c-2; j++) {
            for (int k=0; k<9; k++) {
                arr[k]=img[i+k/3][j+k%3];
            }
            sort(arr,arr+9);
            answer+=arr[4]>=t;
        }
    }

    cout << answer;
    return 0;
}