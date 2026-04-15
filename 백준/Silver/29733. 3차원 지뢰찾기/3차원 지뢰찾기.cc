#include <iostream>
#include <vector>
using namespace std;
struct Node {
    bool isMine;
    int value;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int r, c, h;
    cin >> r >> c >> h;

    vector mine(h,vector(r,vector(c,'.')));
    for (int i=0; i<h; i++) {
        for (int j=0; j<r; j++) {
            for (int k=0; k<c; k++) {
                cin >> mine[i][j][k];
            }
        }
    }

    vector<vector<vector<Node>>> answer(h,vector<vector<Node>> (r,vector<Node>(c,{false,0})));
    for (int i=0; i<h; i++) {
        for (int j=0; j<r; j++) {
            for (int k=0; k<c; k++) {
                if (mine[i][j][k]=='*') {
                    answer[i][j][k].isMine=true;
                    for (int l=-1; l<2; l++) {
                        if (l+i>=h||l+i<0) {
                            continue;
                        }
                        for (int m=-1; m<2; m++) {
                            if (m+j>=r||m+j<0) {
                                continue;
                            }
                            for (int n=-1; n<2; n++) {
                                if (n+k>=c||n+k<0) {
                                    continue;
                                }
                                answer[l+i][m+j][n+k].value++;
                            }
                        }
                    }
                }
            }
        }
    }

    for (int i=0; i<h; i++) {
        for (int j=0; j<r; j++) {
            for (int k=0; k<c; k++) {
                if (answer[i][j][k].isMine) {
                    cout << "*";
                } else {
                    cout << answer[i][j][k].value%10;
                }
            }
            cout << "\n";
        }
    }
    return 0;
}