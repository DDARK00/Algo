#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    int board[50][50];
    int answer=0;

    string temp;
    for (int i=0; i<n; i++) {
        cin >> temp;
        for (int j=0; j<m; j++) {
            board[i][j] = temp[j]-'0';
        }
    }

    for (int i=n-1; i>=0; i--) {
        for (int j=m-1; j>=0; j--) {
            if (board[i][j]){
                answer++;
                for (int k=0; k<=i; k++) {
                    for (int l=0; l<=j; l++) {
                        board[k][l]^=1;
                    }
                }
            }
        }
    }
    cout << answer;
    return 0;
}