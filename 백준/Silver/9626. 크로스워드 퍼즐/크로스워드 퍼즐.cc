#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int m, n;
    cin >> m >> n;
    int u, l, r, d;
    cin >> u >> l >> r >> d;
    vector<string> puzzle(m);
    
    for (int i=0; i<m; i++) {
        cin >> puzzle[i];
    }

    string deco[]={"#","."};
    for (int i=0; i<u; i++) {
        for (int j=0; j<l+r+n; j++) {
            cout << deco[(i+j)%2];
        }
        cout << "\n";
    }

    for (int i=0; i<m; i++) {
        for (int x=0; x<l; x++) {
            cout << deco[(u+x+i)%2];
        }
        cout << puzzle[i];
        for (int y=0; y<r; y++) {
            cout << deco[(u+l+y+n+i)%2];
        }
        cout << "\n";
    }

    for (int i=0; i<d; i++) {
        for (int j=0; j<l+r+n; j++) {
            cout << deco[(u+j+i+m)%2];
        }
        cout << "\n";
    }
    
    return 0;
}