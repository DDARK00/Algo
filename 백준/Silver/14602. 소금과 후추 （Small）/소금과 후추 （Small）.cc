#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, k, w;
    cin >> n >> m >> k >> w;
    vector<vector<int>> board(n, vector<int>(m,0));
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> board[i][j];
        }
    }

    vector<vector<int>> answer(n-w+1, vector<int> (m-w+1,0));
    for (int i=0; i<n-w+1; i++) {
        for (int j=0; j<m-w+1; j++) {
            vector<int> tmp;
            for (int x=0; x<w; x++) {
                for (int y=0; y<w; y++) {
                    tmp.push_back(board[x+i][y+j]);
                }
            }
            sort(tmp.begin(),tmp.end());
            cout << tmp[tmp.size()/2] << " ";
        }
        cout << "\n";
    }
    return 0;
}