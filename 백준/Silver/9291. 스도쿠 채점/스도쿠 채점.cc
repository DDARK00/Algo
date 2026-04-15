#include <iostream>
#include <vector>
using namespace std;

void solve(int tc) {
    int tmp;
    bool cor=true;
    vector<int> x(9,0);
    vector<int> y(9,0);
    vector<int> z(9,0);
    for (int i=0; i<9; i++) {
        for (int j=0; j<9; j++) {
            if (cor) {
                cin >> tmp;
                tmp = 1<<tmp-1;
                if ((x[i]|tmp) == x[i]) {
                    cor=false;
                }
                x[i]|=tmp;
                if ((y[j]|tmp) == y[j]) {
                    cor=false;
                }
                y[j]|=tmp;
                if ((z[i/3*3+j/3]|tmp) == z[i/3*3+j/3]) {
                    cor=false;
                }
                z[i/3*3+j/3]|=tmp;
            } else {
                cin >> tmp;
            }
        }
    }

    cout << "Case " << tc;
    if (cor) {
        cout << ": CORRECT\n";
    } else {
        cout << ": INCORRECT\n";
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int tc;
    cin >> tc;
    for (int i=1; i<tc+1; i++) {
        solve(i);
    }

    return 0;
}